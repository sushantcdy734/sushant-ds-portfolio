import json
import streamlit as st
from pathlib import Path

DATA = json.loads(Path("data/projects.json").read_text())

st.title("Skills")

for group, items in DATA["skills"].items():
    st.subheader(group)
    cols = st.columns(min(len(items), 5))
    for i, item in enumerate(items):
        cols[i % len(cols)].markdown(f"`{item}`")
    st.write("")