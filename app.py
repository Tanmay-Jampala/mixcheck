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

import stats
import ui
import widgets
from grade import extract_code, followed_format, grade, strip_fences
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
    if "followed_format" in df.columns:
        df["followed_format"] = df["followed_format"].astype(str).str.lower() == "true"
    else:
        df["followed_format"] = True   # older results files don't have this column
    return df


@st.cache_data
def load_tasks():
    return pd.read_csv(TASKS_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def read_reply(model, task_id, version):
    """The AI's full reply, exactly as it came back."""
    path = os.path.join("generated", model, f"{task_id}_{version}.py")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_code(model, task_id, version):
    """The code we actually tested: the block that defines the function we asked for."""
    reply = read_reply(model, task_id, version)
    row = task_rows.get(task_id)
    return extract_code(reply, row["function_name"] if row is not None else None) if reply else ""


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
                    res[v][m] = [int(r.passed_cases), int(r.total_cases), bool(r.followed_format)]
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


def make_report(results, code_rows, fmt_rows, board):
    """A short shareable summary of the results, as Markdown."""
    lines = ["# MixCheck report", "",
             f"{len(results)} answers graded by running the code: {results['task_id'].nunique()} tasks, "
             f"{results['language'].nunique()} ways of asking, {results['model'].nunique()} models.", "",
             f"- Correct code overall: {100 * results['passed_all'].mean():.1f}%",
             f"- Replied with only code, as asked: {100 * results['followed_format'].mean():.1f}%", "",
             "## Models", "", "| Model | Correct code | Only code | Weakest way of asking |", "|---|---|---|---|"]
    for c, f_, m, w in board:
        lines.append(f"| {MODELS.get(m, m)} ({exact_model_id(m) or m}) | {100 * c:.1f}% | {100 * f_:.1f}% | {VERSIONS.get(w, w)} |")
    lines += ["", "## Against English in the same style", "",
              "| Way of asking | Correct code | p | Only code | p |", "|---|---|---|---|---|"]
    for r in code_rows:
        f_ = fmt_rows.get(r["version"])
        lines.append(f"| {VERSIONS.get(r['version'], r['version'])} | {100 * r['rate']:.1f}% | {r['p']:.3g} | "
                     f"{100 * f_['rate']:.1f}% | {f_['p']:.3g} |" if f_ else "")
    lines += ["", "p = Fisher's exact test, two-sided. Below 0.05 = unlikely to be chance.", "",
              "Made with MixCheck by Team El Rata Alada."]
    return "\n".join(lines)


components.html(widgets.mix_dial(dial_data(len(results))), height=820, scrolling=True)

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
        (f"{100 * results['followed_format'].mean():.1f}%", "replied with only code, as asked", ui.T["accent"]),
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
    by_format = results.groupby("language")["followed_format"].agg(["sum", "count"]).reindex(versions)
    by_format["ignored"] = by_format["count"] - by_format["sum"]
    worst_fmt = by_format["ignored"].idxmax()
    baseline = by_format.loc["english_casual"] if "english_casual" in by_format.index else None
    if by_format.loc[worst_fmt, "ignored"] > 0:
        rate = 100 * by_format.loc[worst_fmt, "sum"] / by_format.loc[worst_fmt, "count"]
        compare = (f" In casual English, {100 * baseline['sum'] / baseline['count']:.0f}% were."
                   if baseline is not None and worst_fmt != "english_casual" else "")
        ui.finding(f"{VERSIONS.get(worst_fmt, worst_fmt)} has the most replies that ignored the instructions: "
                   f"{rate:.0f}% were only code, as asked.{compare}")

    ui.section("Where the models fail", "Switch between the two scores, then click a cell to open the answers behind it.")
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
                    "fmt": bool(r.followed_format),
                    "reply": "" if r.followed_format else read_reply(m, r.task_id, v)[:4000],
                })
            cells[m][v] = {"passed": int(rows["passed_all"].sum()), "formatted": int(rows["followed_format"].sum()),
                           "total": len(rows), "items": items}
    components.html(widgets.heat_grid({"versions": version_list, "models": model_list, "cells": cells}),
                    height=900, scrolling=True)

    ui.section("By way of asking", "All models together. Left: wrong code. Right: replies that ignored \"only code\".")

    def count_bars(counts, word, colour_by_version=True):
        order = counts.sort_values()
        fig = go.Figure(go.Bar(
            x=order.values, y=[VERSIONS.get(v, v) for v in order.index], orientation="h",
            marker={"color": [ui.VERSION_COLOURS.get(v, ui.T["brand"]) for v in order.index], "cornerradius": 4},
            text=[f"{int(c)} {word}" if c else "" for c in order.values], textposition="outside",
            textfont={"color": ui.T["text"]}, hovertemplate="%{y}: %{x} " + word + "<extra></extra>",
        ))
        fig.update_layout(
            height=60 + 40 * len(order), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font={"family": "Instrument Sans, Segoe UI, sans-serif", "color": ui.T["muted"], "size": 13},
            margin={"l": 10, "r": 10, "t": 10, "b": 10},
            hoverlabel={"bgcolor": ui.T["surface_2"], "font": {"color": ui.T["text"]}},
        )
        top = max(3, int(order.max()) + 2)
        fig.update_xaxes(showgrid=True, gridcolor=ui.T["border"], zeroline=False, ticks="", automargin=True,
                         range=[0, top * 1.15], dtick=max(1, top // 6))
        fig.update_yaxes(tickfont={"color": ui.T["text"], "size": 12}, ticks="", automargin=True)
        return fig

    left, right = st.columns(2)
    with left:
        st.plotly_chart(count_bars(by_version["fails"], "wrong"), width="stretch", theme=None)
    with right:
        st.plotly_chart(count_bars(by_format["ignored"], "ignored"), width="stretch", theme=None)

    with st.expander("See the full pass-rate table"):
        pivot = (results.assign(pct=results["passed_all"] * 100)
                 .pivot_table(index="model", columns="language", values="pct", aggfunc="mean")
                 .reindex(index=models, columns=versions).round(1))
        pivot.index = [f"{MODELS.get(m, m)} ({exact_model_id(m)})" if exact_model_id(m) else MODELS.get(m, m)
                       for m in pivot.index]
        pivot.columns = [VERSIONS.get(v, v) for v in pivot.columns]
        st.dataframe(pivot.style.format("{:.1f}%"), width="stretch")

    # ---- Statistics: which gaps are real? ----
    ui.section("Is the gap real, or could it be chance?",
               "Each way of asking against English in the same style (casual vs casual, formal vs formal), "
               "all 3 models together. The range is a 95% confidence range. p is Fisher's exact test: "
               "the chance of a gap at least this big if the language made no difference.")

    def english_for(v):
        if v.startswith("english"):
            return None
        return "english_casual" if v.endswith("casual") else "english"

    code_rows = stats.compare(results, "passed_all", versions, english_for)
    fmt_rows = {r["version"]: r for r in stats.compare(results, "followed_format", versions, english_for)}

    def pct(r):
        return f'{100 * r["rate"]:.0f}% <span style="color:{ui.T["faint"]}">({100 * r["lo"]:.0f}–{100 * r["hi"]:.0f})</span>'

    def pval(p):
        return "&lt; 0.001" if p < 0.001 else f"{p:.2f}"

    def verdict_tag(r):
        if r["p"] >= 0.05:
            return ui.tag("could be chance", "muted")
        return ui.tag("real drop", "fail") if r["rate"] < r["base_rate"] else ui.tag("real gain", "pass")

    table_rows, hot = [], []
    for i, c in enumerate(code_rows):
        f_ = fmt_rows.get(c["version"])
        table_rows.append([
            ui.esc(VERSIONS.get(c["version"], c["version"])),
            pct(c), pval(c["p"]), verdict_tag(c),
            pct(f_) if f_ else "", pval(f_["p"]) if f_ else "", verdict_tag(f_) if f_ else "",
        ])
        if (c["p"] < 0.05) or (f_ and f_["p"] < 0.05):
            hot.append(i)
    ui.table(["Way of asking", "Correct code", "p", "", "Replied with only code", "p", ""], table_rows, hot)

    real = [(r, "correct code") for r in code_rows if r["p"] < 0.05] + \
           [(r, "following \u201conly code\u201d") for r in fmt_rows.values() if r["p"] < 0.05]
    if real:
        parts = [f'{VERSIONS.get(r["version"], r["version"])} on {what} '
                 f'({100 * r["rate"]:.0f}% vs {100 * r["base_rate"]:.0f}%, p {pval(r["p"]).replace("&lt;", "<")})'
                 for r, what in real]
        smallest = min(r["p"] for r in code_rows) if code_rows else 1
        ui.finding("Statistically real: " + "; ".join(parts) + ". "
                   + ("None of the differences in correct code are significant on their own "
                      f"(smallest p = {smallest:.2f}), so those need more runs before we claim them."
                      if all(r["p"] >= 0.05 for r in code_rows) else ""))
    n_tests = max(1, 2 * len(code_rows))
    strict = 0.05 / n_tests
    survivors = [VERSIONS.get(r["version"], r["version"]) for r, _ in real if r["p"] < strict]
    st.caption(f"We made {n_tests} comparisons, so a stricter cut-off (Bonferroni) is p < {strict:.4f}. "
               + (f"Still real at that cut-off: {', '.join(survivors)}." if survivors else "No gap passes that stricter cut-off."))

    # ---- Can it be fixed? (results/fixes.csv, made by fix_experiment.py) ----
    FIXES_FILE = "results/fixes.csv"
    if os.path.exists(FIXES_FILE):
        fixes = pd.read_csv(FIXES_FILE, keep_default_na=False)
        for col in ("passed_all", "followed_format"):
            fixes[col] = fixes[col].astype(str).str.lower() == "true"
        ui.section("Can it be fixed?",
                   "We tried two simple fixes a coding tool could apply on the Kanglish prompts. "
                   "Guard: add one fixed English line, \u201cReply with only one Python code block and nothing else. "
                   "Name the function exactly ...\u201d. Translate: have the model translate the prompt into English first.")
        fix_version = fixes["language"].iloc[0] if not fixes.empty else "kanglish_casual"
        fix_rows, best_gain = [], None
        for m in [m for m in models if m in set(fixes["model"])]:
            b = results[(results["model"] == m) & (results["language"] == fix_version)]
            cells = [f"<b>{ui.esc(MODELS.get(m, m))}</b>"]
            base_fmt = b["followed_format"].mean() if len(b) else 0
            for label, rows in [("none", b)] + [(fx, fixes[(fixes["model"] == m) & (fixes["fix"] == fx)])
                                                for fx in ("guard", "translate")]:
                if rows.empty:
                    cells.append("")
                    continue
                c, f_ = rows["passed_all"].mean(), rows["followed_format"].mean()
                colour = ui.T["pass"] if f_ >= 0.9 else (ui.T["accent"] if f_ >= 0.5 else ui.T["fail"])
                cells.append(f'{100 * c:.0f}% correct · <span style="color:{colour};font-weight:600">'
                             f'{100 * f_:.0f}% only code</span>')
                if label != "none":
                    gain = f_ - base_fmt
                    if best_gain is None or gain > best_gain[0]:
                        best_gain = (gain, label, m, base_fmt, f_)
            fix_rows.append(cells)
        ui.table(["Model (" + VERSIONS.get(fix_version, fix_version) + ")", "No fix", "Guard line", "Translate first"],
                 fix_rows)
        if best_gain and best_gain[0] > 0:
            g, label, m, before, after = best_gain
            ui.finding(f"Biggest improvement: the {'guard line' if label == 'guard' else 'translate-first'} fix took "
                       f"{MODELS.get(m, m)} from {100 * before:.0f}% to {100 * after:.0f}% replies with only code. "
                       "MixCheck can measure whether a fix really works, not just find the problem.")

    # ---- Model leaderboard ----
    ui.section("Model leaderboard", "All 10 ways of asking together. Weakest = the way of asking with the most failures.")
    board = []
    for m in models:
        rows = results[results["model"] == m]
        if rows.empty:
            continue
        per_v = rows.groupby("language").agg(c=("passed_all", "mean"), f=("followed_format", "mean"))
        weakest = (per_v["c"] + per_v["f"]).idxmin()
        board.append((rows["passed_all"].mean(), rows["followed_format"].mean(), m, weakest))
    board.sort(key=lambda b: (b[0] + b[1]), reverse=True)
    ui.table(["Model", "Correct code", "Replied with only code", "Weakest way of asking"],
             [[f'<b>{ui.esc(MODELS.get(m, m))}</b> <span style="color:{ui.T["faint"]}">{ui.esc(exact_model_id(m) or "")}</span>',
               f"{100 * c:.1f}%", f"{100 * f_:.1f}%", ui.esc(VERSIONS.get(w, w))] for c, f_, m, w in board])

    # ---- Downloads ----
    ui.section("Take the results with you", "The raw results table, and a short report a team could share.")
    d1, d2 = st.columns(2)
    with open(RESULTS_FILE, "rb") as fh:
        d1.download_button("Download results (CSV)", fh.read(), file_name="mixcheck_results.csv", mime="text/csv")
    d2.download_button("Download report (Markdown)", make_report(results, code_rows, fmt_rows, board),
                       file_name="mixcheck_report.md", mime="text/markdown")

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
    rng = random.Random(7)
    rng.shuffle(deck)
    deck = deck[:6]                      # 6 failures + 4 passes, so guessing "fails" every time doesn't win
    passes = results[results["passed_all"] & results["language"].str.contains("casual|devanagari")]
    picks = passes.sample(n=min(len(passes), 10 - len(deck)), random_state=7) if len(passes) else passes
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
        components.html(widgets.guess_game({"deck": deck[:10]}), height=780, scrolling=True)
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
            if not r.followed_format:
                with st.expander("This reply also ignored \"only code\": see the full reply"):
                    st.text(read_reply(r.model, r.task_id, r.language))

# ---------------------------------------------------------------
# Try it live
# ---------------------------------------------------------------
def run_one(model, prompt, task_id):
    """Ask the model and grade the answer.
    Returns (passed, total, error, code, followed_format) or raises."""
    from models import ask
    try:
        reply = ask(model, prompt)
    except Exception as e:
        if "tool_use_failed" in str(e):
            return 0, 1, "The model tried to call a tool instead of writing code.", "", False
        raise
    ok, n, error = grade(reply, os.path.join("tests", f"{task_id}.py"))
    return ok, n, error, strip_fences(reply), followed_format(reply)


with tab_live:
    mode = st.radio("Mode", ["Face-off: English vs mixed", "Test one prompt"], horizontal=True,
                    label_visibility="collapsed")
    task_labels = {tid: title_of(r["function_name"]) for tid, r in task_rows.items()}

    if mode.startswith("Face-off"):
        ui.section("English vs mixed, side by side",
                   "The same task in two languages, sent to the same model. Does the language change the result?")
        mixed_options = [v for v in VERSIONS if v in tasks.columns and not v.startswith("english")]
        c1, c2, c3 = st.columns(3)
        start_task = "task16" if "task16" in task_labels else list(task_labels)[dial_data(len(results))["start_task"]]
        task_id = c1.selectbox("Task", list(task_labels), format_func=task_labels.get, key="fo_task",
                               index=list(task_labels).index(start_task))
        mixed = c2.selectbox("Mixed version", mixed_options, format_func=VERSIONS.get,
                             index=mixed_options.index("kanglish_casual") if "kanglish_casual" in mixed_options else 0)
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
                            ui.verdict(res[0], res[1], res[2], res[4])
                            if res[3]:
                                st.code(res[3], language="python")
                    ui.faceoff_summary(VERSIONS[english_key], a[0] == a[1], VERSIONS[mixed], b[0] == b[1], a[4], b[4])
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
                        ok, n, error, code, fmt = run_one(model, prompt, task_id)
                    ui.verdict(ok, n, error, fmt)
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
        ("Run the code", "We test the code block that defines the function we asked for. It runs in a separate "
                         "process with a time limit, against the same test cases, including tricky ones like empty lists."),
        ("Two scores", "Correct code: did the function pass every test? Followed instructions: was the reply only "
                       "code, as every prompt asks? Compare each mixed version with the same task in English."),
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
