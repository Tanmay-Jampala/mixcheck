"""
app.py - entry point for the MixCheck Streamlit app.

Run:  streamlit run app.py
  /            the MixCheck website (home.py), with the dashboard embedded in it
  /dashboard   the dashboard itself (dashboard.py)
"""

import streamlit as st

st.navigation(
    [
        st.Page("home.py", title="MixCheck", default=True),
        st.Page("dashboard.py", title="MixCheck dashboard", url_path="dashboard"),
    ],
    position="hidden",
).run()
