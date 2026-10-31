"""
db.py - MixCheck's SQLite database: every task, prompt, model answer and grade in one file.

    python build_db.py          # (re)build mixcheck.db from the files in this repo

Tables
    models      model, label, provider, model_id
    tasks       task_id, function_name, checked_by, review_notes
    prompts     task_id, version, text                     (25 tasks x 10 ways of asking)
    answers     model, task_id, version, reply             (each model's full reply)
    grades      model, task_id, version, passed_cases, total_cases, passed_all,
                followed_format, error                     (one row per answer)
    fixes       fix, model, task_id, version, reply, passed_cases, total_cases,
                passed_all, followed_format, error         (the fix experiment)
    live_runs   every test run from the dashboard's "Try it live" tab, typed or spoken

Where the data comes from: prompts/tasks.csv, generated/, results/results.csv,
generated_fixes/ and results/fixes.csv. Those plain files stay in git (easy to review and
diff); the database is rebuilt from them and is what the dashboard reads.

No model is trained here. MixCheck only sends prompts to existing models and grades
their answers.
"""

import os
import sqlite3
from contextlib import closing
from datetime import datetime, timezone

import pandas as pd

DB_FILE = "mixcheck.db"

SCHEMA = """
CREATE TABLE models (
    model       TEXT PRIMARY KEY,
    label       TEXT NOT NULL,
    provider    TEXT NOT NULL,
    model_id    TEXT
);
CREATE TABLE tasks (
    task_id       TEXT PRIMARY KEY,
    function_name TEXT NOT NULL,
    checked_by    TEXT,
    review_notes  TEXT
);
CREATE TABLE prompts (
    task_id  TEXT NOT NULL REFERENCES tasks(task_id),
    version  TEXT NOT NULL,
    text     TEXT NOT NULL,
    PRIMARY KEY (task_id, version)
);
CREATE TABLE answers (
    model    TEXT NOT NULL REFERENCES models(model),
    task_id  TEXT NOT NULL REFERENCES tasks(task_id),
    version  TEXT NOT NULL,
    reply    TEXT NOT NULL,
    PRIMARY KEY (model, task_id, version)
);
CREATE TABLE grades (
    model           TEXT NOT NULL REFERENCES models(model),
    task_id         TEXT NOT NULL REFERENCES tasks(task_id),
    version         TEXT NOT NULL,
    passed_cases    INTEGER NOT NULL,
    total_cases     INTEGER NOT NULL,
    passed_all      INTEGER NOT NULL,
    followed_format INTEGER NOT NULL,
    error           TEXT,
    PRIMARY KEY (model, task_id, version)
);
CREATE TABLE fixes (
    fix             TEXT NOT NULL,
    model           TEXT NOT NULL REFERENCES models(model),
    task_id         TEXT NOT NULL REFERENCES tasks(task_id),
    version         TEXT NOT NULL,
    reply           TEXT,
    passed_cases    INTEGER NOT NULL,
    total_cases     INTEGER NOT NULL,
    passed_all      INTEGER NOT NULL,
    followed_format INTEGER NOT NULL,
    error           TEXT,
    PRIMARY KEY (fix, model, task_id, version)
);
CREATE TABLE IF NOT EXISTS live_runs (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    at              TEXT NOT NULL,
    source          TEXT NOT NULL,          -- 'typed' or 'voice'
    task_id         TEXT,
    model_asked     TEXT NOT NULL,
    model_used      TEXT,                   -- differs from model_asked after a failover
    transcriber     TEXT,                   -- 'gemini' or 'whisper', for voice runs
    prompt          TEXT NOT NULL,
    passed_cases    INTEGER,
    total_cases     INTEGER,
    followed_format INTEGER,
    error           TEXT
);
CREATE INDEX grades_by_version ON grades (version);
"""

LABELS = {"gemini": "Gemini", "groq": "Groq (big)", "groq-small": "Groq (small)"}
PROVIDERS = {"gemini": "Google", "groq": "Groq", "groq-small": "Groq"}
TASK_COLUMNS = {"task_id", "function_name", "checked_by", "needs_check"}


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _bool(series):
    return (series.astype(str).str.lower() == "true").astype(int)


def build(path=DB_FILE, root="."):
    """Build the database from the repo's files. Keeps any live runs already logged."""
    j = lambda *p: os.path.join(root, *p)  # noqa: E731
    old_runs = None
    if os.path.exists(path):
        with closing(sqlite3.connect(path)) as old:
            try:
                old_runs = pd.read_sql("SELECT * FROM live_runs", old)
            except Exception:
                pass

    tmp = path + ".building"
    if os.path.exists(tmp):
        os.remove(tmp)
    with closing(sqlite3.connect(tmp)) as con:
        con.executescript(SCHEMA)

        tasks = pd.read_csv(j("prompts", "tasks.csv"), dtype=str, keep_default_na=False, encoding="utf-8-sig")
        con.executemany("INSERT INTO tasks VALUES (?, ?, ?, ?)",
                        tasks[["task_id", "function_name", "checked_by", "needs_check"]].itertuples(index=False))
        versions = [c for c in tasks.columns if c not in TASK_COLUMNS]
        con.executemany("INSERT INTO prompts VALUES (?, ?, ?)",
                        [(r["task_id"], v, r[v]) for _, r in tasks.iterrows() for v in versions if r[v]])

        model_dirs = sorted(d for d in os.listdir(j("generated")) if os.path.isdir(j("generated", d)))
        for m in model_dirs:
            id_file = j("generated", m, "model_id.txt")
            con.execute("INSERT INTO models VALUES (?, ?, ?, ?)",
                        (m, LABELS.get(m, m), PROVIDERS.get(m, ""),
                         _read(id_file).strip() if os.path.exists(id_file) else None))
            for name in sorted(os.listdir(j("generated", m))):
                if name.endswith(".py") and "_" in name:
                    task_id, version = name[:-3].split("_", 1)
                    con.execute("INSERT INTO answers VALUES (?, ?, ?, ?)",
                                (m, task_id, version, _read(j("generated", m, name))))

        results = pd.read_csv(j("results", "results.csv"), keep_default_na=False)
        con.executemany("INSERT INTO grades VALUES (?, ?, ?, ?, ?, ?, ?, ?)", zip(
            results["model"], results["task_id"], results["language"],
            results["passed_cases"].astype(int), results["total_cases"].astype(int),
            _bool(results["passed_all"]),
            _bool(results["followed_format"]) if "followed_format" in results else [1] * len(results),
            results["error"]))

        fixes_file = j("results", "fixes.csv")
        if os.path.exists(fixes_file):
            fixes = pd.read_csv(fixes_file, keep_default_na=False)
            for r in fixes.itertuples(index=False):
                reply_file = j("generated_fixes", r.fix, r.model, f"{r.task_id}_{r.language}.py")
                con.execute("INSERT INTO fixes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    r.fix, r.model, r.task_id, r.language,
                    _read(reply_file) if os.path.exists(reply_file) else None,
                    int(r.passed_cases), int(r.total_cases),
                    int(str(r.passed_all).lower() == "true"), int(str(r.followed_format).lower() == "true"),
                    r.error))

        if old_runs is not None and not old_runs.empty:
            old_runs.to_sql("live_runs", con, if_exists="append", index=False)
        con.commit()
    os.replace(tmp, path)
    return path


def ensure(path=DB_FILE):
    """Build the database if it isn't there yet (for example on a fresh deploy)."""
    if not os.path.exists(path):
        build(path)
    return path


def connect(path=DB_FILE):
    return sqlite3.connect(ensure(path))


# ---------- Reads used by the dashboard ----------
def results_frame(path=DB_FILE):
    """The grades, shaped exactly like results/results.csv."""
    with closing(connect(path)) as con:
        df = pd.read_sql("""SELECT model, task_id, version AS language, passed_cases, total_cases,
                                   passed_all, error, followed_format
                            FROM grades ORDER BY model, task_id, version""", con)
    df["passed_all"] = df["passed_all"].astype(bool)
    df["followed_format"] = df["followed_format"].astype(bool)
    df["error"] = df["error"].fillna("")
    return df


def tasks_frame(path=DB_FILE):
    """One row per task with a column per way of asking, shaped like prompts/tasks.csv."""
    with closing(connect(path)) as con:
        tasks = pd.read_sql("SELECT * FROM tasks ORDER BY task_id", con)
        prompts = pd.read_sql("SELECT * FROM prompts", con)
    wide = prompts.pivot(index="task_id", columns="version", values="text").reset_index()
    df = tasks.merge(wide, on="task_id", how="left").rename(columns={"review_notes": "needs_check"})
    return df.fillna("").astype(str)


def fixes_frame(path=DB_FILE):
    with closing(connect(path)) as con:
        df = pd.read_sql("""SELECT fix, model, task_id, version AS language, passed_cases, total_cases,
                                   passed_all, followed_format, error FROM fixes""", con)
    df["passed_all"] = df["passed_all"].astype(bool)
    df["followed_format"] = df["followed_format"].astype(bool)
    return df


def reply(model, task_id, version, path=DB_FILE):
    with closing(connect(path)) as con:
        row = con.execute("SELECT reply FROM answers WHERE model = ? AND task_id = ? AND version = ?",
                          (model, task_id, version)).fetchone()
    return row[0] if row else ""


def model_id(model, path=DB_FILE):
    with closing(connect(path)) as con:
        row = con.execute("SELECT model_id FROM models WHERE model = ?", (model,)).fetchone()
    return (row[0] or "") if row else ""


def counts(path=DB_FILE):
    """Row count of every table, for the "about the data" panel."""
    with closing(connect(path)) as con:
        names = [r[0] for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")]
        return {n: con.execute(f"SELECT COUNT(*) FROM {n}").fetchone()[0] for n in names}


# ---------- Writes ----------
def log_live_run(source, model_asked, prompt, task_id=None, model_used=None, transcriber=None,
                 passed_cases=None, total_cases=None, followed_format=None, error=None, path=DB_FILE):
    """Record one "Try it live" run. Never breaks the dashboard if the disk is read-only."""
    try:
        with closing(connect(path)) as con:
            con.execute("""INSERT INTO live_runs (at, source, task_id, model_asked, model_used, transcriber,
                                                  prompt, passed_cases, total_cases, followed_format, error)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (datetime.now(timezone.utc).isoformat(timespec="seconds"), source, task_id, model_asked,
                         model_used, transcriber, prompt, passed_cases, total_cases,
                         None if followed_format is None else int(followed_format), error))
            con.commit()
    except sqlite3.Error:
        pass
