"""
regrade_compare.py - grades every saved reply again with the current grader and compares
with results/results.csv. Use it after changing grade.py: the scores should not change.

    python checks/regrade_compare.py
"""

import os
import sys

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from grade import grade  # noqa: E402

results = pd.read_csv("results/results.csv", keep_default_na=False)
different = 0
for n, r in enumerate(results.itertuples(), start=1):
    path = os.path.join("generated", r.model, f"{r.task_id}_{r.language}.py")
    with open(path, encoding="utf-8") as f:
        reply = f.read()
    if reply.startswith("# MODEL ERROR"):
        continue
    passed, total, error = grade(reply, os.path.join("tests", f"{r.task_id}.py"))
    if passed != int(r.passed_cases):
        different += 1
        print(f"DIFFERENT {r.model} {r.task_id} {r.language}: was {r.passed_cases}, now {passed}  ({error})")
    if n % 50 == 0:
        print(f"...checked {n} of {len(results)}")

print(f"\nDone: {different} answers scored differently.")
print("All good, the new grader gives the same scores." if different == 0 else "Send this output to Claude.")
