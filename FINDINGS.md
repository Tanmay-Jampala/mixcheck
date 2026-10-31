# MixCheck findings (Oct 31, 2026)

**Setup:** 25 Python tasks × 10 prompt versions × 3 models = 750 graded answers.
Models: Gemini (`gemini-flash-lite-latest`), Groq big (`openai/gpt-oss-120b`), Groq small (`openai/gpt-oss-20b`). Temperature 0, one run each.
Every prompt names the function to write and says "reply with only the code".
All numbers count every answer; nothing is left out. They match the dashboard.
The Kanglish prompts were reviewed by a native Kannada speaker (Takshak P) on Oct 31 and re-run (see `prompts/kanglish_review.md`).

## Headline

> In every language, the AI writes working code most of the time (93–97% in the casual versions). After a native speaker fixed our Kanglish wording, Kanglish code was as correct as English.
> What breaks is following instructions. Kanglish answers replied with only the code **35%** of the time; casual English answers did it **100%** of the time (p < 0.001).
> **One fixed English line fixes it.** Adding "Reply with only one Python code block and nothing else. Name the function exactly …" took both GPT-OSS models from 0% / 4% to **100%**, with no loss in correct code.

## The numbers

Same casual style, only the language changes (3 models × 25 tasks each):

| Casual version | Correct code | Followed "only code" |
|---|---|---|
| English | 97.3% | 100% |
| Hinglish | 96.0% | 93.3% |
| Benglish | 93.3% | 100% |
| Tanglish | 94.7% | 98.7% |
| Odia-English | 94.7% | 100% |
| **Kanglish** | 97.3% | **34.7%** |

- Overall: 96.0% of the 750 answers had correct code, and 92.3% replied with only code.
- **Is it real?** Fisher's exact test against English in the same style:
  - The Kanglish "only code" gap is real: p ≈ 2 × 10⁻²⁰. It passes even a strict Bonferroni cut-off (p < 0.003).
  - None of the correct-code differences are significant (smallest p = 0.44).
- In Kanglish, Groq big replied with only code in **0 of 25** prompts, and Groq small in **1 of 25**. Gemini did it every time, in all 250 answers.
- In the original run, 10 of Groq big's 25 Kanglish answers were partly written in Kannada script, even though the prompts were in Roman letters.

## Can it be fixed? (`fix_experiment.py`, Kanglish prompts)

| Model | No fix | Guard line | Translate first |
|---|---|---|---|
| Groq big (GPT-OSS 120B) | 24/25 correct · 0/25 only code | 24/25 · **25/25** | 25/25 · 0/25 |
| Groq small (GPT-OSS 20B) | 25/25 correct · 1/25 only code | 25/25 · **25/25** | 21/25 · 2/25 |

- **Guard line works completely:** every answer replied with only code, and correctness didn't change.
- **Translating first does not work.** The model's own translation loses the instruction: "bari code kodu" ("give only code") became "Provide the code". It also cost Groq small 4 correct answers.

## The three kinds of failure

1. **Wrong function name.**
   - This happened in 7 of 600 mixed prompts and 0 of 150 English prompts. The exact name was written in every prompt.
   - Groq small turned "bhai indian_format naam er python fn bana" into `def bhai_indian_format`. It read the slang word "bhai" as part of the name.
2. **Missed instruction details.**
   - The case-insensitive palindrome rule was ignored in casual Benglish (both Groq models) and Odia.
3. **Mistakes that also happen in English.**
   - task19 `minutes_between` says the end time is on the next day only when it is *earlier* than the start. Some answers returned 1,440 for equal times, including in English.
   - Groq big's `indian_format` crashed on 1000 in several mixed versions. It is a plain Python bug (`reversed(list) + list`).
   - Groq small made 3 API errors on English prompts. These count as fails, which is why English isn't 100%.

## Caveats

- The sample is small: 25 tasks and one run per prompt. The correctness gaps are signals only. The instruction gap is large and significant.
- The Kanglish prompts are now native-reviewed, and the team wrote Hinglish and Benglish. Tanglish and Odia were drafted with AI help and still need a check by a native speaker (Tanmay speaks Tamil, Aaliya speaks Odia).
- Re-running the Kanglish prompts changed its correct-code score from 90.7% to 97.3%. Better wording mattered for correctness, but not for following "only code".
- The "only code" check is strict on purpose: one sentence of explanation counts as a fail.
