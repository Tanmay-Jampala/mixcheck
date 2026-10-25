# MixCheck findings (Oct 25, 2026)

**Setup:** 25 Python tasks × 10 prompt versions × 3 models = 750 graded answers.
Models: Gemini (`gemini-flash-lite-latest`), Groq big (`openai/gpt-oss-120b`), Groq small (`openai/gpt-oss-20b`). Temperature 0, one run each.
Every prompt names the function to write and says "reply with only the code".
All numbers below count every answer; nothing is left out. They match the dashboard.

## Headline

> In every language, the AI still writes working code most of the time: 91–97% in the casual versions, with Kanglish lowest.
> What breaks is following instructions. Kanglish answers replied with only the code **35%** of the time; casual English answers did it **100%** of the time.
> Only mixed prompts made the AI rename the function: 9 of 600 mixed prompts, against 0 of 150 English ones.

## The numbers

| Prompt group | Correct code | Followed "only code" |
|---|---|---|
| English (formal and casual) | 96.0% | 98.0% |
| Hindi and Bengali mixes (5 versions) | 96.3% | 98.7% |
| Kannada, Tamil and Odia mixes (3 versions) | **93.3%** | **77.8%** |

Fairest comparison: same casual style, only the language changes.

| Casual version | Correct code | Followed "only code" |
|---|---|---|
| English | 97.3% | 100% |
| Hinglish | 96.0% | 93.3% |
| Benglish | 93.3% | 100% |
| Tanglish | 94.7% | 98.7% |
| Odia-English | 94.7% | 100% |
| **Kanglish** | **90.7%** | **34.7%** |

- Groq big followed "only code" in **0 of 25** Kanglish prompts, and Groq small in 1 of 25.
- 10 of Groq big's 25 Kanglish answers were partly written in Kannada script, even though the prompts were in Roman letters.
- Gemini replied with only code all 250 times.

## The three kinds of failure

1. **Wrong function name.**
   - This happened in 9 of 600 mixed prompts and 0 of 150 English prompts. The exact name was written in every prompt.
   - Groq small turned "bhai indian_format naam er python fn bana" into `def bhai_indian_format`. It read the slang word "bhai" as part of the name.
   - Gemini wrote `compress_string` (Tanglish), `merge` (Kanglish) and `calculate_running_balance` (Odia). Groq small wrote `is_valid_mobile` (Odia).
2. **Missed instruction details.**
   - The case-insensitive palindrome rule was ignored in casual Benglish and Odia.
   - An extra parameter was added to `missing_number` in Kanglish.
3. **Mistakes that also happen in English.**
   - task19 `minutes_between` says the end time is on the next day only when it is *earlier* than the start. 9 answers still returned 1,440 for equal times, including Gemini's English answers. This is an edge case that is hard in every language.
   - Groq big's `indian_format` crashed on 1000 in 4 mixed versions. It is a plain Python bug (`reversed(list) + list`).
   - Groq small made 3 API errors on English prompts: it tried to call a tool instead of answering. These count as fails, which is why English isn't 100%.

## Caveats (say these before a judge asks)

- The sample is small: 25 tasks and one run per prompt. The correctness gaps are a few tasks each, so treat them as signals. The instruction-following gap for Kanglish (35% vs 100%) is large.
- The Kanglish, Tanglish and Odia prompts were drafted with AI help and are being checked by native speakers.
- The "only code" check is strict on purpose: one sentence of explanation counts as a fail. A tool that pastes AI output straight into an editor would break.
