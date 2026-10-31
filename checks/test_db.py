"""
test_db.py - checks that mixcheck.db holds exactly what the repo's files say.

    python -m pytest checks -q
"""

import os
import sqlite3
import sys

import pandas as pd
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import db  # noqa: E402


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    path = str(tmp_path_factory.mktemp("db") / "mixcheck.db")
    return db.build(path, root=ROOT)


def test_every_table_is_filled(built):
    counts = db.counts(built)
    tasks = pd.read_csv(os.path.join(ROOT, "prompts", "tasks.csv"), dtype=str, encoding="utf-8-sig")
    results = pd.read_csv(os.path.join(ROOT, "results", "results.csv"))
    assert counts["tasks"] == len(tasks)
    assert counts["grades"] == len(results)
    assert counts["answers"] == len(results)       # every graded answer has its full reply stored
    assert counts["prompts"] > 0 and counts["models"] > 0


def test_grades_match_the_results_file(built):
    from_db = db.results_frame(built).set_index(["model", "task_id", "language"]).sort_index()
    csv = pd.read_csv(os.path.join(ROOT, "results", "results.csv"), keep_default_na=False)
    csv = csv.set_index(["model", "task_id", "language"]).sort_index()
    assert (from_db["passed_cases"] == csv["passed_cases"]).all()
    assert (from_db["passed_all"] == (csv["passed_all"].astype(str).str.lower() == "true")).all()
    assert (from_db["followed_format"] == (csv["followed_format"].astype(str).str.lower() == "true")).all()


def test_prompts_match_the_tasks_file(built):
    from_db = db.tasks_frame(built).set_index("task_id")
    csv = pd.read_csv(os.path.join(ROOT, "prompts", "tasks.csv"), dtype=str, keep_default_na=False,
                      encoding="utf-8-sig").set_index("task_id")
    for column in csv.columns:
        assert (from_db.loc[csv.index, column] == csv[column]).all(), column


def test_live_runs_survive_a_rebuild(built):
    db.log_live_run("voice", "groq", "bari code kodu", task_id="task01", model_used="gemini",
                    transcriber="gemini", passed_cases=5, total_cases=5, followed_format=True, path=built)
    db.build(built, root=ROOT)
    with sqlite3.connect(built) as con:
        rows = con.execute("SELECT source, model_asked, model_used FROM live_runs").fetchall()
    assert ("voice", "groq", "gemini") in rows
