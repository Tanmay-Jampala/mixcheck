# MixCheck design system

The dashboard's look lives in `ui.py` (styles and simple components) and `widgets.py` (the interactive parts). Change a token in `ui.py` and both follow.

## Concept

A live test bench that makes code-mixing *visible*. The one bold element is the **Mix Dial** in the hero: drag it and the same coding prompt slides from English to casual Hinglish, Hindi script and Benglish. Every word is coloured by its language, a meter shows how mixed the prompt is, and three lights show which AI models passed that exact prompt. Everything else stays calm so the dial is what people remember.

## Tokens

| Token | Value | Use |
| --- | --- | --- |
| `bg` | `#0E0B1F` | Page background (with a faint grain texture and three soft glows layered on top) |
| `surface` / `surface_2` | `#17132E` / `#211B42` | Cards, and raised parts inside them |
| `border` | `#2E2759` | Hairlines |
| `text` / `muted` / `faint` | `#F2EFFF` / `#A9A3CF` / `#6F6A99` | Text, from most to least important |
| `brand` | `#9B8CFF` | AVISHKAR lavender: English words, step numbers |
| `accent` | `#FF9F1C` | Saffron: main buttons, dial thumb, key finding, Hindi words |
| sky | `#4CC9F0` | Bengali words |
| `pass` / `fail` | `#2BD9A0` / `#FF5C7A` | Only for pass and fail, always with the word next to it |

**Type:** Bricolage Grotesque for headings (a hand-made, signboard feel), Instrument Sans for body text, JetBrains Mono only for real code, and Noto Sans Devanagari and Bengali for Indian scripts. Without internet, these fall back to Segoe UI, Consolas and Nirmala UI, which come with Windows.

**The wordmark** is layered type: white letters with a saffron and an indigo shadow stacked behind them.

**Language colours in prompts:** Hindi words get a saffron highlight and Bengali words a sky-blue one. English words stay plain with a thin lavender underline, so the mixing stands out as the dial moves. Names and numbers are set in monospace. The colouring uses a word list built from our own prompts (`mixtag.py`), so the mix percentage is an approximate guide.

**Motion:** one orchestrated moment, where the words of the prompt fade in one after another when the dial moves. Everything else moves only when someone clicks: the heatmap drawer slides in, the game's verdict pops, and meters fill. The drifting letters behind the hero are very faint. All motion stops if the viewer's computer is set to reduce motion.

## Interactive widgets (`widgets.py`)

| Widget | What it does |
| --- | --- |
| `mix_dial(data)` | The hero. Task dropdown, coloured prompt, mix meter, the dial (a real slider, so the arrow keys work), "Play all versions" for presenting, and pass/fail lights per model |
| `heat_grid(data)` | Results grid. Red cells had failures. Clicking a cell slides open a panel with every failed answer behind it: the prompt, the code and what went wrong |
| `guess_game(deck)` | "Guess the verdict." Shows a prompt and the AI's code; the player guesses pass or fail, sees the real result, and gets a score at the end |

## Simple components (`ui.py`)

`section`, `stats`, `finding`, `chip`, `failure_card_head`, `bubble`, `verdict` (the big Passed/Failed with a test meter), `faceoff_summary` (the English vs mixed result banner), `pipeline` (numbered, because it is a real sequence), `footer`.

## Rules

1. Colours only come from `TOKENS`. No new hex codes in `dashboard.py`.
2. Pass and fail colours never appear without the words "Passed" or "Failed".
3. No all-caps labels, and no "01 / 02" numbering unless the content really is a sequence.
4. HTML in Streamlit always goes through `ui._html()`, which strips indentation and blank lines so it renders properly.
5. Every widget works with the keyboard and keeps a visible focus ring.
