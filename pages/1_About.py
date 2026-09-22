import json
import streamlit as st
from pathlib import Path

DATA = json.loads(Path("data/projects.json").read_text())

st.title("About me")
st.write("""
I'm a computer science student with a growing focus on **data science and machine learning**.
I enjoy turning messy data into clear insights — and I'm building a portfolio of real projects
to prove it.

My current focus areas:
- **Data analysis** with pandas and NumPy
- **Visualization** with Matplotlib, Seaborn, Plotly
- **Machine learning** with scikit-learn
- **Deployment** with Streamlit
""")

st.subheader("Education")
for e in DATA["education"]:
    with st.container(border=True):
        st.caption(e["period"])
        st.markdown(f"**{e['title']}**")
        st.write(e["org"])

st.subheader("What I'm working on now")
st.write("""
- Finishing my first end-to-end ML project
- Learning SQL more deeply
- Contributing small fixes to open-source data tools
""")