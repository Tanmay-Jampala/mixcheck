# Kanglish native-speaker review

- **Reviewer:** Takshak P (native Kannada speaker), at AVISHKAR, Oct 31, 2026
- **Prompts checked:** tasks 1, 4, 9, 15, 16, 17, 18, 20, 22 and 24

## What he suggested

1. **Remove "guru"** from the start of tasks 1, 4, 9, 15, 16, 18, 20, 22 and 24. Read that way it sounds like a taunt.
2. **No capital letters in the middle of words.** We had written sounds like `ondE`, `eraDu`, `heLu` and `tagoLLi` with capitals. People don't type like that.
3. **Tasks 15 and 17:** `irbahudu` → `irabahudu`
4. **Task 17:** `saryaagi` → `sariyagi`

## Exact changes

| Before | After | Tasks |
|---|---|---|
| `guru …` at the start | (removed) | 1, 4, 9, 15, 16, 18, 20, 22, 24 |
| `ondE` | `onde` | 4, 12, 18, 20 |
| `eraDu`, `eraDne`, `eraDralli` | `eradu`, `eradne`, `eradralli` | 8, 14, 19, 24 |
| `heLu` | `helu` | 9 |
| `tagoLLi` | `tagolli` | 10, 18, 22 |
| `uLibeku` | `ulibeku` | 17 |
| `irbahudu` | `irabahudu` | 15, 17 |
| `saryaagi` | `sariyagi` | 17 |

Code words stay exactly as they are (`True`, `False`, `None`, `"HH:MM"`, `"A"`, function names), because the tests depend on them.

## Status

- The results in the dashboard and the deck come from the **original** prompts.
- To apply these fixes and re-run only the changed Kanglish prompts, run `python apply_kanglish_review.py`. It backs up the old prompts and replies first.
- One caveat when comparing old and new runs: `gemini-flash-lite-latest` is an alias, so Google may have moved it to a newer model since our first run.
