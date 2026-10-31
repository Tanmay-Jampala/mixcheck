# MixCheck

![tests](https://github.com/Tanmay-Jampala/mixcheck/actions/workflows/tests.yml/badge.svg)

**Same coding task. Different language. Does the AI still get it right?**

MixCheck tests AI coding assistants on prompts written the way many Indians actually type: mixing English with Hindi, Bengali, Kannada, Tamil or Odia. Every task is asked in English and in mixed versions. The code each AI writes is run against test cases, and we give it two scores:

1. **Correct code**: did the function pass every test?
2. **Followed instructions**: every prompt says "reply with only the code". Did it?

Team **El Rata Alada** (Tanmay, Ritobroto, Aaditya, Aaliya) · AVISHKAR 2026, FET, Jain University · AI & IoT track · Problem statement: Cross-lingual code-switching robustness tester.

## What we tested

- **25 Python tasks**, from reversing a string to merging intervals and Indian-style number formatting.
- **10 versions of every task**: English, English casual, Hinglish, Hinglish casual, Hinglish in Hindi script, Benglish, Benglish casual, Kanglish casual, Tanglish casual and Odia-English casual.
- **3 models**: Gemini (`gemini-flash-lite-latest`), GPT-OSS 120B and GPT-OSS 20B (through Groq). Temperature 0, one run each.
- **750 answers**, every one graded by actually running the code.

## What we found

| Casual version | Correct code | Replied with only code |
|---|---|---|
| English | 97.3% | 100% |
| Hinglish | 96.0% | 93.3% |
| Benglish | 93.3% | 100% |
| Tanglish | 94.7% | 98.7% |
| Odia-English | 94.7% | 100% |
| **Kanglish** | **90.7%** | **34.7%** |

- The code mostly still works in every language. **What breaks is following instructions.**
- GPT-OSS 120B replied with only code in **0 of 25** Kanglish prompts. 10 of those answers were partly written in Kannada script.
- The AI **renamed the function** in 9 of 600 mixed prompts and 0 of 150 English ones. One answer to a casual Benglish prompt was named `bhai_indian_format`: the model read "bhai" (bro) as part of the name.

Full details and limitations: [FINDINGS.md](FINDINGS.md).

## Run it

You need Python 3.14 and free API keys from Google AI Studio (Gemini) and Groq.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

Make a file called `.env` in this folder (it is ignored by git, never commit it):

```
GEMINI_API_KEY=your-key-here
GROQ_API_KEY=your-key-here
```

Then:

```bash
python check_keys.py                  # checks both keys work
streamlit run app.py                  # opens the dashboard at http://localhost:8501
```

The saved answers and results are already in the repo, so the dashboard works without running the models again. To redo everything:

```bash
python run_all.py --model gemini      # sends every prompt, saves replies to generated/
python run_all.py --model groq
python run_all.py --model groq-small
python grade_all.py                   # runs every reply against tests/, writes results/results.csv
python fix_experiment.py              # tests two fixes on the Kanglish prompts, writes results/fixes.csv
```

Run the automated checks (GitHub also runs them on every push, on Linux and Windows):

```bash
pip install pytest
python -m pytest checks -q
```

## How it works

| File | What it does |
|---|---|
| `prompts/tasks.csv` | 25 tasks × 10 prompt versions |
| `tests/task01.py` … `task25.py` | The function name and test cases for each task |
| `run_all.py` | Sends every prompt to a model and saves the reply |
| `grade.py` | Finds the requested function in a reply, runs it in a sandboxed separate process with a 10-second limit, and checks the "only code" rule |
| `stats.py` | 95% confidence ranges and Fisher's exact test: which gaps are real and which could be chance |
| `fix_experiment.py` | Tests two fixes on the Kanglish prompts: a fixed English guard line, and translating to English first |
| `checks/` | Automated tests: the grader, the sandbox, the statistics, and a reference solution that must pass every test file |
| `grade_all.py` | Grades every saved reply and writes `results/results.csv` |
| `mixtag.py` | Tags each word of a prompt by language for the Mix Dial |
| `app.py`, `ui.py`, `widgets.py` | The Streamlit dashboard: Mix Dial, results grid, Guess the verdict game, every failure, and a live face-off |
| `models.py` | Asks a model live, for the face-off |
| `deck/` | Presentation slides |

## How the grader keeps untrusted code contained

The code an AI writes is untrusted, so `grade.py` runs it with five layers of protection:

1. **A separate process with a 10-second limit**, so a crash or an endless loop can't affect the app.
2. **A clean environment.** Python's isolated mode is used, and no API keys are passed in.
3. **A Python audit hook** that blocks network access, running other programs, deleting or writing files, `ctypes`, and reading files outside Python itself.
4. **A 1 GB memory limit** on Linux, which is what Streamlit Cloud runs on.
5. **A secret code, different every run, on the result line**, so printing a fake "passed" line doesn't work.

This is strong isolation for a benchmark. A public service taking anyone's code would add an OS-level container (for example Docker with gVisor) on top.

## Limits we know about

- The sample is small: 25 tasks with one run each. Gaps of a few tasks are signals, not proof. The Kanglish instruction gap (35% vs 100%) is large.
- Our team wrote the Hinglish and Benglish prompts. The other mixes were drafted with AI help and are being checked by native speakers.
- The "only code" check is strict on purpose: tools that paste AI output straight into code break on extra text.
