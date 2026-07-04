import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Resume",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume")

st.write("""
Explore my resume to learn about my education, technical skills, internships,
projects, certifications, and achievements.
""")

resume_path = "resume/Vanshika_Soni_Resume.pdf"


def show_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="800"
        type="application/pdf">
    </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)


if os.path.exists(resume_path):

    show_pdf(resume_path)

    with open(resume_path, "rb") as pdf:
        st.download_button(
            label="📥 Download Resume",
            data=pdf,
            file_name="Vanshika_Soni_Resume.pdf",
            mime="application/pdf"
        )

else:
    st.error("Resume file not found.")