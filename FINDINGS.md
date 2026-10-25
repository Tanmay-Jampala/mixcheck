# MixCheck findings (Oct 25, 2026)

**Setup:** 25 Python tasks × 10 prompt versions × 3 models = 750 graded replies.
Models: Gemini (`gemini-flash-lite-latest`), Groq big (`openai/gpt-oss-120b`), Groq small (`openai/gpt-oss-20b`). Temperature 0, one run each.
Every prompt asks for a named function and says "reply with only the code".

## Headline

> When the prompt is in English, the models get it right every time.
> When the same task is mixed with an Indian language, they still mostly write working code,
> but they **stop following instructions**: they rename the function, add long explanations, or reply in another script.
> The lower-resource the mix, the bigger the drop.

## The numbers

Correct code, leaving out task19 (its spec is ambiguous, and it fails in English too) and 3 API errors:

| Prompt version | Correct code |
|---|---|
| English (formal and casual) | **100%** |
| Hinglish (formal) | 100% |
| Hinglish in Hindi script | 98.6% |
| Benglish (formal) | 98.6% |
| Hinglish casual | 97.2% |
| Tanglish casual | 94.4% |
| Odia-English casual | 94.4% |
| Benglish casual | 93.1% |
| **Kanglish casual** | **90.3%** |

Replied with only the code, as asked:

- English: 98% of replies. Mixed: 90.8%.
- Groq big, Kanglish: **0 of 25**. Groq small, Kanglish: **1 of 25**.
- 10 of Groq big's 25 Kanglish replies were partly written in Kannada script, even though the prompts were in Roman letters. The median reply was about 2,000 characters with two code blocks, when we asked for code only.
- Gemini replied with only code 250 out of 250 times.

## The three kinds of failure

1. **Wrong function name (9 cases, all in mixed prompts, none in English).** The exact name was in every one of these prompts.
   - Groq small turned "bhai indian_format" into `def bhai_indian_format`: it took the slang word "bhai" as part of the name.
   - Gemini wrote `compress_string` (Tanglish), `merge` (Kanglish) and `calculate_running_balance` (Odia).
   - Groq small wrote `is_valid_mobile` (Odia).
   - In a real codebase, any other code that calls the function by its real name would break.
2. **Missed instruction details (comprehension).**
   - The case-insensitive palindrome rule was ignored in casual Benglish and Odia.
   - An extra parameter was added to `missing_number` in Kanglish.
3. **Ordinary coding bugs, not caused by the language. We count these honestly and do not blame the language for them.**
   - task19 `minutes_between` fails the "same time → 0" case in English too.
   - Groq big's `indian_format` crashed on 1000 in 4 mixed versions. It is a Python bug (`reversed(list) + list`) that it happened to avoid in English.

## Caveats (say these before a judge asks)

- The sample is small: 25 tasks and one run per prompt. The differences are a few tasks each, so they are signals, not proof.
- The Kanglish, Tanglish and Odia prompts were drafted with AI help and are still being checked by native speakers.
- The "only code" check is strict: one explanation sentence counts as a fail. That is deliberate, because a tool that pastes AI output straight into an editor would break.
