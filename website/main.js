/* MixCheck: particle glyph scene + page interactions */
(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const isSmall = window.matchMedia("(max-width: 760px)").matches;

  /* ---------- language dial data ---------- */
  // Same sound ("ka"), four scripts: one task, different language.
  const LANGS = [
    { name: "English",  caption: "Plain English prompt",  glyph: { text: "{ }", font: '600 300px "IBM Plex Mono", monospace' } },
    { name: "Hinglish", caption: "Hindi + English",       glyph: { text: "क", font: '800 400px "Noto Sans Devanagari", sans-serif' } },
    { name: "Benglish", caption: "Bengali + English",     glyph: { text: "ক", font: '800 400px "Noto Sans Bengali", sans-serif' } },
    { name: "Kanglish", caption: "Kannada + English",     glyph: { text: "ಕ", font: '800 400px "Noto Sans Kannada", sans-serif' } },
  ];

  const SECTION_GLYPHS = {
    question: { text: "?", font: '700 400px "Unbounded", sans-serif' },
    braces:   { text: "{ }", font: '600 300px "IBM Plex Mono", monospace' },
    "96":     { text: "96%", font: '700 250px "Unbounded", sans-serif' },
    check:    { check: true },
    logo:     { text: "mc", font: '800 300px "Unbounded", sans-serif' },
    team:     { text: "ERA", font: '800 230px "Unbounded", sans-serif' },
  };

  /* ---------- embedded dashboard ---------- */
  // Inside the Streamlit app the page is an about:srcdoc frame whose base URL is the app's
  // own page (on Community Cloud that sits under /~/+/), so the dashboard is a relative path.
  // Opened on its own, point at the live app.
  const inApp = location.href === "about:srcdoc";
  const LIVE_APP = "https://mixcheck-elrata.streamlit.app/";
  const dashboardUrl = new URL("dashboard", inApp ? document.baseURI : LIVE_APP).href;
  const dashFrame = document.querySelector("[data-dashboard]");
  if (dashFrame) dashFrame.src = dashboardUrl + "?embed=true&embed_options=dark_theme";
  document.querySelectorAll("[data-dashboard-link]").forEach((a) => { a.href = dashboardUrl; });

  // A srcdoc page resolves "#id" against the parent app's URL, which would load the app
  // inside this frame. Scroll in place instead.
  document.addEventListener("click", (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const target = a.getAttribute("href") === "#top" ? document.body : document.querySelector(a.getAttribute("href"));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
  });

  /* ---------- page: reveal + deep state ---------- */
  document.documentElement.classList.add("reveal-ready");
  const panels = document.querySelectorAll(".panel");
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("is-in"); revealObs.unobserve(e.target); } });
  }, { threshold: 0.25 });
  panels.forEach((p) => revealObs.observe(p));

  /* ---------- dial UI ---------- */
  const dialButtons = Array.from(document.querySelectorAll("[data-lang]"));
  const caption = document.querySelector(".dial-caption");
  let langIndex = 1;
  let autoCycle = !reduceMotion;
  let cycleTimer = null;

  function setLang(i, fromUser) {
    langIndex = (i + LANGS.length) % LANGS.length;
    dialButtons.forEach((b, j) => b.setAttribute("aria-pressed", String(j === langIndex)));
    caption.textContent = LANGS[langIndex].caption;
    if (fromUser) { autoCycle = false; clearInterval(cycleTimer); }
    if (scene && currentSection === "hero") scene.morphTo(LANGS[langIndex].glyph);
  }
  dialButtons.forEach((b) => b.addEventListener("click", () => setLang(Number(b.dataset.lang), true)));
  document.querySelectorAll(".dial-arrow").forEach((b) =>
    b.addEventListener("click", () => setLang(langIndex + Number(b.dataset.step), true)));

  /* ---------- section tracking ---------- */
  let currentSection = "hero";
  const sections = document.querySelectorAll("[data-glyph]");
  const sectionObs = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const key = e.target.dataset.glyph;
      if (key === currentSection) return;
      currentSection = key;
      document.body.classList.toggle("is-deep", key !== "hero");
      if (!scene) return;
      scene.setDeep(key !== "hero");
      scene.morphTo(key === "hero" ? LANGS[langIndex].glyph : SECTION_GLYPHS[key]);
    });
  }, { rootMargin: "-45% 0px -45% 0px" });
  sections.forEach((s) => sectionObs.observe(s));

  /* ---------- three.js scene ---------- */
  let scene = null;
  if (window.THREE) {
    try { scene = createScene(); } catch (err) { console.warn("WebGL unavailable", err); }
  }
  if (!scene) document.body.classList.add("no-webgl");

  const fontsReady = document.fonts && document.fonts.load
    ? Promise.all([
        document.fonts.load('800 100px "Noto Sans Devanagari"', "क"),
        document.fonts.load('800 100px "Noto Sans Bengali"', "ক"),
        document.fonts.load('800 100px "Noto Sans Kannada"', "ಕ"),
        document.fonts.load('700 100px "Unbounded"', "96%"),
        document.fonts.load('600 100px "IBM Plex Mono"', "{}"),
      ]).catch(() => {})
    : Promise.resolve();

  fontsReady.then(() => {
    if (!scene) return;
    scene.morphTo(LANGS[langIndex].glyph);
    if (autoCycle) {
      cycleTimer = setInterval(() => {
        if (autoCycle && currentSection === "hero" && !document.hidden) setLang(langIndex + 1, false);
      }, 3800);
    }
  });

  function createScene() {
    const THREE = window.THREE;
    const canvas = document.getElementById("scene");
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: "high-performance" });
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    renderer.setPixelRatio(dpr);
    renderer.setClearColor(0x000000, 0);

    const world = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
    camera.position.set(0, 0.35, 9.5);

    const group = new THREE.Group();
    world.add(group);

    /* glyph particles */
    const COUNT = isSmall ? 4200 : 9000;
    const pos = new Float32Array(COUNT * 3);
    const target = new Float32Array(COUNT * 3);
    const speed = new Float32Array(COUNT);
    const sizes = new Float32Array(COUNT);
    const colors = new Float32Array(COUNT * 3);
    const accent = new Uint8Array(COUNT);

    for (let i = 0; i < COUNT; i++) {
      const r = 1.5 + Math.random() * 2.5;
      const t = Math.random() * Math.PI * 2;
      const p = Math.acos(2 * Math.random() - 1);
      pos[i * 3] = r * Math.sin(p) * Math.cos(t);
      pos[i * 3 + 1] = r * Math.sin(p) * Math.sin(t);
      pos[i * 3 + 2] = r * Math.cos(p);
      target.set(pos.subarray(i * 3, i * 3 + 3), i * 3);
      speed[i] = 0.035 + Math.random() * 0.06;
      sizes[i] = 0.6 + Math.random() * 1.0;
      accent[i] = Math.random() < 0.035 ? 1 : 0;
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    geo.setAttribute("aSize", new THREE.BufferAttribute(sizes, 1));
    geo.setAttribute("aColor", new THREE.BufferAttribute(colors, 3));

    const pointMat = new THREE.ShaderMaterial({
      transparent: true,
      depthWrite: false,
      uniforms: {
        uSize: { value: (isSmall ? 28 : 36) * dpr },
        uOpacity: { value: 1 },
      },
      vertexShader: `
        attribute float aSize;
        attribute vec3 aColor;
        uniform float uSize;
        varying vec3 vColor;
        varying float vFog;
        void main() {
          vec4 mv = modelViewMatrix * vec4(position, 1.0);
          gl_Position = projectionMatrix * mv;
          gl_PointSize = uSize * aSize / -mv.z;
          float depth = -mv.z;
          vFog = smoothstep(16.0, 6.5, depth);
          // front of the glyph catches the light, back falls into fog
          vColor = aColor * mix(0.55, 1.15, smoothstep(10.6, 8.6, depth));
        }`,
      fragmentShader: `
        uniform float uOpacity;
        varying vec3 vColor;
        varying float vFog;
        void main() {
          vec2 c = gl_PointCoord - 0.5;
          float d = length(c);
          float a = smoothstep(0.5, 0.12, d);
          gl_FragColor = vec4(vColor, a * vFog * uOpacity);
        }`,
    });
    const points = new THREE.Points(geo, pointMat);
    group.add(points);

    /* faint wireframe shell, like the mesh around the reference's X */
    const shell = new THREE.LineSegments(
      new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(3.1, 2)),
      new THREE.LineBasicMaterial({ color: 0xe7eaef, transparent: true, opacity: 0.05, depthWrite: false })
    );
    group.add(shell);

    /* pedestal rings */
    const pedestal = new THREE.Group();
    [1.4, 2.3, 3.4, 4.8, 6.6].forEach((r, i) => {
      const pts = [];
      for (let k = 0; k <= 128; k++) {
        const a = (k / 128) * Math.PI * 2;
        pts.push(new THREE.Vector3(Math.cos(a) * r, 0, Math.sin(a) * r));
      }
      const ring = new THREE.LineLoop(
        new THREE.BufferGeometry().setFromPoints(pts),
        new THREE.LineBasicMaterial({ color: i === 0 ? 0xf4b23e : 0xe7eaef, transparent: true, opacity: i === 0 ? 0.5 : 0.22 - i * 0.03, depthWrite: false })
      );
      pedestal.add(ring);
    });
    pedestal.position.y = -2.35;
    world.add(pedestal);

    /* drifting snow / dust */
    const DUST = isSmall ? 260 : 600;
    const dustPos = new Float32Array(DUST * 3);
    const dustSize = new Float32Array(DUST);
    const dustCol = new Float32Array(DUST * 3);
    for (let i = 0; i < DUST; i++) {
      dustPos[i * 3] = (Math.random() - 0.5) * 22;
      dustPos[i * 3 + 1] = (Math.random() - 0.5) * 14;
      dustPos[i * 3 + 2] = (Math.random() - 0.5) * 10 - 1;
      dustSize[i] = 0.4 + Math.random() * 0.9;
      dustCol.set([0.85, 0.88, 0.92], i * 3);
    }
    const dustGeo = new THREE.BufferGeometry();
    dustGeo.setAttribute("position", new THREE.BufferAttribute(dustPos, 3));
    dustGeo.setAttribute("aSize", new THREE.BufferAttribute(dustSize, 1));
    dustGeo.setAttribute("aColor", new THREE.BufferAttribute(dustCol, 3));
    const dustMat = pointMat.clone();
    dustMat.uniforms.uSize.value = 34 * dpr;
    dustMat.uniforms.uOpacity.value = 0.55;
    world.add(new THREE.Points(dustGeo, dustMat));

    /* ---------- glyph sampling ---------- */
    const off = document.createElement("canvas");
    const W = 1024, H = 640;
    off.width = W; off.height = H;
    const ctx = off.getContext("2d", { willReadFrequently: true });
    const cache = new Map();

    function sample(glyph) {
      const key = glyph.check ? "check" : glyph.text + glyph.font;
      if (cache.has(key)) return cache.get(key);
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = "#fff";
      ctx.strokeStyle = "#fff";
      if (glyph.check) {
        ctx.lineWidth = 92; ctx.lineCap = "round"; ctx.lineJoin = "round";
        ctx.beginPath();
        ctx.moveTo(330, 330); ctx.lineTo(460, 460); ctx.lineTo(700, 180);
        ctx.stroke();
      } else {
        ctx.font = glyph.font;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        const m = ctx.measureText(glyph.text);
        const scale = Math.min(1, 860 / m.width);
        ctx.save();
        ctx.translate(W / 2, H / 2 + 20);
        ctx.scale(scale, scale);
        ctx.fillText(glyph.text, 0, 0);
        ctx.restore();
      }
      const data = ctx.getImageData(0, 0, W, H).data;
      const hits = [];
      for (let y = 0; y < H; y += 3) {
        for (let x = 0; x < W; x += 3) {
          if (data[(y * W + x) * 4 + 3] > 120) hits.push(x, y);
        }
      }
      cache.set(key, hits);
      return hits;
    }

    const SNOW = [0.91, 0.92, 0.94];
    const MARIGOLD = [0.96, 0.7, 0.24];
    const PASS = [0.56, 0.89, 0.71];
    let tint = SNOW;
    const colorTarget = new Float32Array(COUNT * 3);

    function morphTo(glyph, instant) {
      if (!glyph) return;
      const hits = sample(glyph);
      const n = hits.length / 2;
      if (!n) return;
      const unit = 7.6 / W;
      tint = glyph.check ? PASS : SNOW;
      for (let i = 0; i < COUNT; i++) {
        const h = Math.floor(Math.random() * n) * 2;
        const x = (hits[h] - W / 2 + Math.random() * 3) * unit;
        const y = -(hits[h + 1] - H / 2 + Math.random() * 3) * unit + 0.15;
        const z = (Math.random() - 0.5) * 0.7 + (Math.random() < 0.08 ? (Math.random() - 0.5) * 2.2 : 0);
        target[i * 3] = x; target[i * 3 + 1] = y; target[i * 3 + 2] = z;
        const c = accent[i] ? MARIGOLD : tint;
        colorTarget.set(c, i * 3);
        if (instant || reduceMotion) {
          pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z;
          colors.set(c, i * 3);
        } else {
          // scatter a little first so the morph reads as particles regrouping
          pos[i * 3] += (Math.random() - 0.5) * 0.6;
          pos[i * 3 + 1] += (Math.random() - 0.5) * 0.6;
          pos[i * 3 + 2] += (Math.random() - 0.5) * 1.2;
        }
      }
      geo.attributes.position.needsUpdate = true;
      geo.attributes.aColor.needsUpdate = true;
      if (reduceMotion) render();
    }
    colors.fill(0.9);

    /* ---------- layout + state ---------- */
    let deep = false;
    const groupX = { cur: 0, to: 0 };
    let heroY = 0;
    const groupOpacity = { cur: 1, to: 1 };
    const pedestalOpacity = { cur: 1, to: 1 };

    function setDeep(v) {
      deep = v;
      layout();
    }
    function layout() {
      const w = canvas.clientWidth, h = canvas.clientHeight;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      const wide = w > 900;
      const reach = Math.min(1.25, camera.aspect / 1.6);
      // keep the widest glyph (~6.5 units) inside narrow viewports
      const visibleWidth = 2 * Math.tan((camera.fov * Math.PI) / 360) * camera.position.z * camera.aspect;
      group.scale.setScalar(Math.min(1, (visibleWidth * 0.86) / 6.5));
      // hero: lift the glyph clear of the headline and nudge it right on wide screens
      groupX.to = wide ? (deep ? 3.4 : 1.2) * reach : 0;
      heroY = deep ? 0 : (wide ? 1.15 : 0.9);
      groupOpacity.to = deep ? (wide ? 0.6 : 0.2) : 1;
      pedestalOpacity.to = deep ? 0 : 1;
      if (reduceMotion) render();
    }
    window.addEventListener("resize", layout);
    layout();

    const pointer = { x: 0, y: 0 };
    window.addEventListener("pointermove", (e) => {
      pointer.x = e.clientX / window.innerWidth - 0.5;
      pointer.y = e.clientY / window.innerHeight - 0.5;
    }, { passive: true });

    /* ---------- loop ---------- */
    const clock = new THREE.Clock();
    function render() {
      // time-based easing so slow or throttled devices still settle into the glyph
      const dt = Math.min(clock.getDelta(), 0.25);
      const frames = dt * 60;
      const t = clock.elapsedTime;
      const ease = (s) => 1 - Math.pow(1 - s, frames);
      const k = reduceMotion ? 1 : ease(0.06);

      groupX.cur += (groupX.to - groupX.cur) * k;
      groupOpacity.cur += (groupOpacity.to - groupOpacity.cur) * k;
      pedestalOpacity.cur += (pedestalOpacity.to - pedestalOpacity.cur) * k;

      group.position.x = groupX.cur;
      pointMat.uniforms.uOpacity.value = groupOpacity.cur;
      shell.material.opacity = 0.05 * groupOpacity.cur;
      pedestal.children.forEach((r, i) => { r.material.opacity = (i === 0 ? 0.5 : 0.22 - i * 0.03) * pedestalOpacity.cur; });

      if (!reduceMotion) {
        const kc = ease(0.05);
        for (let i = 0; i < COUNT; i++) {
          const s = ease(speed[i]);
          const ix = i * 3;
          // tiny shimmer around the target, not cumulative drift
          const jx = Math.sin(t * 0.9 + i * 0.37) * 0.012;
          const jy = Math.cos(t * 0.7 + i) * 0.012;
          pos[ix] += (target[ix] + jx - pos[ix]) * s;
          pos[ix + 1] += (target[ix + 1] + jy - pos[ix + 1]) * s;
          pos[ix + 2] += (target[ix + 2] - pos[ix + 2]) * s;
          colors[ix] += (colorTarget[ix] - colors[ix]) * kc;
          colors[ix + 1] += (colorTarget[ix + 1] - colors[ix + 1]) * kc;
          colors[ix + 2] += (colorTarget[ix + 2] - colors[ix + 2]) * kc;
        }
        geo.attributes.position.needsUpdate = true;
        geo.attributes.aColor.needsUpdate = true;

        for (let i = 0; i < DUST; i++) {
          const iy = i * 3 + 1;
          dustPos[iy] -= (0.004 + dustSize[i] * 0.003) * frames;
          dustPos[i * 3] += Math.sin(t * 0.3 + i) * 0.002 * frames;
          if (dustPos[iy] < -7) dustPos[iy] = 7;
        }
        dustGeo.attributes.position.needsUpdate = true;

        group.rotation.y = Math.sin(t * 0.25) * 0.32 + pointer.x * 0.35;
        group.rotation.x = pointer.y * 0.15;
        shell.rotation.y = t * 0.04;
        pedestal.rotation.y = -t * 0.03;
        group.position.y += (heroY + Math.sin(t * 0.6) * 0.06 - group.position.y) * k;
      } else {
        group.position.y = heroY;
        for (let i = 0; i < COUNT * 3; i++) colors[i] = colorTarget[i];
        geo.attributes.aColor.needsUpdate = true;
      }

      renderer.render(world, camera);
    }

    if (!reduceMotion) {
      renderer.setAnimationLoop(render);
    } else {
      render();
    }

    return { morphTo, setDeep };
  }
})();
