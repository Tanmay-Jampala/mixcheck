"""
grade_all.py - grades every saved AI reply and saves the scores.

Reads:   generated/<model>/<task_id>_<language>.py
Tests:   tests/<task_id>.py
Saves:   results/results.csv
"""

import os

import pandas as pd

from grade import followed_format, grade

GENERATED_FOLDER = "generated"
TESTS_FOLDER = "tests"
RESULTS_FILE = "results/results.csv"
LANGUAGE_ORDER = [                                       # order for the summary
    "english", "hinglish", "benglish",
    "english_casual", "hinglish_casual", "benglish_casual",
    "hinglish_devanagari",
    "kanglish_casual", "tanglish_casual", "odia_casual",
]

rows = []
missing_tests = set()

# Each sub-folder of generated/ is one model (for example generated/gemini)
models = sorted(
    name for name in os.listdir(GENERATED_FOLDER)
    if os.path.isdir(os.path.join(GENERATED_FOLDER, name))
)

for model in models:
    model_folder = os.path.join(GENERATED_FOLDER, model)
    files = sorted(f for f in os.listdir(model_folder) if f.endswith(".py"))
    print(f"\n=== {model}: {len(files)} files ===")

    for file_name in files:
        # "task01_hinglish.py" -> task_id "task01", language "hinglish"
        name_without_py = file_name[:-3]
        if "_" not in name_without_py:
            print(f"{file_name}: name isn't <task_id>_<language>.py, skipping")
            continue
        task_id, language = name_without_py.split("_", 1)

        test_file = os.path.join(TESTS_FOLDER, f"{task_id}.py")
        if not os.path.exists(test_file):
            missing_tests.add(task_id)
            print(f"{file_name}: no {test_file} yet, skipping")
            continue

        with open(os.path.join(model_folder, file_name), encoding="utf-8") as f:
            code_text = f.read()

        if code_text.startswith("# MODEL ERROR:"):
            # The model gave no usable answer at all (see run_all.py)
            from grade import load_tests
            passed, total = 0, len(load_tests(test_file).CASES)
            error = code_text.strip().lstrip("# ").strip()
        else:
            passed, total, error = grade(code_text, test_file)
        passed_all = total > 0 and passed == total
        format_ok = followed_format(code_text)   # did it reply with only the code, as asked?

        status = "PASS" if passed_all else "FAIL"
        print(f"{file_name}: {passed}/{total} {status}" + (f"  ({error})" if error else ""))

        rows.append({
            "model": model,
            "task_id": task_id,
            "language": language,
            "passed_cases": passed,
            "total_cases": total,
            "passed_all": passed_all,
            "error": error or "",
            "followed_format": format_ok,
        })

# Save the results table
os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
results = pd.DataFrame(rows, columns=[
    "model", "task_id", "language", "passed_cases", "total_cases", "passed_all", "error", "followed_format"
])
results.to_csv(RESULTS_FILE, index=False, encoding="utf-8")
print(f"\nSaved {len(results)} rows to {RESULTS_FILE}")

if missing_tests:
    print(f"Skipped tasks with no test file yet: {', '.join(sorted(missing_tests))}")

# Pass rate = share of tasks where the code passed ALL test cases
print("\n=== Pass rate by language (correct code | replied with only code) ===")
for model in results["model"].unique():
    print(f"{model}:")
    model_rows = results[results["model"] == model]
    languages = [l for l in LANGUAGE_ORDER if l in model_rows["language"].values]
    languages += sorted(set(model_rows["language"]) - set(LANGUAGE_ORDER))
    for language in languages:
        lang_rows = model_rows[model_rows["language"] == language]
        fully_passed = int(lang_rows["passed_all"].sum())
        count = len(lang_rows)
        formatted = int(lang_rows["followed_format"].sum())
        print(f"  {language:<20} {fully_passed}/{count} correct ({100 * fully_passed / count:5.1f}%)"
              f"  |  {formatted}/{count} only code ({100 * formatted / count:5.1f}%)")

# Refresh the database the dashboard reads (see db.py)
import db  # noqa: E402
db.build()
print(f"Updated {db.DB_FILE}")
