import json
import streamlit as st
from pathlib import Path

profile = json.loads(Path("data/projects.json").read_text())["profile"]

st.title("Get in touch")
st.write("Have a project, an internship, or just want to say hi? Drop me a line.")

# ---------- Download CV ----------
st.subheader("📄 My CV")
st.write("Grab a copy of my CV — a one-page PDF with my education, skills and projects.")

cv_path = Path("assets/Sushant-Chaudhary-CV.pdf")
if cv_path.exists():
    with open(cv_path, "rb") as f:
        st.download_button(
            label="⬇️ Download CV (PDF)",
            data=f,
            file_name="Sushant-Chaudhary-CV.pdf",
            mime="application/pdf",
            type="primary",
        )
else:
    st.warning("CV file not found in assets folder.")

st.divider()

# ---------- Contact form ----------
with st.form("contact", clear_on_submit=True):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    subject = st.text_input("Subject")
    message = st.text_area("Message", height=140)
    submitted = st.form_submit_button("Send", use_container_width=True)

if submitted:
    if not all([name, email, subject, message]):
        st.error("Please fill in every field.")
    else:
        mailto = (
            f"mailto:{profile['email']}"
            f"?subject={subject}"
            f"&body=From: {name} ({email})%0D%0A%0D%0A{message}"
        )
        st.success(f"Thanks, {name}! If your mail client doesn't open, email me at {profile['email']}.")
        st.markdown(f"[Open email client]({mailto})")

st.divider()

# ---------- Social links ----------
st.subheader("Elsewhere")
c1, c2, c3 = st.columns(3)
c1.link_button("🐙 GitHub", profile["github"], use_container_width=True)
c2.link_button("📷 Instagram", profile["instagram"], use_container_width=True)
c3.link_button("✉️ Email", f"mailto:{profile['email']}", use_container_width=True)