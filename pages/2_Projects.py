import json
import streamlit as st
from pathlib import Path

DATA = json.loads(Path("data/projects.json").read_text())

st.title("Projects")
st.write("Real projects, real data, real code. Everything links to a notebook or live demo.")

for p in DATA["projects"]:
    with st.container(border=True):
        st.markdown(f"### {p['title']}")
        st.write(p["description"])
        st.caption(" · ".join(f"`{t}`" for t in p["tags"]))
        c1, c2, _ = st.columns([1, 1, 3])
        if p.get("notebook"):
            c1.link_button("📓 Notebook", p["notebook"], use_container_width=True)
        if p.get("demo"):
            c2.link_button("🚀 Live Demo", p["demo"], use_container_width=True)