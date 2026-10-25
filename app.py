"""
app.py - the MixCheck dashboard.

Run:  streamlit run app.py
  Hero              the Mix Dial: drag to rewrite one prompt in another language
  Results           scoreboard, a clickable results grid, failures by version
  Guess the verdict a game for the audience: will the AI's code pass?
  Failures          every failed answer, with the prompt and the AI's code
  Try it live       English vs mixed face-off, or test a single prompt
  How it works      the method, for judges
Look and feel: ui.py (styles) and widgets.py (interactive parts).
"""

import os
import random

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

import ui
import widgets
from grade import grade, strip_fences
from mixtag import build_english_vocab, mix_level, tag_words

RESULTS_FILE = "results/results.csv"
TASKS_FILE = "prompts/tasks.csv"

VERSIONS = {
    "english": "English",
    "english_casual": "English, casual",
    "hinglish": "Hinglish",
    "hinglish_casual": "Hinglish, casual",
    "hinglish_devanagari": "Hinglish in Hindi script",
    "benglish": "Benglish",
    "benglish_casual": "Benglish, casual",
    "kanglish_casual": "Kanglish, casual",
    "tanglish_casual": "Tanglish, casual",
    "odia_casual": "Odia-English, casual",
}
MODELS = {"gemini": "Gemini", "groq": "Groq (big)", "groq-small": "Groq (small)"}
TITLES = {
    "reverse_string": "Reverse a string", "count_vowels": "Count the vowels",
    "find_largest": "Find the largest number", "is_palindrome": "Check for a palindrome",
    "remove_duplicates": "Remove duplicates", "sum_even_numbers": "Add up the even numbers",
    "factorial": "Factorial", "second_largest": "Second-largest number", "count_words": "Count the words",
    "fibonacci": "Fibonacci number", "celsius_to_fahrenheit": "Celsius to Fahrenheit",
    "capitalize_words": "Capitalise every word", "word_count": "Count each word",
    "are_anagrams": "Check for anagrams", "missing_number": "Find the missing number",
}

st.set_page_config(page_title="MixCheck", layout="wide")
ui.inject_styles()


# ---------------------------------------------------------------
# Data
# ---------------------------------------------------------------
@st.cache_data
def load_results():
    df = pd.read_csv(RESULTS_FILE, keep_default_na=False)
    df["passed_all"] = df["passed_all"].astype(str).str.lower() == "true"
    return df


@st.cache_data
def load_tasks():
    return pd.read_csv(TASKS_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def read_code(model, task_id, version):
    path = os.path.join("generated", model, f"{task_id}_{version}.py")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return strip_fences(f.read())


def exact_model_id(model):
    path = os.path.join("generated", model, "model_id.txt")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    return ""


def title_of(function_name):
    return TITLES.get(function_name, function_name.replace("_", " ").capitalize())


results = load_results()
tasks = load_tasks()
models = [m for m in MODELS if m in set(results["model"])]
models += sorted(set(results["model"]) - set(models))
versions = [v for v in VERSIONS if v in set(results["language"])]
task_rows = {r["task_id"]: r for _, r in tasks.iterrows()}
english_vocab = build_english_vocab(tasks)
lookup = {(r.model, r.task_id, r.language): r for r in results.itertuples()}

version_list = [{"key": v, "label": VERSIONS.get(v, v)} for v in versions]
model_list = [{"key": m, "label": MODELS.get(m, m)} for m in models]


# ---------------------------------------------------------------
# Hero: the Mix Dial
# ---------------------------------------------------------------
@st.cache_data
def dial_data(_results_len):
    dial_tasks, most_fails, start = [], -1, 0
    for i, (task_id, row) in enumerate(task_rows.items()):
        prompts, res, fails = {}, {}, 0
        for v in versions:
            if v in tasks.columns and row[v]:
                words = tag_words(row[v], v, english_vocab)
                prompts[v] = {"words": words, "mix": round(mix_level(words), 3)}
            res[v] = {}
            for m in models:
                r = lookup.get((m, task_id, v))
                if r is not None:
                    res[v][m] = [int(r.passed_cases), int(r.total_cases)]
                    fails += 0 if r.passed_all else 1
        if fails > most_fails:
            most_fails, start = fails, i
        dial_tasks.append({"title": title_of(row["function_name"]), "prompts": prompts, "results": res})
    total = len(results)
    return {
        "versions": version_list, "models": model_list, "tasks": dial_tasks,
        "start_task": start, "start_version": 0,
        "facts": [[str(total), "answers graded by running the code"], [str(len(tasks)), "coding tasks"],
                  [str(len(versions)), "ways of asking"], [str(len(models)), "AI models"]],
    }


components.html(widgets.mix_dial(dial_data(len(results))), height=650, scrolling=False)

tab_results, tab_game, tab_failures, tab_live, tab_how = st.tabs(
    ["Results", "Guess the verdict", "Failures", "Try it live", "How it works"]
)

# ---------------------------------------------------------------
# Results
# ---------------------------------------------------------------
with tab_results:
    total = len(results)
    passed = int(results["passed_all"].sum())
    ui.section("The scoreboard", "Every answer counts as a pass only if its code passes every test case.")
    ui.stats([
        (f"{total}", "answers graded", ui.T["brand"]),
        (f"{100 * passed / total:.1f}%", "passed every test case", ui.T["pass"]),
        (f"{total - passed}", "failed answers", ui.T["fail"]),
        (f"{len(models)} × {len(versions)}", "models × ways of asking", ui.T["accent"]),
    ])

    by_version = results.groupby("language")["passed_all"].agg(["sum", "count"]).reindex(versions)
    by_version["fails"] = by_version["count"] - by_version["sum"]
    hardest = by_version["fails"].idxmax()
    if by_version.loc[hardest, "fails"] > 0:
        rate = 100 * by_version.loc[hardest, "sum"] / by_version.loc[hardest, "count"]
        ui.finding(f"{VERSIONS.get(hardest, hardest)} is the hardest way to ask: "
                   f"{int(by_version.loc[hardest, 'fails'])} failed answers, {rate:.1f}% passed across all models.")
    else:
        ui.finding("Every model passed every task, however it was asked.")

    ui.section("Where the models fail", "Click a cell to open the answers behind it. Red cells had failures.")
    cells = {}
    for m in models:
        cells[m] = {}
        for v in versions:
            rows = results[(results["model"] == m) & (results["language"] == v)]
            if rows.empty:
                continue
            items = []
            for r in rows.itertuples():
                row = task_rows.get(r.task_id)
                items.append({
                    "title": title_of(row["function_name"]) if row is not None else r.task_id,
                    "ok": bool(r.passed_all), "passed": int(r.passed_cases), "cases": int(r.total_cases),
                    "prompt": row[v] if row is not None and v in tasks.columns else "",
                    "code": "" if r.passed_all else read_code(m, r.task_id, v),
                    "error": r.error,
                })
            cells[m][v] = {"passed": int(rows["passed_all"].sum()), "total": len(rows), "items": items}
    components.html(widgets.heat_grid({"versions": version_list, "models": model_list, "cells": cells}),
                    height=600, scrolling=False)

    ui.section("Failed answers by way of asking", "All models together.")
    order = by_version.sort_values("fails")
    bars = go.Figure(go.Bar(
        x=order["fails"], y=[VERSIONS.get(v, v) for v in order.index], orientation="h",
        marker={"color": [ui.VERSION_COLOURS.get(v, ui.T["brand"]) for v in order.index], "cornerradius": 4},
        text=[f"{int(f)} failed" if f else "" for f in order["fails"]], textposition="outside",
        textfont={"color": ui.T["text"]}, hovertemplate="%{y}: %{x} failed answers<extra></extra>",
    ))
    bars.update_layout(
        height=60 + 46 * len(order), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Instrument Sans, Segoe UI, sans-serif", "color": ui.T["muted"], "size": 13},
        margin={"l": 10, "r": 10, "t": 10, "b": 10},
        hoverlabel={"bgcolor": ui.T["surface_2"], "font": {"color": ui.T["text"]}},
    )
    bars.update_xaxes(showgrid=True, gridcolor=ui.T["border"], zeroline=False, dtick=1, ticks="",
                      automargin=True, range=[0, max(3, order["fails"].max() + 1)])
    bars.update_yaxes(tickfont={"color": ui.T["text"], "size": 13}, ticks="", automargin=True)
    st.plotly_chart(bars, width="stretch", theme=None)

    with st.expander("See the full pass-rate table"):
        pivot = (results.assign(pct=results["passed_all"] * 100)
                 .pivot_table(index="model", columns="language", values="pct", aggfunc="mean")
                 .reindex(index=models, columns=versions).round(1))
        pivot.index = [f"{MODELS.get(m, m)} ({exact_model_id(m)})" if exact_model_id(m) else MODELS.get(m, m)
                       for m in pivot.index]
        pivot.columns = [VERSIONS.get(v, v) for v in pivot.columns]
        st.dataframe(pivot.style.format("{:.1f}%"), width="stretch")

# ---------------------------------------------------------------
# Guess the verdict
# ---------------------------------------------------------------
with tab_game:
    ui.section("Can you spot a failure by eye?",
               "Read the prompt and the AI's code, then guess. Hand the laptop to a judge for this one.")
    deck = []
    fails = results[~results["passed_all"]]
    for r in fails.itertuples():
        code = read_code(r.model, r.task_id, r.language)
        if not code or code.startswith("# MODEL ERROR"):
            continue
        row = task_rows[r.task_id]
        deck.append({"title": title_of(row["function_name"]), "version": VERSIONS.get(r.language, r.language),
                     "model": MODELS.get(r.model, r.model), "prompt": row[r.language], "code": code,
                     "ok": False, "passed": int(r.passed_cases), "cases": int(r.total_cases),
                     "why": r.error or f"It ran without crashing, but gave the wrong answer on "
                                       f"{int(r.total_cases - r.passed_cases)} of {int(r.total_cases)} test cases."})
    # Mix in passing answers, preferring casual and mixed prompts
    passes = results[results["passed_all"] & results["language"].str.contains("casual|devanagari")]
    rng = random.Random(7)
    picks = passes.sample(n=min(len(passes), max(4, 10 - len(deck))), random_state=7) if len(passes) else passes
    for r in picks.itertuples():
        code = read_code(r.model, r.task_id, r.language)
        if not code:
            continue
        row = task_rows[r.task_id]
        deck.append({"title": title_of(row["function_name"]), "version": VERSIONS.get(r.language, r.language),
                     "model": MODELS.get(r.model, r.model), "prompt": row[r.language], "code": code,
                     "ok": True, "passed": int(r.passed_cases), "cases": int(r.total_cases),
                     "why": "It gave the right answer on every test case, including the tricky ones."})
    rng.shuffle(deck)
    if deck:
        components.html(widgets.guess_game({"deck": deck[:10]}), height=720, scrolling=False)
    else:
        st.info("Run run_all.py and grade_all.py first, so there are answers to guess about.")

# ---------------------------------------------------------------
# Failures
# ---------------------------------------------------------------
with tab_failures:
    failures = results[~results["passed_all"]]
    ui.section(f"Every failed answer ({len(failures)})", "The prompt, the AI's code, and what went wrong.")
    if failures.empty:
        st.info("No failures yet.")
    for r in failures.itertuples():
        row = task_rows.get(r.task_id)
        name = title_of(row["function_name"]) if row is not None else r.task_id
        ui.failure_card_head(name, r.language, VERSIONS.get(r.language, r.language),
                             MODELS.get(r.model, r.model), r.passed_cases, r.total_cases, r.error)
        left, right = st.columns([1, 1.25])
        with left:
            if row is not None and r.language in tasks.columns:
                ui.bubble("The prompt", row[r.language])
        with right:
            code = read_code(r.model, r.task_id, r.language)
            if code:
                st.code(code, language="python")

# ---------------------------------------------------------------
# Try it live
# ---------------------------------------------------------------
def run_one(model, prompt, task_id):
    """Ask the model and grade the answer. Returns (passed, total, error, code) or raises."""
    from models import ask
    try:
        reply = ask(model, prompt)
    except Exception as e:
        if "tool_use_failed" in str(e):
            return 0, 1, "The model tried to call a tool instead of writing code.", ""
        raise
    ok, n, error = grade(reply, os.path.join("tests", f"{task_id}.py"))
    return ok, n, error, strip_fences(reply)


with tab_live:
    mode = st.radio("Mode", ["Face-off: English vs mixed", "Test one prompt"], horizontal=True,
                    label_visibility="collapsed")
    task_labels = {tid: title_of(r["function_name"]) for tid, r in task_rows.items()}

    if mode.startswith("Face-off"):
        ui.section("English vs mixed, side by side",
                   "The same task in two languages, sent to the same model. Does the language change the result?")
        mixed_options = [v for v in VERSIONS if v in tasks.columns and not v.startswith("english")]
        c1, c2, c3 = st.columns(3)
        start_task = list(task_labels)[dial_data(len(results))["start_task"]]
        task_id = c1.selectbox("Task", list(task_labels), format_func=task_labels.get, key="fo_task",
                               index=list(task_labels).index(start_task))
        mixed = c2.selectbox("Mixed version", mixed_options, format_func=VERSIONS.get,
                             index=mixed_options.index("benglish_casual") if "benglish_casual" in mixed_options else 0)
        model = c3.selectbox("Model", list(MODELS), format_func=MODELS.get, key="fo_model",
                             index=list(MODELS).index("groq") if "groq" in MODELS else 0)
        english_key = "english_casual" if mixed.endswith("casual") and "english_casual" in tasks.columns else "english"
        row = task_rows[task_id]
        left, right = st.columns(2)
        p_left = left.text_area(VERSIONS[english_key], row[english_key], height=120, key=f"fo_l_{task_id}_{english_key}")
        p_right = right.text_area(VERSIONS[mixed], row[mixed], height=120, key=f"fo_r_{task_id}_{mixed}")

        if st.button("Run the face-off"):
            fn = row["function_name"]
            if fn not in p_left or fn not in p_right:
                st.warning(f"Keep the function name {fn} in both prompts, so the tests can find the function.")
            else:
                try:
                    with st.spinner(f"Asking {MODELS[model]} in {VERSIONS[english_key]} and {VERSIONS[mixed]}..."):
                        a = run_one(model, p_left, task_id)
                        b = run_one(model, p_right, task_id)
                    for col, res in ((left, a), (right, b)):
                        with col:
                            ui.verdict(res[0], res[1], res[2])
                            if res[3]:
                                st.code(res[3], language="python")
                    ui.faceoff_summary(VERSIONS[english_key], a[0] == a[1], VERSIONS[mixed], b[0] == b[1])
                except Exception as e:
                    st.error(f"Couldn't reach the model: {type(e).__name__}: {str(e)[:200]}")
                    st.caption("Check the internet connection and the API keys in .env.")
    else:
        ui.section("Test any prompt yourself", "Pick a task, rewrite the prompt however you like, and see if the code passes.")
        version_options = [v for v in VERSIONS if v in tasks.columns]
        c1, c2, c3 = st.columns(3)
        task_id = c1.selectbox("Task", list(task_labels), format_func=task_labels.get, key="one_task")
        start_from = c2.selectbox("Start from", version_options, format_func=VERSIONS.get,
                                  index=version_options.index("hinglish_casual") if "hinglish_casual" in version_options else 0)
        model = c3.selectbox("Model", list(MODELS), format_func=MODELS.get, key="one_model")
        row = task_rows[task_id]
        prompt = st.text_area("Your prompt", row[start_from], height=110, key=f"one_{task_id}_{start_from}")
        if st.button("Ask the AI and test its code"):
            if row["function_name"] not in prompt:
                st.warning(f"Keep the function name {row['function_name']} in the prompt, so the tests can find the function.")
            else:
                ui.bubble("You asked", prompt)
                try:
                    with st.spinner("Asking the AI and running the tests..."):
                        ok, n, error, code = run_one(model, prompt, task_id)
                    ui.verdict(ok, n, error)
                    if code:
                        st.code(code, language="python")
                except Exception as e:
                    st.error(f"Couldn't reach the model: {type(e).__name__}: {str(e)[:200]}")
                    st.caption("Check the internet connection and the API keys in .env.")

# ---------------------------------------------------------------
# How it works
# ---------------------------------------------------------------
with tab_how:
    ui.section("How MixCheck works", "Five steps, from a prompt to a verdict.")
    ui.pipeline([
        ("Paired prompts", f"Each of the {len(tasks)} tasks is written in {len(versions)} ways. "
                           "Every version asks for the same function, so only the language changes."),
        ("Native-speaker checks", "Hinglish is checked by Hindi speakers on our team, Benglish by a Bengali speaker."),
        ("Ask the models", f"Every prompt goes to {len(models)} AI models at temperature 0, so answers are repeatable."),
        ("Run the code", "Each answer runs in a separate process with a time limit, against the same test cases, "
                         "including tricky ones like empty lists."),
        ("Compare", "Passed in English but failed in a mixed version of the same task? "
                    "Then the language caused the failure."),
    ])
    ui.section("Models tested")
    st.markdown(" ".join(
        ui.chip(f"{MODELS.get(m, m)}" + (f": {exact_model_id(m)}" if exact_model_id(m) else ""), c)
        for m, c in zip(models, [ui.T["brand"], ui.T["accent"], "#4CC9F0", ui.T["pass"]])
    ), unsafe_allow_html=True)
    ui.section("About the Mix Dial colours",
               "Words are coloured by language using a word list built from our own prompts, so the "
               "mix percentage is an approximate guide, not an exact linguistic measure.")

ui.footer()
