"""
models.py - one place that knows how to talk to each AI model.

    from models import ask, ask_with_backup, transcribe, model_name

ask(model, prompt)
    One model only, retried on short outages. Used by the benchmark scripts, because a
    result must always come from the model it is labelled with.

ask_with_backup(model, prompt)
    Used by the dashboard's live test. If a provider is down (outage, data-centre damage,
    rate limit, bad key), it retries, then switches to the other provider and says so.

transcribe(audio, ...)
    Turns a spoken, code-mixed prompt into text. Gemini first, Groq's Whisper as backup.

How it stays up:
    - every request has a timeout, so a dead data centre can't hang the app
    - short outages are retried with growing, randomised waits (exponential backoff)
    - a provider that just failed is skipped for a while (circuit breaker), so the next
      visitor goes straight to the backup instead of waiting for the same timeout
    - Gemini (Google) and Groq run in different companies' data centres, so one going
      down doesn't take the other with it
"""

import os
import random
import re
import time
from dataclasses import dataclass, field
from functools import lru_cache

try:
    from dotenv import load_dotenv
    load_dotenv()  # on a laptop: reads GEMINI_API_KEY and GROQ_API_KEY from .env
except ImportError:  # the GitHub test runner only installs pytest
    pass


def _key(name):
    """API key from the environment (.env on a laptop), or from Streamlit secrets when deployed."""
    value = os.getenv(name)
    if value:
        return value
    try:
        import streamlit as st
        return st.secrets.get(name)
    except Exception:
        return None

MODEL_IDS = {
    "gemini": "gemini-flash-lite-latest",
    "groq": "openai/gpt-oss-120b",
    "groq-small": "openai/gpt-oss-20b",   # pinned: the model all our results use
}
SMALL_GROQ_CANDIDATES = [
    "llama-3.1-8b-instant",
    "openai/gpt-oss-20b",
    "gemma2-9b-it",
    "llama-3.2-3b-preview",
]
PROVIDER = {"gemini": "Google", "groq": "Groq", "groq-small": "Groq"}
# The backup always runs at a different provider, so it lives in a different data centre
BACKUP = {"gemini": "groq", "groq": "gemini", "groq-small": "gemini"}
WHISPER_MODEL = "whisper-large-v3"

TIMEOUT_SECONDS = 30
ATTEMPTS = 3            # tries per model before giving up on it
BACKOFF_SECONDS = 1.0   # first wait; doubles each retry, plus jitter
COOL_OFF_SECONDS = 60   # how long a failed provider is skipped


class ModelUnavailable(RuntimeError):
    """Every model we tried is down. `tried` lists (model, error) pairs."""

    def __init__(self, tried):
        self.tried = tried
        detail = "; ".join(f"{m}: {type(e).__name__}" for m, e in tried)
        super().__init__(f"No model could answer ({detail}).")


@dataclass
class Answer:
    text: str
    model: str                 # the model that actually answered
    asked: str                 # the model we wanted
    tried: list = field(default_factory=list)   # (model, error) for each model that failed

    @property
    def fell_back(self):
        return self.model != self.asked


@dataclass
class Transcript:
    text: str
    service: str               # "gemini" or "whisper"
    tried: list = field(default_factory=list)

    @property
    def fell_back(self):
        return self.service != "gemini"


# ---------- Telling outages apart from real mistakes ----------
def _status(error):
    for attr in ("status_code", "code", "status"):
        value = getattr(error, attr, None)
        if isinstance(value, int):
            return value
    return None


def is_outage(error):
    """True for errors that mean "this provider can't serve us right now":
    timeouts, dropped connections, rate limits, server errors, and missing or rejected keys.
    A bad request (our mistake) is not an outage, so it is never retried or failed over."""
    status = _status(error)
    if status is not None:
        return status in (401, 403, 408, 429) or status >= 500
    name = type(error).__name__
    return any(word in name for word in ("Timeout", "Connection", "Unavailable", "RateLimit", "ServerError")) \
        or isinstance(error, (TimeoutError, ConnectionError, PermissionError))


_down_until = {}   # provider -> time.monotonic() when we may try it again


def _provider_down(model):
    return _down_until.get(PROVIDER[model], 0) > time.monotonic()


def _mark_down(model):
    _down_until[PROVIDER[model]] = time.monotonic() + COOL_OFF_SECONDS


def _with_retries(call):
    """Run call(); on an outage, wait about 1 s, 2 s, 4 s ... (with jitter) and try again."""
    for attempt in range(ATTEMPTS):
        try:
            return call()
        except Exception as e:
            if not is_outage(e) or isinstance(e, PermissionError) or attempt == ATTEMPTS - 1:
                raise
            time.sleep(BACKOFF_SECONDS * 2 ** attempt * (0.5 + random.random()))


# ---------- Clients ----------
@lru_cache(maxsize=None)
def _gemini_client():
    from google import genai
    key = _key("GEMINI_API_KEY")
    if not key:
        raise PermissionError("GEMINI_API_KEY is not set")
    return genai.Client(api_key=key, http_options={"timeout": TIMEOUT_SECONDS * 1000})


@lru_cache(maxsize=None)
def _groq_client():
    from groq import Groq
    key = _key("GROQ_API_KEY")
    if not key:
        raise PermissionError("GROQ_API_KEY is not set")
    # max_retries=0: retries happen here, so they are counted and can fail over
    return Groq(api_key=key, timeout=TIMEOUT_SECONDS, max_retries=0)


@lru_cache(maxsize=None)
def model_name(model):
    """The exact model ID behind a short name like 'groq-small'."""
    model_id = MODEL_IDS[model]
    if model_id != "auto":
        return model_id
    # Use the same small model that run_all.py used, so live tests match the results
    saved = os.path.join("generated", model, "model_id.txt")
    if os.path.exists(saved):
        with open(saved, encoding="utf-8") as f:
            return f.read().strip()
    available = {m.id for m in _groq_client().models.list().data}
    for candidate in SMALL_GROQ_CANDIDATES:
        if candidate in available:
            return candidate
    raise RuntimeError("No small Groq model is available right now.")


def _ask_once(model, prompt):
    if model == "gemini":
        response = _gemini_client().models.generate_content(
            model=model_name(model), contents=prompt, config={"temperature": 0}
        )
        return response.text or ""

    response = _groq_client().chat.completions.create(
        model=model_name(model),
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content or ""


# ---------- Asking for code ----------
def ask(model, prompt):
    """Send one prompt to one model and return its reply text (temperature 0).
    Retries short outages, but never switches model."""
    return _with_retries(lambda: _ask_once(model, prompt))


def ask_with_backup(model, prompt):
    """Like ask(), but if the model's provider is down, the other provider answers.
    Returns an Answer that records who really answered; raises ModelUnavailable if nobody can."""
    tried = []
    backup = BACKUP[model]
    for candidate in (model, backup):
        if candidate != backup and _provider_down(candidate):
            tried.append((candidate, RuntimeError("skipped: it failed less than a minute ago")))
            continue
        try:
            return Answer(text=ask(candidate, prompt), model=candidate, asked=model, tried=tried)
        except Exception as e:
            if not is_outage(e):
                raise
            _mark_down(candidate)
            tried.append((candidate, e))
    raise ModelUnavailable(tried)


# ---------- Voice ----------
# Example sentences steer the transcriber toward the romanised spelling people type in chats
LANGUAGE_HINTS = {
    "hinglish": ("Hindi", "ek python function likho jo list ko reverse kare. sirf code bhejo"),
    "benglish": ("Bengali", "ekta python function likho je list ta reverse kore. shudhu code dao"),
    "kanglish": ("Kannada", "list na reverse maado python function beku. bari code kodu"),
    "tanglish": ("Tamil", "list a reverse panra python function venum. code mattum kudu"),
    "odia": ("Odia", "list ku reverse karuthiba python function lekha. kebala code dia"),
}


def _transcribe_instructions(language, function_name):
    # No example sentence here: Gemini copied words from one into the transcript in testing
    lang, _ = LANGUAGE_HINTS.get(language, ("an Indian language", ""))
    lines = [
        f"Transcribe this recording exactly as spoken, word for word. The speaker mixes {lang} and English.",
        f"Write {lang} words in English letters, the way people type them in WhatsApp chats.",
        "Keep English words in English. Do not translate, correct, complete or summarise anything,",
        "and never add a word that wasn't spoken.",
        "Keep every instruction word, especially words meaning 'only' or 'just'.",
    ]
    if function_name:
        lines.append(f"If the speaker says \"{function_name.replace('_', ' ')}\", write it as {function_name}.")
    lines.append("Reply with the transcript only.")
    return "\n".join(lines)


def _gemini_transcribe(audio, mime_type, instructions):
    from google.genai import types
    response = _gemini_client().models.generate_content(
        model=model_name("gemini"),
        contents=[types.Part.from_bytes(data=audio, mime_type=mime_type), instructions],
        config={"temperature": 0},
    )
    return (response.text or "").strip()


def _whisper_transcribe(audio, language):
    _, example = LANGUAGE_HINTS.get(language, ("", ""))
    result = _groq_client().audio.transcriptions.create(
        file=("speech.wav", audio), model=WHISPER_MODEL, prompt=example, temperature=0,
    )
    return (result.text or "").strip()


def transcribe(audio, mime_type="audio/wav", language="hinglish", function_name=None):
    """Spoken, code-mixed prompt -> text. Gemini first; Groq's Whisper if Google is down."""
    tried = []
    instructions = _transcribe_instructions(language, function_name)
    services = (("gemini", "gemini", lambda: _gemini_transcribe(audio, mime_type, instructions)),
                ("whisper", "groq", lambda: _whisper_transcribe(audio, language)))
    for service, model, call in services:
        if service == "gemini" and _provider_down(model):
            tried.append((service, RuntimeError("skipped: it failed less than a minute ago")))
            continue
        try:
            text = _with_retries(call)
            if function_name:   # people say "reverse string"; the tests need reverse_string
                text = re.sub(r"\b" + r"[\s_-]+".join(map(re.escape, function_name.split("_"))) + r"\b",
                              function_name, text, flags=re.IGNORECASE)
            return Transcript(text=text, service=service, tried=tried)
        except Exception as e:
            if not is_outage(e):
                raise
            _mark_down(model)
            tried.append((service, e))
    raise ModelUnavailable(tried)
