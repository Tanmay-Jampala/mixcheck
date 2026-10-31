"""
apply_kanglish_review.py - applies the native-speaker review of the Kanglish prompts
(see prompts/kanglish_review.md), then re-runs and re-grades ONLY the changed prompts.

Usage:
    python apply_kanglish_review.py

Backups it makes first:
    prompts/tasks_before_review.csv
    generated_before_review/<model>/<task>_kanglish_casual.py
"""

import os
import re
import shutil
import subprocess
import sys

import pandas as pd

TASKS_FILE = "prompts/tasks.csv"
COLUMN = "kanglish_casual"
MODELS = ["gemini", "groq", "groq-small"]
WORD_FIXES = {
    "ondE": "onde", "eraDne": "eradne", "eraDralli": "eradralli", "eraDu": "eradu",
    "heLu": "helu", "tagoLLi": "tagolli", "uLibeku": "ulibeku",
    "irbahudu": "irabahudu", "saryaagi": "sariyagi",
}

tasks = pd.read_csv(TASKS_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")

# 1. Fix the prompts
changed = []
for i, row in tasks.iterrows():
    old = row[COLUMN]
    new = old[len("guru "):] if old.startswith("guru ") else old
    for before, after in WORD_FIXES.items():
        new = re.sub(rf"\b{before}\b", after, new)
    if new != old:
        tasks.at[i, COLUMN] = new
        changed.append(row["task_id"].strip())
        print(f"{row['task_id']}:\n  before: {old}\n  after:  {new}\n")

if not changed:
    print("Nothing to change: the review is already applied.")
    sys.exit(0)

shutil.copyfile(TASKS_FILE, "prompts/tasks_before_review.csv")
tasks.to_csv(TASKS_FILE, index=False, encoding="utf-8")
print(f"Updated {len(changed)} Kanglish prompts: {', '.join(changed)}")

# 2. Move the old replies for those prompts aside, so run_all.py asks again
for model in MODELS:
    for task_id in changed:
        old_reply = os.path.join("generated", model, f"{task_id}_{COLUMN}.py")
        if os.path.exists(old_reply):
            backup_folder = os.path.join("generated_before_review", model)
            os.makedirs(backup_folder, exist_ok=True)
            shutil.move(old_reply, os.path.join(backup_folder, f"{task_id}_{COLUMN}.py"))

# 3. Ask the models again (run_all.py skips every reply that still exists)
for model in MODELS:
    print(f"\n===== Re-running {model} =====")
    subprocess.run([sys.executable, "run_all.py", "--model", model], check=False)

# 4. Grade everything again
print("\n===== Grading =====")
subprocess.run([sys.executable, "grade_all.py"], check=False)
print("\nDone. Restart the dashboard (Ctrl + C, then streamlit run app.py) to see the new results.")
