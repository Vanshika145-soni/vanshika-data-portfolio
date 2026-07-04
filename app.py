import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Vanshika Soni | Data Analytics Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# LOAD CSS
# -------------------------------------------------

def load_css():
    with open("css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.image("assets/profile.png", width=170)

    st.markdown(
        """
        <div style="text-align:center;">

        <h2 style="margin-bottom:0;">
        Vanshika Soni
        </h2>

        <p style="color:#2563EB;font-size:17px;font-weight:600;">
        Data Analyst
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 👩‍💻 About")

    st.write(
        """
Passionate about transforming raw data into meaningful
business insights using Analytics, Business Intelligence,
SQL, Python, Power BI and Machine Learning.
"""
    )

    st.markdown("---")

    st.markdown("### 🛠 Tech Stack")

    st.markdown("""
- 🐍 Python
- 🗄 SQL
- 📊 Power BI
- 📈 Excel
- 🤖 Machine Learning
- 📉 Statistics
- 📦 Pandas
- 🔢 NumPy
- 🎨 Streamlit
""")

    st.markdown("---")

    st.markdown("### 📍 Location")

    st.write("Indore, Madhya Pradesh")

    st.markdown("### 📧 Email")

    st.write("sonivanshika14@gmail.com")

    st.markdown("---")

    st.markdown("### 🌐 Connect")

    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/vanshika-soni-b58216328/)")

    st.markdown("[💻 GitHub](https://github.com/Vanshika145-soni)")

    st.markdown("---")

    st.caption("© 2026 Vanshika Soni")

# -------------------------------------------------
# MAIN PAGE
# -------------------------------------------------

st.title("👋 Welcome")

st.write(
"""
Welcome to my **Data Analytics Portfolio**.

Use the navigation menu on the left to explore:

- 🏠 Home
- 👩 About
- 🏆 Certifications
- 📄 Resume
- 📞 Contact
- 🚀 Projects

This portfolio showcases my work in **Data Analytics, Business Intelligence, Machine Learning, SQL, Python, Power BI, Excel and Streamlit**.
"""
)

st.info("👈 Select a page from the sidebar to explore my portfolio.")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Projects", "8+")
c2.metric("Dashboards", "15+")
c3.metric("Certificates", "10+")
c4.metric("CGPA", "3.83")

st.markdown("---")

st.markdown(
"""
<div class="footer">

<b>Designed & Developed by Vanshika Soni</b>

<br><br>

Python • SQL • Power BI • Machine Learning • Streamlit

</div>
""",
unsafe_allow_html=True
)