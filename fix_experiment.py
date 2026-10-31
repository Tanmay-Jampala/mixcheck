"""
fix_experiment.py - can the Kanglish gap be fixed? Tests two simple fixes a coding tool could apply.

  guard      add one fixed English line to the prompt:
             "Reply with only one Python code block and nothing else. Name the function exactly <name>."
  translate  ask the model to translate the prompt into English first, then send the translation

Runs on the Kanglish prompts with both GPT-OSS models (the two that ignored "only code").
Saves replies to generated_fixes/<fix>/<model>/ (skips ones it already has, so you can stop and
re-run), then grades them into results/fixes.csv. The dashboard shows the comparison.

Usage:
    python fix_experiment.py
"""

import os
import time

import pandas as pd

from grade import followed_format, grade
from models import ask

VERSION = "kanglish_casual"
MODELS = ["groq", "groq-small"]
FIXES = ["guard", "translate"]
WAIT_SECONDS = 3            # Groq's free tier allows about 30 requests a minute
OUT_FOLDER = "generated_fixes"
RESULTS_FILE = "results/fixes.csv"

GUARD_LINE = "\n\nReply with only one Python code block and nothing else. Name the function exactly {name}."
TRANSLATE_ASK = ("Translate this request into clear English. Keep every code name, number and symbol exactly "
                 "as it is. Reply with only the English translation.\n\n{prompt}")


def ask_with_retry(model, prompt):
    for attempt in range(3):
        try:
            return ask(model, prompt)
        except Exception as e:
            if "tool_use_failed" in str(e):
                return "# MODEL ERROR: the model tried to call a tool instead of writing code\n"
            print(f"   (error: {type(e).__name__}, retrying in 20 s)")
            time.sleep(20)
    raise RuntimeError("the model kept failing; run the script again later")


tasks = pd.read_csv("prompts/tasks.csv", dtype=str, keep_default_na=False, encoding="utf-8-sig")
jobs = [(fix, model, row) for fix in FIXES for model in MODELS for _, row in tasks.iterrows()]

for n, (fix, model, row) in enumerate(jobs, start=1):
    task_id, name, prompt = row["task_id"].strip(), row["function_name"].strip(), row[VERSION].strip()
    folder = os.path.join(OUT_FOLDER, fix, model)
    os.makedirs(folder, exist_ok=True)
    out_path = os.path.join(folder, f"{task_id}_{VERSION}.py")
    if os.path.exists(out_path):
        continue
    print(f"[{n}/{len(jobs)}] {fix} {model} {task_id}...", flush=True)
    if fix == "guard":
        reply = ask_with_retry(model, prompt + GUARD_LINE.format(name=name))
    else:
        english = ask_with_retry(model, TRANSLATE_ASK.format(prompt=prompt)).strip()
        with open(os.path.join(folder, f"{task_id}_{VERSION}_translation.txt"), "w", encoding="utf-8") as f:
            f.write(english)
        time.sleep(WAIT_SECONDS)
        reply = ask_with_retry(model, english)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(reply or "")
    time.sleep(WAIT_SECONDS)

# Grade every saved reply
rows = []
for fix in FIXES:
    for model in MODELS:
        for _, row in tasks.iterrows():
            task_id = row["task_id"].strip()
            path = os.path.join(OUT_FOLDER, fix, model, f"{task_id}_{VERSION}.py")
            if not os.path.exists(path):
                continue
            with open(path, encoding="utf-8") as f:
                reply = f.read()
            test_file = os.path.join("tests", f"{task_id}.py")
            if reply.startswith("# MODEL ERROR"):
                passed, total, error = 0, 1, reply.strip("# \n")
            else:
                passed, total, error = grade(reply, test_file)
            rows.append({"fix": fix, "model": model, "task_id": task_id, "language": VERSION,
                         "passed_cases": passed, "total_cases": total, "passed_all": total > 0 and passed == total,
                         "followed_format": followed_format(reply), "error": error or ""})

fixes = pd.DataFrame(rows)
fixes.to_csv(RESULTS_FILE, index=False, encoding="utf-8")
print(f"\nSaved {len(fixes)} rows to {RESULTS_FILE}\n")

base = pd.read_csv("results/results.csv", keep_default_na=False)
base["followed_format"] = base["followed_format"].astype(str).str.lower() == "true"
base["passed_all"] = base["passed_all"].astype(str).str.lower() == "true"
print("=== Kanglish: correct code | replied with only code ===")
for model in MODELS:
    b = base[(base["model"] == model) & (base["language"] == VERSION)]
    print(f"{model}:")
    print(f"  no fix      {int(b['passed_all'].sum())}/{len(b)} correct  |  {int(b['followed_format'].sum())}/{len(b)} only code")
    for fix in FIXES:
        f_ = fixes[(fixes["model"] == model) & (fixes["fix"] == fix)]
        print(f"  {fix:<11} {int(f_['passed_all'].sum())}/{len(f_)} correct  |  {int(f_['followed_format'].sum())}/{len(f_)} only code")


# Refresh the database the dashboard reads (see db.py)
import db  # noqa: E402
db.build()
print(f"Updated {db.DB_FILE}")
