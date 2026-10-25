"""
check_keys.py - quickly checks that your Gemini and Groq API keys work.

Run:  python check_keys.py
It sends one tiny message to each model and prints OK or the problem.
It never prints your keys.
"""

from dotenv import load_dotenv

load_dotenv()  # reads GEMINI_API_KEY and GROQ_API_KEY from .env

GEMINI_MODEL = "gemini-flash-lite-latest"
GROQ_MODEL = "openai/gpt-oss-120b"
TEST_PROMPT = "Reply with just the word OK."

# ---- Gemini ----
try:
    from google import genai

    client = genai.Client()
    reply = client.models.generate_content(model=GEMINI_MODEL, contents=TEST_PROMPT)
    print("Gemini: OK  (it replied:", (reply.text or "").strip()[:20] + ")")
except Exception as e:
    print("Gemini: FAILED  ->", type(e).__name__, str(e)[:200])

# ---- Groq ----
try:
    from groq import Groq

    client = Groq()
    reply = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": TEST_PROMPT}],
    )
    text = reply.choices[0].message.content or ""
    print("Groq:   OK  (it replied:", text.strip()[:20] + ")")
except Exception as e:
    print("Groq:   FAILED  ->", type(e).__name__, str(e)[:200])
