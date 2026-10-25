"""
mixtag.py - colours each word of a prompt by its language.

Used by the dashboard's Mix Dial. It's a simple word list approach, tuned to
MixCheck's own prompts, so it's an approximate picture of how mixed a prompt is.

    tag_words("ek fn likho jo list sort kare", "hinglish_casual")
    -> [("ek", "hi"), ("fn", "en"), ("likho", "hi"), ...]
Tags: "en" English, "hi" Hindi, "bn" Bengali, "kn" Kannada, "ta" Tamil, "or" Odia,
"code" names, numbers and symbols.
"""

import re

# English words that also appear inside the mixed prompts
EXTRA_ENGLISH = {
    "answer", "convert", "duplicate", "formula", "maintain", "read", "separate",
    "small", "space", "total", "vowel", "end", "bro", "full", "reverse", "letter",
}
# Words that look English but are Hindi/Bengali in these prompts ("to" = "then")
FORCE_NATIVE = {"hi": {"to"}, "bn": set(), "kn": set(), "ta": set(), "or": set()}

DEVANAGARI = re.compile(r"[ऀ-ॿ]")
BENGALI = re.compile(r"[ঀ-৿]")
CODEISH = re.compile(r"[_()\[\]{}=*+×\"'<>0-9]")


def _core(token):
    return token.strip(".,?!:;।").lower()


def build_english_vocab(tasks, english_columns=("english", "english_casual")):
    vocab = set(EXTRA_ENGLISH)
    for column in english_columns:
        if column in tasks.columns:
            for text in tasks[column]:
                for token in re.split(r"[\s/]+", text):
                    vocab.add(_core(token))
    return vocab


NATIVE_BY_PREFIX = {
    "hinglish": "hi",   # Hindi
    "benglish": "bn",   # Bengali
    "kanglish": "kn",   # Kannada
    "tanglish": "ta",   # Tamil
    "odia": "or",       # Odia
}


def native_language(version):
    for prefix, code in NATIVE_BY_PREFIX.items():
        if version.startswith(prefix):
            return code
    return "en"


def tag_words(text, version, english_vocab):
    """Return a list of (token, tag). Splits on spaces, keeps punctuation on the token."""
    native = native_language(version)
    tagged = []
    for token in text.split():
        core = _core(token)
        if DEVANAGARI.search(token):
            tag = "hi"
        elif BENGALI.search(token):
            tag = "bn"
        elif len(core) == 1 and core.isalpha():
            # "a" is English; Bengali uses "e" as a word ("string e" = "in the string")
            tag = "en" if native == "en" else ("bn" if native == "bn" and core == "e" else "code")
        elif not core or CODEISH.search(core):
            tag = "code"
        elif native != "en" and core in FORCE_NATIVE.get(native, set()):
            tag = native
        elif native == "en" or any(part in english_vocab for part in core.split("/")):
            # "shuru/end/beech": English if any part is English, else native
            parts = core.split("/")
            if native != "en" and len(parts) > 1 and not all(p in english_vocab for p in parts):
                tag = native
            else:
                tag = "en"
        else:
            tag = native
        tagged.append((token, tag))
    return tagged


def mix_level(tagged):
    """Share of words (ignoring names, numbers and symbols) that are not English."""
    words = [tag for _, tag in tagged if tag != "code"]
    if not words:
        return 0.0
    return sum(tag not in ("en", "code") for tag in words) / len(words)
