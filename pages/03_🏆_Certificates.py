import streamlit as st
import os

st.set_page_config(
    page_title="Certificates",
    page_icon="🏆",
    layout="wide"
)

# ---------------- CSS ----------------

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown("# 🏆 Certifications")

st.write(
    """
Professional certifications showcasing continuous learning in
Data Analytics, Python, SQL, Power BI, Machine Learning, Excel,
Business Intelligence and Data Science.
"""
)

st.markdown("---")

# ---------------- CERTIFICATE FOLDER ----------------

CERT_FOLDER = "certificates"

certificates = sorted(os.listdir(CERT_FOLDER))

# ---------------- HELPER ----------------

def issuer(name):

    lower = name.lower()

    if "coursera" in lower:
        return "Coursera"

    elif "google" in lower:
        return "Google"

    elif "microsoft" in lower:
        return "Microsoft"

    elif "ibm" in lower:
        return "IBM"

    elif "udemy" in lower:
        return "Udemy"

    else:
        return "Professional Certificate"

# ---------------- GRID ----------------

cols = st.columns(3)

for i, file in enumerate(certificates):

    file_path = os.path.join(CERT_FOLDER, file)

    title = file.replace(".pdf", "").replace("_", " ")

    with cols[i % 3]:

        st.markdown(
        f"""
<div class="project-card">

<h3>🏆 {title}</h3>

<p><b>Issuer:</b> {issuer(file)}</p>

<p>
This certification validates practical knowledge and
hands-on skills relevant to Data Analytics and Business Intelligence.
</p>

</div>
""",
unsafe_allow_html=True
        )

        with open(file_path, "rb") as pdf:

            st.download_button(
                "📄 View / Download Certificate",
                data=pdf,
                file_name=file,
                mime="application/pdf",
                use_container_width=True,
                key=file
            )

        st.markdown("<br>", unsafe_allow_html=True)