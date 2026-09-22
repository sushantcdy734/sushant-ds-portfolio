import json
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sushant Chaudhary — Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA = json.loads(Path("data/projects.json").read_text())
profile = DATA["profile"]

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown(f"### Hi, I'm {profile['name']} 👋")
    st.title(profile["title"])
    st.write(profile["tagline"])
    st.write("")
    cta1, cta2 = st.columns([1, 1])
    with cta1:
        st.page_link("pages/2_Projects.py", label="View Projects", icon="📁")
    with cta2:
        st.page_link("pages/4_Contact.py", label="Get in Touch", icon="✉️")

with col2:
    avatar = Path("assets/profile.png")
    if avatar.exists():
        st.image(str(avatar), use_container_width=True)
    else:
        st.info("Add your photo to `assets/profile.jpg`")

st.divider()

st.subheader("Quick overview")
a, b, c = st.columns(3)
a.metric("Focus", "Data Science", "Python • ML")
b.metric("Status", "Student", "Open to internships")
c.metric("Based in", profile["location"])

st.divider()

st.subheader("Latest projects")
projects = DATA["projects"][:3]

for p in projects:
    with st.container(border=True):
        st.markdown(f"**{p['title']}**")
        st.write(p["description"])
        st.caption(" · ".join(p["tags"]))
        cols = st.columns([1, 1, 4])
        if p.get("notebook"):
            cols[0].link_button("Notebook", p["notebook"])
        if p.get("demo"):
            cols[1].link_button("Live Demo", p["demo"])

st.divider()

st.caption(
    f"Built with Python & Streamlit · "
    f"[GitHub]({profile['github']}) · "
    f"[Instagram]({profile['instagram']}) · "
    f"[Email](mailto:{profile['email']})"
)