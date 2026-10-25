"""
app.py - the MixCheck dashboard.

Run:  streamlit run app.py
It opens in your browser. Tabs:
  Results       - how often each model's code passed, for every prompt version
  Failures      - every failed answer: the prompt, the AI's code and what went wrong
  Try it live   - type any prompt, pick a model, and test the code it writes
  How it works  - the method, for judges
"""

import os

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from grade import grade, strip_fences

RESULTS_FILE = "results/results.csv"
TASKS_FILE = "prompts/tasks.csv"

# Order and display names for every prompt version
VERSIONS = {
    "english": "English",
    "hinglish": "Hinglish",
    "benglish": "Benglish",
    "english_casual": "English (casual)",
    "hinglish_casual": "Hinglish (casual)",
    "benglish_casual": "Benglish (casual)",
    "hinglish_devanagari": "Hinglish (Hindi script)",
}
MODELS = {
    "gemini": "Gemini",
    "groq": "Groq, big model",
    "groq-small": "Groq, small model",
}

st.set_page_config(page_title="MixCheck", layout="wide")


# ---------------------------------------------------------------
# Load the data
# ---------------------------------------------------------------
@st.cache_data
def load_results():
    df = pd.read_csv(RESULTS_FILE, keep_default_na=False)
    df["passed_all"] = df["passed_all"].astype(str).str.lower() == "true"
    return df


@st.cache_data
def load_tasks():
    return pd.read_csv(TASKS_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def model_label(model):
    """'Groq, small model (openai/gpt-oss-20b)' - the exact model ID if we saved it."""
    label = MODELS.get(model, model)
    saved = os.path.join("generated", model, "model_id.txt")
    if os.path.exists(saved):
        with open(saved, encoding="utf-8") as f:
            label += f" ({f.read().strip()})"
    return label


results = load_results()
tasks = load_tasks()
models = [m for m in MODELS if m in set(results["model"])]
models += sorted(set(results["model"]) - set(models))
versions = [v for v in VERSIONS if v in set(results["language"])]

st.title("MixCheck")
st.markdown(
    "**Do AI coding assistants write worse code when you ask in a mixed Indian language?** "
    "Every coding task is asked in English, Hinglish and Benglish, in clean and casual styles. "
    "The code each AI writes is run against the same test cases."
)

tab_results, tab_failures, tab_live, tab_how = st.tabs(
    ["Results", "Failures", "Try it live", "How it works"]
)

# ---------------------------------------------------------------
# Tab 1: Results
# ---------------------------------------------------------------
with tab_results:
    total = len(results)
    passed = int(results["passed_all"].sum())
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("AI answers graded", f"{total}")
    c2.metric("Passed every test", f"{100 * passed / total:.1f}%")
    c3.metric("Failed answers", f"{total - passed}")
    c4.metric("Models x prompt versions", f"{len(models)} x {len(versions)}")

    st.subheader("Where the models fail")
    st.caption(
        "Each cell is one model on one prompt version, across all tasks. "
        "Darker means more failed tasks. White cells passed everything."
    )

    table = (
        results.groupby(["model", "language"])["passed_all"]
        .agg(["sum", "count"])
        .reset_index()
    )
    z, text, hover = [], [], []
    for m in models:
        z_row, text_row, hover_row = [], [], []
        for v in versions:
            row = table[(table["model"] == m) & (table["language"] == v)]
            if row.empty:
                z_row.append(None)
                text_row.append("")
                hover_row.append("not run")
                continue
            ok, n = int(row["sum"].iloc[0]), int(row["count"].iloc[0])
            fail_rate = 100 * (n - ok) / n
            z_row.append(fail_rate)
            text_row.append(f"{100 * ok / n:.0f}%<br>{ok}/{n}")
            hover_row.append(
                f"{model_label(m)}<br>{VERSIONS.get(v, v)}<br>"
                f"{ok} of {n} tasks passed, {n - ok} failed"
            )
        z.append(z_row)
        text.append(text_row)
        hover.append(hover_row)

    fig = go.Figure(
        go.Heatmap(
            z=z,
            x=[VERSIONS.get(v, v) for v in versions],
            y=[MODELS.get(m, m) for m in models],
            text=text,
            texttemplate="%{text}",
            textfont={"size": 14, "color": "#0b0b0b"},
            customdata=hover,
            hovertemplate="%{customdata}<extra></extra>",
            colorscale=[[0, "#ffffff"], [1, "#2a78d6"]],
            zmin=0,
            zmax=40,
            xgap=2,
            ygap=2,
            colorbar={"title": "Failed %", "ticksuffix": "%"},
        )
    )
    fig.update_layout(
        height=120 + 80 * len(models),
        margin={"l": 10, "r": 10, "t": 10, "b": 10},
        yaxis={"autorange": "reversed"},
        xaxis={"side": "top"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Pass rate table")
    pivot = (
        results.assign(passed_pct=results["passed_all"] * 100)
        .pivot_table(index="model", columns="language", values="passed_pct", aggfunc="mean")
        .reindex(index=models, columns=versions)
        .round(1)
    )
    pivot.index = [model_label(m) for m in pivot.index]
    pivot.columns = [VERSIONS.get(v, v) for v in pivot.columns]
    st.dataframe(pivot.style.format("{:.1f}%"), use_container_width=True)

# ---------------------------------------------------------------
# Tab 2: Failures
# ---------------------------------------------------------------
with tab_failures:
    failures = results[~results["passed_all"]].copy()
    st.subheader(f"Every failed answer ({len(failures)})")
    if failures.empty:
        st.info("No failures yet.")
    else:
        prompts_by_task = tasks.set_index("task_id")
        for _, row in failures.iterrows():
            title = (
                f"{row['task_id']} · {VERSIONS.get(row['language'], row['language'])} · "
                f"{MODELS.get(row['model'], row['model'])} · "
                f"{row['passed_cases']}/{row['total_cases']} test cases passed"
            )
            with st.expander(title):
                if row["task_id"] in prompts_by_task.index and row["language"] in tasks.columns:
                    st.markdown("**The prompt**")
                    st.write(prompts_by_task.loc[row["task_id"], row["language"]])
                if row["error"]:
                    st.markdown(f"**What went wrong:** {row['error']}")
                code_path = os.path.join(
                    "generated", row["model"], f"{row['task_id']}_{row['language']}.py"
                )
                if os.path.exists(code_path):
                    with open(code_path, encoding="utf-8") as f:
                        st.markdown("**The AI's code**")
                        st.code(strip_fences(f.read()), language="python")

# ---------------------------------------------------------------
# Tab 3: Try it live
# ---------------------------------------------------------------
with tab_live:
    st.subheader("Test any prompt yourself")
    st.caption("Pick a task, edit the prompt however you like, and see if the AI's code passes.")

    task_labels = {
        r["task_id"]: f"{r['task_id']}: {r['function_name']}" for _, r in tasks.iterrows()
    }
    col_a, col_b, col_c = st.columns(3)
    task_id = col_a.selectbox("Task", list(task_labels), format_func=task_labels.get)
    start_from = col_b.selectbox(
        "Start from this version",
        [v for v in VERSIONS if v in tasks.columns],
        index=list(VERSIONS).index("hinglish_casual") if "hinglish_casual" in tasks.columns else 0,
        format_func=VERSIONS.get,
    )
    live_model = col_c.selectbox("Model", list(MODELS), format_func=MODELS.get)

    task_row = tasks[tasks["task_id"] == task_id].iloc[0]
    prompt = st.text_area(
        "Prompt", value=task_row[start_from], height=120, key=f"prompt_{task_id}_{start_from}"
    )
    function_name = task_row["function_name"]

    if st.button("Ask the AI and test its code", type="primary"):
        if function_name not in prompt:
            st.warning(f"Keep the function name **{function_name}** in the prompt, "
                       "so the tests can find the function.")
        else:
            try:
                from models import ask
                with st.spinner("Asking the AI..."):
                    reply = ask(live_model, prompt)
                with st.spinner("Running the test cases..."):
                    ok, n, error = grade(reply, os.path.join("tests", f"{task_id}.py"))
                if ok == n:
                    st.success(f"PASSED: {ok} of {n} test cases")
                else:
                    st.error(f"FAILED: {ok} of {n} test cases passed")
                if error:
                    st.markdown(f"**What went wrong:** {error}")
                st.markdown("**The AI's code**")
                st.code(strip_fences(reply), language="python")
            except Exception as e:
                message = str(e)
                if "tool_use_failed" in message:
                    st.error("FAILED: the model tried to call a tool instead of writing code.")
                else:
                    st.error(f"Couldn't reach the model: {type(e).__name__}: {message[:200]}")
                    st.caption("Check the internet connection and the API keys in .env.")

# ---------------------------------------------------------------
# Tab 4: How it works
# ---------------------------------------------------------------
with tab_how:
    st.subheader("How MixCheck works")
    st.markdown(
        f"""
1. **Paired prompts.** Each of the {len(tasks)} coding tasks is written in {len(versions)} versions:
   clean English, Hinglish and Benglish; casual versions of all three, the way students really type;
   and Hinglish in Hindi script. Every version asks for the same function, so only the language changes.
2. **Native-speaker checks.** Hinglish is checked by Hindi speakers on our team, and Benglish by a Bengali speaker.
3. **Ask the models.** Every prompt goes to {len(models)} AI models with temperature 0,
   so the answers are repeatable.
4. **Grade by running the code.** The code each model writes runs in a separate process,
   with a time limit, against the same test cases, including tricky ones like empty lists.
   An answer passes only if every test case passes. No opinions, no hand-marking.
5. **Compare.** If a model passes in English but fails in a mixed version of the same task,
   the language caused the failure.
"""
    )
    st.markdown("**Models tested**")
    for m in models:
        st.markdown(f"- {model_label(m)}")
