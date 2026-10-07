"""
run_all.py - sends every prompt in prompts/tasks.csv to Gemini and saves the replies.

Saves each reply to: generated/gemini/<task_id>_<language>.py
Files that already exist are skipped, so you can stop (Ctrl + C) and
re-run at any time without wasting free quota.
"""

import os
import time

import pandas as pd
from dotenv import load_dotenv
from google import genai

load_dotenv()                 # reads your keys from .env
client = genai.Client()       # uses GEMINI_API_KEY automatically

MODEL = "gemini-flash-lite-latest"
TASKS_FILE = "prompts/tasks.csv"
OUTPUT_FOLDER = "generated/gemini"
LANGUAGES = ["english", "hinglish", "benglish"]
WAIT_SECONDS = 6              # pause after each request (free-tier rate limits)

# Read the sheet. dtype=str keeps everything as text;
# keep_default_na=False turns empty cells into "" instead of NaN.
tasks = pd.read_csv(TASKS_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")

# Only use language columns that actually exist in the sheet
languages = [lang for lang in LANGUAGES if lang in tasks.columns]
for lang in LANGUAGES:
    if lang not in languages:
        print(f"Warning: no '{lang}' column in {TASKS_FILE}, skipping that language")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

total_jobs = len(tasks) * len(languages)
job_number = 0
saved = skipped = failed = 0

print(f"{len(tasks)} tasks x {len(languages)} languages = {total_jobs} prompts\n")

for _, row in tasks.iterrows():
    task_id = row["task_id"].strip()

    for language in languages:
        job_number += 1
        label = f"[{job_number}/{total_jobs}] {task_id} {language}"
        output_path = os.path.join(OUTPUT_FOLDER, f"{task_id}_{language}.py")
        prompt = row[language].strip()

        if os.path.exists(output_path):
            print(f"{label}: already done, skipping")
            skipped += 1
            continue

        if prompt == "":
            print(f"{label}: prompt cell is empty, skipping")
            skipped += 1
            continue

        print(f"{label}: asking Gemini...", end=" ", flush=True)
        try:
            response = client.models.generate_content(
                model=MODEL, contents=prompt, config={"temperature": 0}
            )
            if not response.text:
                raise ValueError("Gemini sent back an empty reply")

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print("saved")
            saved += 1
        except Exception as e:
            # Don't save anything, so this one is retried on the next run
            print(f"FAILED ({type(e).__name__}: {str(e)[:150]})")
            failed += 1

        time.sleep(WAIT_SECONDS)

print(f"\nDone. Saved: {saved}, skipped: {skipped}, failed: {failed}")
if failed:
    print("Run the script again later to retry the failed ones.")