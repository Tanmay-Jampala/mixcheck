"""
home.py - the MixCheck website, served as the app's front page.

The site itself is plain HTML, CSS and JS in website/. Streamlit renders it from a
string, so the stylesheet, script and logo are inlined here; the screenshots are served
from static/screens. The page fills the browser window and scrolls on its own, and its
"Live dashboard" section embeds the /dashboard page.
"""

import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

SITE = Path(__file__).parent / "website"

st.set_page_config(page_title="MixCheck · El Rata Alada", layout="wide", initial_sidebar_state="collapsed")


SITE_FILES = ("index.html", "styles.css", "main.js", "logo.svg")


def site_version():
    """Changes whenever a site file changes, so a new deploy never serves a cached old page."""
    return tuple((SITE / name).stat().st_mtime_ns for name in SITE_FILES)


@st.cache_data
def site_html(version):
    html = (SITE / "index.html").read_text(encoding="utf-8")
    css = (SITE / "styles.css").read_text(encoding="utf-8")
    js = (SITE / "main.js").read_text(encoding="utf-8")
    logo = "data:image/svg+xml;base64," + base64.b64encode((SITE / "logo.svg").read_bytes()).decode()
    return (html
            .replace('<link rel="stylesheet" href="styles.css">', f"<style>{css}</style>")
            .replace('<script src="main.js"></script>', f"<script>{js}</script>")
            .replace("assets/logo.svg", logo)
            # relative, because on Community Cloud the app lives under /~/+/
            .replace('src="screens/', 'src="app/static/screens/'))


# Strip Streamlit's chrome so the site gets the whole window.
st.html("""
<style>
  [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
  [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], footer { display: none !important; }
  [data-testid="stMainBlockContainer"], .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stMain"], [data-testid="stAppViewContainer"] { overflow: hidden !important; }
  [data-testid="stVerticalBlock"] { gap: 0 !important; }
  [data-testid="stElementContainer"]:has(> [data-testid="stHtml"]) { display: none !important; }
  [data-testid="stIFrame"], iframe[title="st.iframe"] {
    display: block; width: 100% !important; border: 0;
    height: 100vh !important; height: 100dvh !important;
  }
</style>
""")

components.html(site_html(site_version()), height=900, scrolling=True)
