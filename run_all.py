"""
run_all.py - sends every prompt in prompts/tasks.csv to an AI model and saves the replies.

Usage:
    python run_all.py --model gemini
    python run_all.py --model groq
    python run_all.py --model groq-small

Saves each reply to: generated/<model>/<task_id>_<language>.py
Files that already exist are skipped, so you can stop (Ctrl + C) and
re-run at any time without wasting free quota.
"""

import argparse
import os
import time

import pandas as pd
from dotenv import load_dotenv

# ---- Settings ----
MODEL_IDS = {
    "gemini": "gemini-flash-lite-latest",
    "groq": "openai/gpt-oss-120b",
    "groq-small": "auto",     # picks the first small model below that Groq offers
}
# Small, cheap models to try for "groq-small", in order of preference
SMALL_GROQ_CANDIDATES = [
    "llama-3.1-8b-instant",
    "openai/gpt-oss-20b",
    "gemma2-9b-it",
    "llama-3.2-3b-preview",
]
TASKS_FILE = "prompts/tasks.csv"
# Every prompt style we test. Columns missing from the sheet are skipped.
LANGUAGES = [
    "english", "hinglish", "benglish",                        # clean, formal versions
    "english_casual", "hinglish_casual", "benglish_casual",   # how people really type
    "hinglish_devanagari",                                    # Hinglish in Hindi script
]
WAIT_SECONDS = 6              # pause after each request (free-tier rate limits)


# ---- Read the --model option from the command line ----
parser = argparse.ArgumentParser(description="Send MixCheck prompts to an AI model.")
parser.add_argument("--model", choices=list(MODEL_IDS), default="gemini",
                    help="which model to use (default: gemini)")
args = parser.parse_args()
model = args.model
model_id = MODEL_IDS[model]

load_dotenv()                 # reads your keys from .env


# ---- One "ask" function per model. Both take a prompt and return the reply text ----
if model == "gemini":
    from google import genai
    gemini_client = genai.Client()          # uses GEMINI_API_KEY automatically

    def ask(prompt):
        response = gemini_client.models.generate_content(
            model=model_id, contents=prompt, config={"temperature": 0}
        )
        return response.text

elif model in ("groq", "groq-small"):
    from groq import Groq
    groq_client = Groq()                    # uses GROQ_API_KEY automatically

    if model_id == "auto":
        # Ask Groq which models exist right now, then take the first small one
        available = {m.id for m in groq_client.models.list().data}
        model_id = next((m for m in SMALL_GROQ_CANDIDATES if m in available), None)
        if model_id is None:
            print("None of the small models are available on Groq right now.")
            print("Available models:", ", ".join(sorted(available)))
            raise SystemExit(1)

    def ask(prompt):
        response = groq_client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return response.choices[0].message.content


# ---- Read the sheet ----
# dtype=str keeps everything as text; keep_default_na=False turns empty cells into "".
tasks = pd.read_csv(TASKS_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")

# Only use language columns that actually exist in the sheet
languages = [lang for lang in LANGUAGES if lang in tasks.columns]
for lang in LANGUAGES:
    if lang not in languages:
        print(f"Warning: no '{lang}' column in {TASKS_FILE}, skipping that language")

output_folder = os.path.join("generated", model)
os.makedirs(output_folder, exist_ok=True)
# Remember exactly which model made these files (useful for the pitch and the judges)
with open(os.path.join(output_folder, "model_id.txt"), "w", encoding="utf-8") as f:
    f.write(model_id + "\n")

total_jobs = len(tasks) * len(languages)
job_number = 0
saved = skipped = failed = 0

print(f"Model: {model} ({model_id})")
print(f"{len(tasks)} tasks x {len(languages)} languages = {total_jobs} prompts\n")

for _, row in tasks.iterrows():
    task_id = row["task_id"].strip()

    for language in languages:
        job_number += 1
        label = f"[{job_number}/{total_jobs}] {task_id} {language}"
        output_path = os.path.join(output_folder, f"{task_id}_{language}.py")
        prompt = row[language].strip()

        if os.path.exists(output_path):
            print(f"{label}: already done, skipping")
            skipped += 1
            continue

        if prompt == "":
            print(f"{label}: prompt cell is empty, skipping")
            skipped += 1
            continue

        print(f"{label}: asking {model}...", end=" ", flush=True)
        try:
            reply = ask(prompt)
            if not reply:
                raise ValueError("the model sent back an empty reply")

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(reply)
            print("saved")
            saved += 1
        except Exception as e:
            if "tool_use_failed" in str(e):
                # The model tried to call a tool instead of answering. Retrying gives the
                # same result every time, so we record it as a failed answer.
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write("# MODEL ERROR: the model tried to call a tool instead of writing code\n")
                print("model broke the format (recorded as a fail)")
                saved += 1
            else:
                # Don't save anything, so this one is retried on the next run
                print(f"FAILED ({type(e).__name__}: {str(e)[:150]})")
                failed += 1

        time.sleep(WAIT_SECONDS)

print(f"\nDone. Saved: {saved}, skipped: {skipped}, failed: {failed}")
if failed:
    print("Run the script again later to retry the failed ones.")