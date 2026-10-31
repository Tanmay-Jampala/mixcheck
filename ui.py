"""
ui.py - the MixCheck design system: colours, fonts and reusable pieces of the page.

app.py uses these helpers so the dashboard looks consistent everywhere.
The interactive widgets (Mix Dial, results grid, guessing game) live in widgets.py.
To change the look, edit TOKENS below; everything else follows.
"""

import html
import textwrap

import streamlit as st

# ---------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------
TOKENS = {
    # Surfaces (darkest to lightest)
    "bg": "#0E0B1F",          # page background: deep indigo night
    "surface": "#17132E",     # cards
    "surface_2": "#211B42",   # raised parts inside cards
    "border": "#2E2759",      # hairlines
    # Text
    "text": "#F2EFFF",
    "muted": "#A9A3CF",
    "faint": "#6F6A99",
    # Brand
    "brand": "#9B8CFF",       # AVISHKAR lavender
    "brand_deep": "#5B4FD6",
    "accent": "#FF9F1C",      # saffron: the one sharp accent
    # Status (only ever used for pass / fail, always with a word)
    "pass": "#2BD9A0",
    "fail": "#FF5C7A",
    # Type
    "font_display": "'Bricolage Grotesque', 'Segoe UI', sans-serif",
    "font_body": "'Instrument Sans', 'Segoe UI', sans-serif",
    "font_mono": "'JetBrains Mono', Consolas, monospace",
    "font_indic": "'Noto Sans Devanagari', 'Noto Sans Bengali', 'Nirmala UI', sans-serif",
    # Shape and motion
    "radius": "16px",
    "radius_sm": "10px",
    "ease": "cubic-bezier(.2,.8,.2,1)",
}
T = TOKENS

# Each language family has one colour, used for chips and bars everywhere
VERSION_COLOURS = {
    "english": "#9B8CFF", "english_casual": "#9B8CFF",
    "hinglish": "#FF9F1C", "hinglish_casual": "#FF9F1C", "hinglish_devanagari": "#FF9F1C",
    "benglish": "#4CC9F0", "benglish_casual": "#4CC9F0",
    "kanglish_casual": "#E87BA4",   # Kannada: pink
    "tanglish_casual": "#9EE493",   # Tamil: soft green
    "odia_casual": "#FFD166",       # Odia: gold
}

# A faint grain texture for the page background (an inline SVG, no download needed)
_GRAIN = (
    "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'>"
    "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/>"
    "<feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0'/></filter>"
    "<rect width='100%' height='100%' filter='url(%23n)'/></svg>\")"
)


def _html(markup):
    """Render raw HTML. Removes indentation and blank lines first, because
    Streamlit would otherwise show parts of the HTML as plain text."""
    lines = textwrap.dedent(markup).strip().splitlines()
    st.markdown("\n".join(line for line in lines if line.strip()), unsafe_allow_html=True)


def esc(text):
    return html.escape(str(text))


# ---------------------------------------------------------------
# Global styles
# ---------------------------------------------------------------
def inject_styles():
    _html(f"""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;600&family=Noto+Sans+Devanagari:wght@500&family=Noto+Sans+Bengali:wght@500&display=swap" rel="stylesheet">
    <style>
    :root {{
      --bg:{T['bg']}; --surface:{T['surface']}; --surface-2:{T['surface_2']}; --border:{T['border']};
      --text:{T['text']}; --muted:{T['muted']}; --faint:{T['faint']};
      --brand:{T['brand']}; --brand-deep:{T['brand_deep']}; --accent:{T['accent']};
      --pass:{T['pass']}; --fail:{T['fail']};
      --r:{T['radius']}; --r-sm:{T['radius_sm']}; --ease:{T['ease']};
    }}
    html, body, [data-testid="stAppViewContainer"] {{
      background:
        {_GRAIN},
        radial-gradient(1100px 520px at 88% -8%, rgba(91,79,214,.32), transparent 60%),
        radial-gradient(760px 420px at -12% 18%, rgba(255,159,28,.08), transparent 60%),
        radial-gradient(900px 600px at 50% 120%, rgba(76,201,240,.06), transparent 60%),
        var(--bg) !important;
      color: var(--text);
      font-family: {T['font_body']};
    }}
    [data-testid="stHeader"] {{ background: transparent; }}
    .block-container {{ padding-top: 1.6rem; max-width: 1260px; }}
    h1, h2, h3, h4 {{ font-family: {T['font_display']} !important; letter-spacing: -.01em; }}
    p, li, label, .stMarkdown {{ font-family: {T['font_body']}; }}
    iframe {{ border-radius: 26px; }}

    /* Tabs */
    [data-baseweb="tab-list"] {{ gap: .3rem; border-bottom: 1px solid var(--border); margin-top: .6rem; }}
    [data-baseweb="tab"] {{
      font-family: {T['font_display']}; font-size: 1.02rem; padding: .7rem 1.1rem;
      border-radius: 12px 12px 0 0; color: var(--muted);
      transition: color .2s var(--ease), background .2s var(--ease);
    }}
    [data-baseweb="tab"]:hover {{ color: var(--text); background: rgba(155,140,255,.08); }}
    [data-baseweb="tab"][aria-selected="true"] {{ color: var(--text); background: rgba(155,140,255,.10); }}
    [data-baseweb="tab-highlight"] {{ background: var(--accent) !important; height: 3px; box-shadow: 0 0 14px var(--accent); }}

    /* Buttons */
    .stButton > button {{
      font-family: {T['font_body']}; font-weight: 600;
      border-radius: 999px; padding: .7rem 1.5rem; border: 0;
      background: linear-gradient(135deg, var(--accent), #FF6B3D) !important; color: #1a0f00 !important;
      box-shadow: 0 8px 24px rgba(255,159,28,.25);
      transition: transform .15s var(--ease), box-shadow .15s var(--ease);
    }}
    .stButton > button:hover {{ transform: translateY(-2px); box-shadow: 0 12px 30px rgba(255,159,28,.35); }}
    .stButton > button:focus-visible {{ outline: 3px solid var(--brand); outline-offset: 3px; }}

    /* Inputs */
    [data-baseweb="select"] > div, .stTextArea textarea {{
      background: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: var(--r-sm) !important;
    }}
    .stTextArea textarea {{ font-family: {T['font_indic']}, {T['font_body']}; font-size: 1.02rem; line-height: 1.5; }}
    label, .stSelectbox label p, .stTextArea label p, .stRadio label p {{ color: var(--muted) !important; font-weight: 500; }}
    [data-testid="stCode"] {{ border-radius: var(--r-sm); border: 1px solid var(--border); }}
    code, pre {{ font-family: {T['font_mono']} !important; }}

    /* ---------- MixCheck components ---------- */
    .mc-section {{ margin: 2.2rem 0 .9rem; max-width: 72ch; }}
    .mc-section h3 {{ margin: 0; font-size: 1.6rem; font-weight: 800; }}
    .mc-section p {{ margin: .25rem 0 0; color: var(--muted); font-size: .98rem; }}

    .mc-chip {{ display:inline-flex; align-items:center; gap:.45rem; font-size:.85rem; font-weight:500;
      padding:.3rem .75rem; border-radius:999px; background:rgba(255,255,255,.04); border:1px solid var(--border); color:var(--text); }}
    .mc-chip i {{ width:.6rem; height:.6rem; border-radius:50%; display:inline-block; }}

    .mc-stats {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(210px,1fr)); gap:1rem; }}
    .mc-stat {{ position:relative; padding:1.2rem 1.3rem 1.1rem; border-radius:var(--r); overflow:hidden;
      background: linear-gradient(160deg, rgba(33,27,66,.9), rgba(23,19,46,.95)); border:1px solid var(--border); }}
    .mc-stat::after {{ content:""; position:absolute; right:-30px; top:-30px; width:110px; height:110px; border-radius:50%;
      background: radial-gradient(circle, var(--c), transparent 70%); opacity:.25; }}
    .mc-stat .v {{ font-family:{T['font_display']}; font-weight:800; font-size:2.5rem; line-height:1.05; color:var(--text); }}
    .mc-stat .l {{ color:var(--muted); font-size:.92rem; margin-top:.2rem; }}

    .mc-finding {{ margin-top:1rem; padding:1.15rem 1.3rem; border-radius:var(--r); display:flex; gap:1rem; align-items:flex-start;
      background: linear-gradient(90deg, rgba(255,159,28,.15), rgba(255,159,28,.02)); border:1px solid rgba(255,159,28,.35); }}
    .mc-finding .dot {{ width:12px; height:12px; border-radius:50%; background:var(--accent); box-shadow:0 0 14px var(--accent); margin-top:.45rem; flex:none; }}
    .mc-finding .k {{ color:var(--accent); font-weight:600; font-size:.9rem; }}
    .mc-finding .t {{ font-family:{T['font_display']}; font-size:1.3rem; margin-top:.15rem; color:var(--text); line-height:1.35; }}

    .mc-card {{ background:var(--surface); border:1px solid var(--border); border-radius:var(--r); padding:1rem 1.2rem; margin: 1.1rem 0 .5rem; }}
    .mc-card-head {{ display:flex; flex-wrap:wrap; align-items:center; gap:.5rem; }}
    .mc-pill {{ font-weight:600; font-size:.8rem; padding:.25rem .7rem; border-radius:999px; }}
    .mc-pill.pass {{ color:var(--pass); background:rgba(43,217,160,.15); }}
    .mc-pill.fail {{ color:var(--fail); background:rgba(255,92,122,.15); }}
    .mc-why {{ margin-top:.6rem; color:var(--muted); font-size:.92rem; }}
    .mc-why b {{ color: var(--text); font-weight:600; }}

    .mc-bubble {{ background:var(--surface-2); border:1px solid var(--border); border-radius:16px 16px 16px 4px;
      padding:.9rem 1rem; font-family:{T['font_indic']}, {T['font_body']}; font-size:1rem; line-height:1.55; color:var(--text); }}
    .mc-bubble-label {{ font-size:.85rem; color:var(--faint); margin:.2rem 0 .4rem; }}

    .mc-verdict {{ border-radius:var(--r); padding:1.1rem 1.3rem; margin:.8rem 0; border:1px solid; animation: mc-pop .45s var(--ease); }}
    .mc-verdict.pass {{ background: rgba(43,217,160,.08); border-color: rgba(43,217,160,.45); }}
    .mc-verdict.fail {{ background: rgba(255,92,122,.08); border-color: rgba(255,92,122,.45); }}
    .mc-verdict .big {{ font-family:{T['font_display']}; font-size:1.7rem; font-weight:800; }}
    .mc-verdict.pass .big {{ color: var(--pass); }} .mc-verdict.fail .big {{ color: var(--fail); }}
    .mc-meter {{ height:10px; border-radius:999px; background: var(--surface-2); overflow:hidden; margin-top:.7rem; }}
    .mc-meter > div {{ height:100%; border-radius:999px; animation: mc-grow .8s var(--ease); }}
    @keyframes mc-pop {{ from {{ opacity:0; transform:translateY(8px) scale(.98); }} to {{ opacity:1; transform:none; }} }}
    @keyframes mc-grow {{ from {{ width:0 !important; }} }}

    .mc-faceoff {{ margin:1.2rem 0 .4rem; padding:1.2rem 1.4rem; border-radius:var(--r);
      background: linear-gradient(120deg, rgba(91,79,214,.35), rgba(23,19,46,.9)); border:1px solid rgba(155,140,255,.4); }}
    .mc-faceoff .t {{ font-family:{T['font_display']}; font-size:1.45rem; font-weight:800; line-height:1.3; }}
    .mc-faceoff p {{ color:var(--muted); margin:.35rem 0 0; }}

    .mc-pipeline {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(190px,1fr)); gap:1rem; }}
    .mc-step {{ position:relative; background:var(--surface); border:1px solid var(--border); border-radius:var(--r); padding:1.2rem; }}
    .mc-step .n {{ width:2.3rem; height:2.3rem; border-radius:50%; display:grid; place-items:center; font-family:{T['font_display']}; font-weight:800;
      background: linear-gradient(135deg, var(--brand), var(--brand-deep)); color:#fff; margin-bottom:.7rem; box-shadow:0 0 0 4px rgba(155,140,255,.15); }}
    .mc-step h4 {{ margin:0 0 .35rem; font-size:1.12rem; color:var(--text); }}
    .mc-step p {{ margin:0; color:var(--muted); font-size:.92rem; line-height:1.5; }}

    .mc-footer {{ margin-top:3rem; padding-top:1.2rem; border-top:1px solid var(--border); color:var(--faint);
      font-size:.88rem; display:flex; flex-wrap:wrap; justify-content:space-between; gap:.6rem; }}
    .mc-footer b {{ color: var(--muted); font-weight:600; }}
    @media (prefers-reduced-motion: reduce) {{ .mc-verdict, .mc-meter > div {{ animation:none; }} }}
    </style>
    """)


# ---------------------------------------------------------------
# Components
# ---------------------------------------------------------------
def section(title, subtitle=""):
    sub = f"<p>{esc(subtitle)}</p>" if subtitle else ""
    _html(f'<div class="mc-section"><h3>{esc(title)}</h3>{sub}</div>')


def stats(items):
    """items: list of (value, label, colour)."""
    cards = "".join(
        f'<div class="mc-stat" style="--c:{c}"><div class="v">{esc(v)}</div><div class="l">{esc(l)}</div></div>'
        for v, l, c in items
    )
    _html(f'<div class="mc-stats">{cards}</div>')


def finding(text):
    _html(f'<div class="mc-finding"><span class="dot"></span><div><div class="k">What we found</div>'
          f'<div class="t">{esc(text)}</div></div></div>')


def chip(label, colour=None):
    dot = f'<i style="background:{colour}"></i>' if colour else ""
    return f'<span class="mc-chip">{dot}{esc(label)}</span>'


def version_chip(version, label):
    return chip(label, VERSION_COLOURS.get(version, T["brand"]))


def failure_card_head(task_label, version, version_label, model_label, passed, total, error):
    why = f'<div class="mc-why"><b>What went wrong:</b> {esc(error)}</div>' if error else ""
    _html(f"""
    <div class="mc-card">
      <div class="mc-card-head">
        <span class="mc-pill fail">Failed {passed} of {total} tests</span>
        {chip(task_label)}
        {version_chip(version, version_label)}
        {chip(model_label)}
      </div>
      {why}
    </div>
    """)


def bubble(label, text):
    _html(f'<div class="mc-bubble-label">{esc(label)}</div><div class="mc-bubble">{esc(text)}</div>')


def verdict(passed, total, error=None, followed=None):
    ok = total > 0 and passed == total
    kind = "pass" if ok else "fail"
    colour = T["pass"] if ok else T["fail"]
    width = 0 if total == 0 else 100 * passed / total
    why = f'<div class="mc-why"><b>What went wrong:</b> {esc(error)}</div>' if error else ""
    fmt = ""
    if followed is True:
        fmt = f'<div class="mc-why" style="color:{T["pass"]}"><b>Instructions:</b> replied with only the code, as asked</div>'
    elif followed is False:
        fmt = f'<div class="mc-why" style="color:{T["accent"]}"><b>Instructions:</b> ignored “only code” and added extra text</div>'
    _html(f"""
    <div class="mc-verdict {kind}">
      <div class="big">{"Passed" if ok else "Failed"}</div>
      <div class="mc-why">{passed} of {total} test cases passed</div>
      <div class="mc-meter"><div style="width:{width:.0f}%; background:{colour}"></div></div>
      {fmt}
      {why}
    </div>
    """)


def faceoff_summary(left_label, left_ok, right_label, right_ok, left_fmt=None, right_fmt=None):
    if left_ok and right_ok and left_fmt and right_fmt is False:
        title = f"Both wrote working code, but the {right_label} answer ignored “only code”."
        note = "This is our main finding: in mixed languages the code mostly still works, but the instructions break."
    elif left_ok and right_ok:
        title, note = "Both passed.", ("The AI handled the task in both languages this time. Most tasks pass: "
                                       "the gaps show up across 750 answers, not in every single run.")
    elif left_ok and not right_ok:
        title = f"{left_label} passed. {right_label} failed."
        note = "Same task, different language, different result: this is exactly the gap MixCheck measures."
    elif right_ok and not left_ok:
        title = f"{right_label} passed. {left_label} failed."
        note = ("The mixed prompt did better this time. One live run can go either way, "
                "which is why our results come from 750 graded answers, not one.")
    else:
        title, note = "Both failed.", "The task itself tripped the AI up, whatever the language."
    _html(f'<div class="mc-faceoff"><div class="t">{esc(title)}</div><p>{esc(note)}</p></div>')


def table(headers, rows, highlight=()):
    """A styled table. rows: lists of cells (cells may contain simple HTML we built ourselves).
    highlight: indexes of rows to mark with the accent colour."""
    head = "".join(f'<th style="text-align:{"left" if i == 0 else "right"};padding:.55rem .8rem;color:{T["faint"]};'
                   f'font-weight:600;font-size:.82rem;border-bottom:1px solid {T["border"]}">{esc(h)}</th>'
                   for i, h in enumerate(headers))
    body = ""
    for r_i, row in enumerate(rows):
        bg = "rgba(255,159,28,.08)" if r_i in highlight else "transparent"
        cells = "".join(f'<td style="text-align:{"left" if i == 0 else "right"};padding:.55rem .8rem;'
                        f'border-bottom:1px solid {T["border"]};color:{T["text"]}">{c}</td>'
                        for i, c in enumerate(row))
        body += f'<tr style="background:{bg}">{cells}</tr>'
    _html(f'<div style="overflow-x:auto;background:{T["surface"]};border:1px solid {T["border"]};border-radius:16px;'
          f'padding:.4rem .6rem;margin:.6rem 0 1rem"><table style="width:100%;border-collapse:collapse;'
          f'font-size:.92rem">{head and "<thead><tr>" + head + "</tr></thead>"}<tbody>{body}</tbody></table></div>')


def tag(text, kind):
    """Small coloured label: kind is 'pass', 'fail', 'warn' or 'muted'."""
    colour = {"pass": T["pass"], "fail": T["fail"], "warn": T["accent"], "muted": T["muted"]}[kind]
    return (f'<span style="color:{colour};border:1px solid {colour}55;background:{colour}14;border-radius:999px;'
            f'padding:.1rem .55rem;font-size:.8rem;font-weight:600;white-space:nowrap">{esc(text)}</span>')


def pipeline(steps):
    """steps: list of (title, description). Numbered because it's a real sequence."""
    cards = "".join(
        f'<div class="mc-step"><div class="n">{i}</div><h4>{esc(t)}</h4><p>{esc(d)}</p></div>'
        for i, (t, d) in enumerate(steps, start=1)
    )
    _html(f'<div class="mc-pipeline">{cards}</div>')


def footer():
    _html("""
    <div class="mc-footer">
      <span>MixCheck, built by <b>Team El Rata Alada</b>: Tanmay, Ritobroto, Aaditya and Aaliya</span>
      <span>AVISHKAR 2026, FET, Jain University</span>
    </div>
    """)
