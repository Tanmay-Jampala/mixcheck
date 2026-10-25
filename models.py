"""
models.py - one place that knows how to talk to each AI model.

Used by the dashboard (app.py) for the live test box.
    from models import ask, model_name
    reply_text = ask("gemini", "Write a Python function ...")
"""

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()  # reads GEMINI_API_KEY and GROQ_API_KEY from .env

MODEL_IDS = {
    "gemini": "gemini-flash-lite-latest",
    "groq": "openai/gpt-oss-120b",
    "groq-small": "auto",
}
SMALL_GROQ_CANDIDATES = [
    "llama-3.1-8b-instant",
    "openai/gpt-oss-20b",
    "gemma2-9b-it",
    "llama-3.2-3b-preview",
]


@lru_cache(maxsize=None)
def _gemini_client():
    from google import genai
    return genai.Client()


@lru_cache(maxsize=None)
def _groq_client():
    from groq import Groq
    return Groq()


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


def ask(model, prompt):
    """Send one prompt to a model and return its reply text (temperature 0)."""
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
