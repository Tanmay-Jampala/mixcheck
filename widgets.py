"""
widgets.py - the interactive parts of the dashboard, built in HTML + JavaScript.

Each function returns a complete little web page that app.py shows with
streamlit.components.v1.html(). The data goes in as JSON, so nothing here
talks to the internet except the fonts.

    mix_dial(data)    the hero: drag a dial to rewrite one prompt in another language
    heat_grid(data)   the results grid: click a cell to open the answers behind it
    guess_game(deck)  "Guess the verdict": does the AI's code pass or fail?
"""

import json

from ui import T

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800'
    '&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;600'
    '&family=Noto+Sans+Devanagari:wght@500&family=Noto+Sans+Bengali:wght@500&display=swap" rel="stylesheet">'
)

BASE_CSS = f"""
:root {{
  --bg:{T['bg']}; --surface:{T['surface']}; --surface-2:{T['surface_2']}; --border:{T['border']};
  --text:{T['text']}; --muted:{T['muted']}; --faint:{T['faint']};
  --brand:{T['brand']}; --brand-deep:{T['brand_deep']}; --accent:{T['accent']}; --sky:#4CC9F0;
  --pass:{T['pass']}; --fail:{T['fail']};
  --display:'Bricolage Grotesque','Segoe UI',sans-serif;
  --body:'Instrument Sans','Segoe UI',sans-serif;
  --mono:'JetBrains Mono',Consolas,monospace;
  --indic:'Noto Sans Devanagari','Noto Sans Bengali','Nirmala UI',sans-serif;
  --ease:cubic-bezier(.2,.8,.2,1);
}}
* {{ box-sizing:border-box; }}
html, body {{ margin:0; background:transparent; color:var(--text); font-family:var(--body); }}
button, select, input {{ font:inherit; color:inherit; }}
button {{ cursor:pointer; }}
:focus-visible {{ outline:3px solid var(--accent); outline-offset:3px; border-radius:8px; }}
.glass {{
  background:linear-gradient(160deg, rgba(33,27,66,.82), rgba(23,19,46,.92));
  border:1px solid rgba(155,140,255,.28); border-radius:20px;
  box-shadow:0 1px 0 rgba(255,255,255,.06) inset, 0 24px 60px rgba(5,2,25,.55);
  backdrop-filter:blur(10px);
}}
/* words coloured by language: a soft highlighter behind normal text */
.w {{ display:inline-block; padding:.05em .28em; margin:.12em .06em; border-radius:6px; line-height:1.35; }}
.w.en {{ background:none; box-shadow: inset 0 -2px 0 rgba(155,140,255,.45); border-radius:0; padding-left:.05em; padding-right:.05em; }}
.w.hi {{ background:rgba(255,159,28,.24); }}
.w.bn {{ background:rgba(76,201,240,.22); }}
.w.kn {{ background:rgba(232,123,164,.26); }}
.w.ta {{ background:rgba(158,228,147,.22); }}
.w.or {{ background:rgba(255,209,102,.24); }}
.w.code {{ font-family:var(--mono); font-size:.88em; color:var(--muted); background:rgba(255,255,255,.05); }}
.key {{ display:inline-flex; align-items:center; gap:.4rem; color:var(--muted); font-size:.85rem; margin-right:1rem; }}
.key i {{ width:.8rem; height:.8rem; border-radius:3px; display:inline-block; }}
.pill {{ display:inline-flex; align-items:center; gap:.35rem; font-weight:600; font-size:.8rem; padding:.2rem .6rem; border-radius:999px; }}
.pill.pass {{ background:rgba(43,217,160,.16); color:var(--pass); }}
.pill.fail {{ background:rgba(255,92,122,.16); color:var(--fail); }}
pre.code {{ margin:0; padding:.9rem 1rem; border-radius:12px; background:#0B0919; border:1px solid var(--border);
  font-family:var(--mono); font-size:.82rem; line-height:1.55; color:#E6E1FF; overflow:auto; white-space:pre; }}
pre.code .k {{ color:#C792EA; }} pre.code .s {{ color:#FFCB6B; }} pre.code .c {{ color:#7E78A8; font-style:italic; }}
.indic {{ font-family:var(--indic), var(--body); }}
@media (prefers-reduced-motion: reduce) {{ * {{ animation:none !important; transition:none !important; }} }}
"""

SHARED_JS = r"""
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function highlight(code){
  const re = /(#.*$)|("(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')|\b(def|return|if|elif|else|for|while|in|not|and|or|import|from|None|True|False|lambda|is|class|with|as|try|except|raise|yield)\b/gm;
  return esc(code).replace(re, (m, c, s, k) => c ? `<span class="c">${c}</span>` : s ? `<span class="s">${s}</span>` : `<span class="k">${k}</span>`);
}
function wordsHtml(words){
  return words.map(([t, g], i) => `<span class="w ${g}" style="--i:${i}">${esc(t)}</span>`).join(' ');
}
"""


def _page(css, body, script, data):
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return (
        f"<!doctype html><html><head><meta charset='utf-8'>{FONTS}"
        f"<style>{BASE_CSS}{css}</style></head><body>{body}"
        f"<script>const DATA = {payload};{SHARED_JS}{script}</script></body></html>"
    )


# ---------------------------------------------------------------
# 1. The Mix Dial (hero)
# ---------------------------------------------------------------
def mix_dial(data):
    css = """
    .hero { position:relative; overflow:hidden; border-radius:26px; padding:2.2rem 2.2rem 2.2rem;
      background:
        radial-gradient(700px 360px at 92% 8%, rgba(255,159,28,.20), transparent 60%),
        radial-gradient(900px 500px at 10% 110%, rgba(91,79,214,.55), transparent 60%),
        linear-gradient(180deg, #19143A, #110D27);
      border:1px solid rgba(155,140,255,.25); min-height:560px; }
    .glyphs { position:absolute; inset:0; pointer-events:none; }
    .glyphs span { position:absolute; font-family:var(--indic), var(--display); font-weight:800; color:#fff; opacity:.05;
      animation: drift linear infinite; }
    @keyframes drift { from { transform:translateY(40px) rotate(-4deg); } to { transform:translateY(-60px) rotate(4deg); } }
    .grid { position:relative; display:grid; grid-template-columns: minmax(0,.9fr) minmax(0,1.25fr); gap:2rem; align-items:center; }
    @media (max-width: 880px) { .grid { grid-template-columns:1fr; } }
    .mark { font-family:var(--display); font-weight:800; font-size:clamp(3rem, 7vw, 5.2rem); line-height:.95; margin:0;
      letter-spacing:-.02em; color:var(--text);
      text-shadow: 3px 3px 0 var(--accent), 6px 6px 0 var(--brand-deep); }
    .q { font-family:var(--display); font-weight:500; font-size:1.55rem; line-height:1.25; margin:1.3rem 0 .8rem; max-width:22ch; }
    .lede { color:var(--muted); font-size:1rem; line-height:1.6; max-width:44ch; margin:0 0 1.2rem; }
    .facts { display:flex; flex-wrap:wrap; gap:1.4rem; }
    .fact b { display:block; font-family:var(--display); font-size:1.8rem; font-weight:800; color:var(--text); }
    .fact span { color:var(--muted); font-size:.85rem; }

    .panel { padding:1.3rem 1.4rem 1.2rem; }
    .row { display:flex; align-items:center; gap:.7rem; flex-wrap:wrap; }
    .row label { color:var(--muted); font-size:.9rem; }
    select { background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:.45rem .7rem; min-width:220px; }
    .play { margin-left:auto; border:1px solid rgba(255,159,28,.5); background:rgba(255,159,28,.12); color:var(--accent);
      border-radius:999px; padding:.4rem 1rem; font-weight:600; transition:background .2s var(--ease); }
    .play:hover { background:rgba(255,159,28,.22); }
    .prompt { margin:1rem 0 .8rem; min-height:9.5rem; padding:1rem 1.1rem; border-radius:16px 16px 16px 4px;
      background:rgba(11,9,25,.55); border:1px solid var(--border); font-size:1.12rem; font-family:var(--indic), var(--body); }
    .prompt .w { opacity:0; transform:translateY(6px); transition: opacity .35s var(--ease), transform .35s var(--ease);
      transition-delay: calc(min(var(--i), 40) * 12ms); }
    .prompt.in .w { opacity:1; transform:none; }
    .meter { display:flex; align-items:center; gap:.9rem; margin:.4rem 0 1.1rem; }
    .meter .lab { color:var(--muted); font-size:.9rem; white-space:nowrap; }
    .meter .lab b { color:var(--text); font-family:var(--display); font-size:1.15rem; }
    .bar { flex:1; height:10px; border-radius:999px; background:rgba(255,255,255,.06); overflow:hidden; }
    .bar div { height:100%; width:0; border-radius:999px; background:linear-gradient(90deg, var(--brand), var(--accent));
      transition: width .6s var(--ease); }

    .dial { position:relative; padding:.2rem 0 .2rem; }
    input[type=range] { -webkit-appearance:none; appearance:none; width:100%; height:34px; background:transparent; margin:0; }
    input[type=range]::-webkit-slider-runnable-track { height:6px; border-radius:999px;
      background:linear-gradient(90deg, rgba(155,140,255,.6), rgba(255,159,28,.6), rgba(76,201,240,.6)); }
    input[type=range]::-moz-range-track { height:6px; border-radius:999px;
      background:linear-gradient(90deg, rgba(155,140,255,.6), rgba(255,159,28,.6), rgba(76,201,240,.6)); }
    input[type=range]::-webkit-slider-thumb { -webkit-appearance:none; width:26px; height:26px; margin-top:-10px; border-radius:50%;
      background:var(--text); border:5px solid var(--accent); box-shadow:0 0 0 6px rgba(255,159,28,.18), 0 6px 18px rgba(0,0,0,.5); }
    input[type=range]::-moz-range-thumb { width:18px; height:18px; border-radius:50%; background:var(--text);
      border:5px solid var(--accent); box-shadow:0 0 0 6px rgba(255,159,28,.18); }
    .stops { display:grid; grid-template-columns:repeat(var(--n), 1fr); margin-top:.3rem; }
    .stops button { background:none; border:0; padding:.3rem .1rem; color:var(--faint); font-size:.78rem; line-height:1.2;
      transition:color .2s var(--ease); }
    .stops button:hover { color:var(--muted); }
    .stops button.on { color:var(--text); font-weight:600; }

    .lights { display:grid; grid-template-columns:repeat(auto-fit, minmax(150px,1fr)); gap:.6rem; margin-top:1rem; }
    .light { display:flex; align-items:center; gap:.65rem; padding:.6rem .75rem; border-radius:12px;
      background:rgba(255,255,255,.03); border:1px solid var(--border); transition: border-color .3s var(--ease), background .3s var(--ease); }
    .light i { width:12px; height:12px; border-radius:50%; flex:none; }
    .light.pass i { background:var(--pass); box-shadow:0 0 12px var(--pass); }
    .light.fail i { background:var(--fail); box-shadow:0 0 14px var(--fail); }
    .light.fail { border-color:rgba(255,92,122,.5); background:rgba(255,92,122,.07); }
    .light .n { font-weight:600; font-size:.92rem; }
    .light .r { color:var(--muted); font-size:.8rem; }
    .keys { margin-top:.2rem; }
    """
    body = """
    <section class="hero">
      <div class="glyphs" id="glyphs" aria-hidden="true"></div>
      <div class="grid">
        <div>
          <h1 class="mark">MixCheck</h1>
          <p class="q">Same coding task. Different language. Does the AI still get it right?</p>
          <p class="lede">Drag the dial to rewrite one prompt the way Indians actually type it.
            The lights show whether each AI model's code passed the tests for that exact prompt.</p>
          <div class="facts" id="facts"></div>
        </div>
        <div class="glass panel">
          <div class="row">
            <label for="task">Task</label>
            <select id="task"></select>
            <button class="play" id="play" type="button">Play all versions</button>
          </div>
          <div class="prompt" id="prompt" aria-live="polite"></div>
          <div class="keys" id="keys"></div>
          <div class="meter">
            <span class="lab"><b id="mixpct">0%</b> of words not in English</span>
            <div class="bar"><div id="mixbar"></div></div>
          </div>
          <div class="dial">
            <input type="range" id="dial" min="0" step="1" aria-label="Prompt version">
            <div class="stops" id="stops"></div>
          </div>
          <div class="lights" id="lights"></div>
        </div>
      </div>
    </section>
    """
    script = r"""
    const V = DATA.versions, M = DATA.models, TASKS = DATA.tasks;
    const $ = id => document.getElementById(id);
    const dial = $('dial'), sel = $('task'), prompt = $('prompt');
    dial.max = V.length - 1;
    const LANGS = {hi:['Hindi','rgba(255,159,28,.6)'], bn:['Bengali','rgba(76,201,240,.55)'], kn:['Kannada','rgba(232,123,164,.6)'],
                   ta:['Tamil','rgba(158,228,147,.55)'], or:['Odia','rgba(255,209,102,.6)']};
    const present = new Set(); TASKS.forEach(t => Object.values(t.prompts).forEach(p => p.words.forEach(([, g]) => present.add(g))));
    $('keys').innerHTML = '<span class="key"><i style="background:none;border-bottom:2px solid rgba(155,140,255,.8);border-radius:0;height:.6rem"></i>English</span>' +
      Object.entries(LANGS).filter(([k]) => present.has(k)).map(([, [n, c]]) => `<span class="key"><i style="background:${c}"></i>${n}</span>`).join('') +
      '<span class="key"><i style="background:rgba(255,255,255,.15)"></i>names and numbers</span>';
    $('stops').style.setProperty('--n', V.length);
    $('facts').innerHTML = DATA.facts.map(([n, l]) => `<div class="fact"><b>${esc(n)}</b><span>${esc(l)}</span></div>`).join('');
    TASKS.forEach((t, i) => sel.insertAdjacentHTML('beforeend', `<option value="${i}">${esc(t.title)}</option>`));
    sel.value = DATA.start_task;
    $('stops').innerHTML = V.map((v, i) => `<button type="button" data-i="${i}">${esc(v.label)}</button>`).join('');
    $('stops').addEventListener('click', e => { const b = e.target.closest('button'); if (b) { stop(); set(+b.dataset.i); } });

    // drifting letters in the background layer
    const glyphs = ['a','क','ক','ख','ব','{ }','ण','ড','z','ग','ল','()'];
    $('glyphs').innerHTML = glyphs.map((g, i) => {
      const size = 40 + (i * 37) % 90, left = (i * 83) % 100, top = (i * 47) % 90, dur = 18 + (i * 7) % 20;
      return `<span style="left:${left}%;top:${top}%;font-size:${size}px;animation-duration:${dur}s;animation-direction:${i%2?'alternate':'alternate-reverse'};animation-iteration-count:infinite">${g}</span>`;
    }).join('');

    function render(){
      const t = TASKS[+sel.value], vi = +dial.value, v = V[vi], p = t.prompts[v.key];
      prompt.classList.remove('in');
      prompt.innerHTML = p ? wordsHtml(p.words) : '<span class="w code">no prompt for this version</span>';
      prompt.classList.toggle('indic', v.key.includes('devanagari'));
      requestAnimationFrame(() => requestAnimationFrame(() => prompt.classList.add('in')));
      const mix = p ? Math.round(p.mix * 100) : 0;
      $('mixpct').textContent = mix + '%';
      $('mixbar').style.width = mix + '%';
      document.querySelectorAll('#stops button').forEach((b, i) => b.classList.toggle('on', i === vi));
      $('lights').innerHTML = M.map(m => {
        const r = (t.results[v.key] || {})[m.key];
        if (!r) return `<div class="light"><i style="background:var(--faint)"></i><div><div class="n">${esc(m.label)}</div><div class="r">not run</div></div></div>`;
        const ok = r[0] === r[1];
        return `<div class="light ${ok ? 'pass' : 'fail'}"><i></i><div><div class="n">${esc(m.label)}</div>
                <div class="r">${ok ? 'Passed' : 'Failed'}: ${r[0]} of ${r[1]} tests</div></div></div>`;
      }).join('');
    }
    function set(i){ dial.value = i; render(); }
    dial.addEventListener('input', () => { stop(); render(); });
    sel.addEventListener('change', render);

    // presenter mode: step through every version automatically
    let timer = null;
    function stop(){ if (timer) { clearInterval(timer); timer = null; $('play').textContent = 'Play all versions'; } }
    $('play').addEventListener('click', () => {
      if (timer) return stop();
      $('play').textContent = 'Pause';
      timer = setInterval(() => set((+dial.value + 1) % V.length), 2600);
    });
    set(DATA.start_version);
    """
    return _page(css, body, script, data)


# ---------------------------------------------------------------
# 2. The results grid (click a cell to open the answers behind it)
# ---------------------------------------------------------------
def heat_grid(data):
    css = """
    .wrap { display:grid; grid-template-columns:minmax(0,1.35fr) minmax(0,1fr); gap:1.2rem; align-items:start; }
    @media (max-width: 900px) { .wrap { grid-template-columns:1fr; } }
    table { width:100%; border-collapse:separate; border-spacing:6px; }
    th { font-weight:500; color:var(--muted); font-size:.8rem; text-align:center; padding:0 .2rem .3rem; line-height:1.25; }
    th.model { text-align:right; color:var(--text); font-size:.92rem; white-space:nowrap; padding-right:.6rem; }
    td button { width:100%; height:68px; border-radius:12px; border:1px solid var(--border); background:var(--surface);
      display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2px;
      transition: transform .15s var(--ease), border-color .15s var(--ease), box-shadow .15s var(--ease); }
    td button:hover { transform:translateY(-2px); border-color:rgba(155,140,255,.6); }
    td button b { font-family:var(--display); font-size:1.15rem; font-weight:800; }
    td button span { font-size:.75rem; color:var(--muted); }
    td button.fail { background:linear-gradient(160deg, rgba(255,92,122,calc(var(--f) * .9)), rgba(255,92,122,calc(var(--f) * .35)));
      border-color:rgba(255,92,122,.55); box-shadow:0 0 22px rgba(255,92,122,calc(var(--f) * .8)); }
    td button.sel { outline:3px solid var(--accent); outline-offset:2px; }
    .hint { color:var(--faint); font-size:.85rem; margin:.4rem 0 0 .4rem; }
    .drawer { padding:1.1rem 1.2rem; max-height:520px; overflow:auto; }
    .drawer h3 { font-family:var(--display); margin:0 0 .2rem; font-size:1.25rem; }
    .drawer .sub { color:var(--muted); margin:0 0 .9rem; font-size:.92rem; }
    .item { border-top:1px solid var(--border); padding:.8rem 0; }
    .item:first-of-type { border-top:0; }
    .item .head { display:flex; align-items:center; gap:.6rem; flex-wrap:wrap; margin-bottom:.5rem; }
    .item .t { font-weight:600; }
    .bubble { padding:.7rem .85rem; border-radius:12px 12px 12px 4px; background:var(--surface-2); border:1px solid var(--border);
      margin-bottom:.6rem; line-height:1.5; font-family:var(--indic), var(--body); }
    .why { color:var(--muted); font-size:.85rem; margin-top:.5rem; }
    .passlist { display:flex; flex-wrap:wrap; gap:.4rem; margin-top:.4rem; }
    .passlist span { font-size:.78rem; color:var(--muted); padding:.2rem .55rem; border-radius:999px; background:rgba(43,217,160,.08);
      border:1px solid rgba(43,217,160,.25); }
    .drawer.enter { animation: slide .35s var(--ease); }
    @keyframes slide { from { opacity:0; transform:translateX(14px); } to { opacity:1; transform:none; } }
    """
    body = """
    <div class="wrap">
      <div>
        <table id="grid" aria-label="Pass rate for each model and prompt version"></table>
        <p class="hint">Click any cell to see the answers behind it.</p>
      </div>
      <div class="glass drawer" id="drawer" aria-live="polite"></div>
    </div>
    """
    script = r"""
    const V = DATA.versions, M = DATA.models, C = DATA.cells;
    const grid = document.getElementById('grid'), drawer = document.getElementById('drawer');
    let head = '<tr><th></th>' + V.map(v => `<th>${esc(v.label)}</th>`).join('') + '</tr>';
    let rows = M.map(m => '<tr><th class="model">' + esc(m.label) + '</th>' + V.map(v => {
      const c = (C[m.key] || {})[v.key];
      if (!c) return '<td></td>';
      const fails = c.total - c.passed, f = (fails / c.total).toFixed(3);
      return `<td><button type="button" class="${fails ? 'fail' : ''}" style="--f:${Math.min(1, f * 3)}" data-m="${m.key}" data-v="${v.key}"
              aria-label="${esc(m.label)}, ${esc(v.label)}: ${c.passed} of ${c.total} passed">
              <b>${Math.round(100 * c.passed / c.total)}%</b><span>${c.passed}/${c.total}</span></button></td>`;
    }).join('') + '</tr>').join('');
    grid.innerHTML = head + rows;

    function open(mk, vk){
      const m = M.find(x => x.key === mk), v = V.find(x => x.key === vk), c = C[mk][vk];
      document.querySelectorAll('td button').forEach(b => b.classList.toggle('sel', b.dataset.m === mk && b.dataset.v === vk));
      const fails = c.items.filter(i => !i.ok), passes = c.items.filter(i => i.ok);
      drawer.classList.remove('enter'); void drawer.offsetWidth; drawer.classList.add('enter');
      drawer.innerHTML = `<h3>${esc(m.label)} on ${esc(v.label)}</h3>
        <p class="sub">${c.passed} of ${c.total} tasks passed every test${fails.length ? '. Here is what failed.' : '.'}</p>` +
        fails.map(i => `<div class="item"><div class="head"><span class="pill fail">Failed ${i.passed}/${i.cases}</span>
          <span class="t">${esc(i.title)}</span></div>
          <div class="bubble">${esc(i.prompt)}</div>
          ${i.code ? `<pre class="code">${highlight(i.code)}</pre>` : ''}
          ${i.error ? `<div class="why">What went wrong: ${esc(i.error)}</div>` : ''}</div>`).join('') +
        (passes.length ? `<div class="item"><div class="head"><span class="pill pass">Passed</span><span class="t">${passes.length} tasks</span></div>
          <div class="passlist">${passes.map(i => `<span>${esc(i.title)}</span>`).join('')}</div></div>` : '');
    }
    grid.addEventListener('click', e => { const b = e.target.closest('button[data-m]'); if (b) open(b.dataset.m, b.dataset.v); });
    // open the most interesting cell first: the one with the most failures
    let best = null;
    M.forEach(m => V.forEach(v => { const c = (C[m.key] || {})[v.key]; if (c && (!best || c.total - c.passed > best[2])) best = [m.key, v.key, c.total - c.passed]; }));
    if (best) open(best[0], best[1]);
    """
    return _page(css, body, script, data)


# ---------------------------------------------------------------
# 3. Guess the verdict
# ---------------------------------------------------------------
def guess_game(data):
    css = """
    .game { padding:1.4rem 1.5rem; }
    .top { display:flex; align-items:center; gap:1rem; flex-wrap:wrap; margin-bottom:1rem; }
    .top h3 { font-family:var(--display); font-size:1.4rem; margin:0; }
    .score { margin-left:auto; display:flex; gap:.35rem; }
    .score i { width:12px; height:12px; border-radius:50%; background:rgba(255,255,255,.1); display:inline-block; transition:background .3s var(--ease); }
    .score i.right { background:var(--pass); } .score i.wrong { background:var(--fail); }
    .meta { color:var(--muted); font-size:.9rem; margin-bottom:.5rem; }
    .meta b { color:var(--text); font-weight:600; }
    .cols { display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.2fr); gap:1rem; }
    @media (max-width: 820px) { .cols { grid-template-columns:1fr; } }
    .bubble { padding:.9rem 1rem; border-radius:16px 16px 16px 4px; background:var(--surface-2); border:1px solid var(--border);
      font-size:1.05rem; line-height:1.55; font-family:var(--indic), var(--body); }
    .label { color:var(--faint); font-size:.85rem; margin:0 0 .35rem; }
    pre.code { max-height:260px; }
    .ask { display:flex; gap:.8rem; margin-top:1.1rem; flex-wrap:wrap; align-items:center; }
    .ask .q { color:var(--muted); margin-right:.4rem; }
    .btn { border-radius:999px; padding:.7rem 1.4rem; font-weight:600; border:1px solid; transition: transform .15s var(--ease), background .15s var(--ease); }
    .btn:hover { transform:translateY(-2px); }
    .btn.p { color:var(--pass); border-color:rgba(43,217,160,.55); background:rgba(43,217,160,.1); }
    .btn.f { color:var(--fail); border-color:rgba(255,92,122,.55); background:rgba(255,92,122,.1); }
    .btn.n { color:#1a0f00; border:0; background:linear-gradient(135deg, var(--accent), #FF6B3D); }
    .reveal { margin-top:1.1rem; padding:1rem 1.1rem; border-radius:14px; border:1px solid; animation: pop .45s var(--ease); }
    .reveal.right { border-color:rgba(43,217,160,.5); background:rgba(43,217,160,.08); }
    .reveal.wrong { border-color:rgba(255,92,122,.5); background:rgba(255,92,122,.08); }
    .reveal .big { font-family:var(--display); font-weight:800; font-size:1.5rem; }
    .reveal .why { color:var(--muted); margin-top:.3rem; line-height:1.5; }
    @keyframes pop { from { opacity:0; transform:scale(.97) translateY(6px); } to { opacity:1; transform:none; } }
    .end { text-align:center; padding:2rem 1rem; }
    .end .big { font-family:var(--display); font-weight:800; font-size:3rem; }
    .end p { color:var(--muted); max-width:48ch; margin:.6rem auto 1.2rem; line-height:1.6; }
    """
    body = """
    <div class="glass game">
      <div class="top"><h3>Guess the verdict</h3><span class="meta" id="count"></span><div class="score" id="score"></div></div>
      <div id="stage"></div>
    </div>
    """
    script = r"""
    const D = DATA.deck; let i = 0, results = [];
    const stage = document.getElementById('stage');
    function dots(){ document.getElementById('score').innerHTML = D.map((_, k) =>
      `<i class="${results[k] === true ? 'right' : results[k] === false ? 'wrong' : ''}"></i>`).join(''); }
    function card(){
      dots();
      if (i >= D.length) return finish();
      const c = D[i];
      document.getElementById('count').textContent = `Card ${i + 1} of ${D.length}`;
      stage.innerHTML = `<div class="meta">${esc(c.title)}, asked in <b>${esc(c.version)}</b> to <b>${esc(c.model)}</b></div>
        <div class="cols"><div><p class="label">The prompt</p><div class="bubble">${esc(c.prompt)}</div></div>
        <div><p class="label">The AI's code</p><pre class="code">${highlight(c.code)}</pre></div></div>
        <div id="rev"></div><div class="ask" id="ask"><span class="q">Will this code pass all ${c.cases} test cases?</span>
          <button class="btn p" data-g="1" type="button">It passes</button>
          <button class="btn f" data-g="0" type="button">It fails</button></div>`;
    }
    function answer(guessPass){
      const c = D[i], right = guessPass === c.ok; results[i] = right; dots();
      document.getElementById('ask').innerHTML = `<button class="btn n" id="next" type="button">${i + 1 < D.length ? 'Next card' : 'See your score'}</button>`;
      document.getElementById('rev').innerHTML = (`<div class="reveal ${right ? 'right' : 'wrong'}">
        <div class="big">${right ? 'Correct' : 'Not quite'}: it ${c.ok ? 'passed' : 'failed'} ${c.passed} of ${c.cases} tests</div>
        <div class="why">${esc(c.why)}</div></div>`);
      document.getElementById('next').focus();
    }
    function finish(){
      const n = results.filter(Boolean).length;
      document.getElementById('count').textContent = '';
      stage.innerHTML = `<div class="end"><div class="big">${n} of ${D.length}</div>
        <p>Even with the code in front of you, a failure is hard to spot by eye. That's why MixCheck runs every answer against real test cases instead of trusting how the code looks.</p>
        <button class="btn n" id="again" type="button">Play again</button></div>`;
    }
    stage.addEventListener('click', e => {
      const g = e.target.closest('[data-g]'); if (g) return answer(g.dataset.g === '1');
      if (e.target.id === 'next') { i++; card(); }
      if (e.target.id === 'again') { i = 0; results = []; card(); }
    });
    card();
    """
    return _page(css, body, script, data)
