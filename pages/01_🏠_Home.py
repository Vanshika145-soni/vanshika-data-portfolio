import streamlit as st
from PIL import Image



st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)


def load_css():
    with open("css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()



profile = Image.open("assets/profile.png")



st.markdown('<div class="hero-container">', unsafe_allow_html=True)

left, right = st.columns([1,2])

with left:
    st.image(profile, use_container_width=True)

with right:

    st.markdown(
    """
    <div class="hero-box">

    <p style="font-size:22px; margin-bottom:0;">
    Hello, I'm
    </p>

    <div class="hero-title">
    Vanshika Soni
    </div>

    <div class="hero-subtitle">
    Data Analyst | Business Intelligence Enthusiast
    </div>

    <br>

    <div class="hero-text">

    I specialize in transforming raw data into meaningful business insights
    through dashboards, SQL analysis, Python automation, and Machine Learning.

    <br><br>

    📊 Power BI &nbsp;&nbsp;|&nbsp;&nbsp;
    🐍 Python &nbsp;&nbsp;|&nbsp;&nbsp;
    🗄 SQL &nbsp;&nbsp;|&nbsp;&nbsp;
    📈 Excel &nbsp;&nbsp;|&nbsp;&nbsp;
    🤖 Machine Learning

    </div>

    </div>

    """,
    unsafe_allow_html=True
    )

    b1, b2 = st.columns(2)
with b1:
    if st.button("🚀 View Projects", use_container_width=True):
        st.switch_page("pages/04_📂_Projects.py")

with b2:
    if st.button("📄 View Resume", use_container_width=True):
        st.switch_page("pages/05_📄_Resume.py")
        

st.markdown("</div>", unsafe_allow_html=True)


# ==========================
# QUICK STATS
# ==========================

st.markdown("## 📊 Portfolio Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Projects",
        "7+"
    )

with c2:
    st.metric(
        "Dashboards",
        "15+"
    )

with c3:
    st.metric(
        "Certificates",
        "10+"
    )

with c4:
    st.metric(
        "CGPA",
        "3.83"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# WHAT I DO
# =====================================================

st.markdown("## 💼 What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
### 📊 Dashboard Development

Design interactive dashboards using **Power BI** and **Excel** to help businesses
monitor KPIs and make informed decisions.
"""
    )

with col2:
    st.info(
        """
### 🐍 Data Analytics

Analyze datasets using **Python**, **Pandas**, **NumPy**, and **SQL** to uncover
valuable business insights.
"""
    )

with col3:
    st.info(
        """
### 🤖 Machine Learning

Build predictive models for business problems including loan prediction,
customer analysis, and forecasting.
"""
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TECHNICAL SKILLS
# =====================================================

st.markdown("## 💻 Technical Skills")

left, right = st.columns(2)

with left:

    st.success("🐍 Python")

    st.success("🗄 SQL")

    st.success("📊 Power BI")

    st.success("📈 Excel")

    st.success("📦 Pandas")

with right:

    st.success("📉 NumPy")

    st.success("🤖 Machine Learning")

    st.success("📊 Statistics")

    st.success("🎨 Streamlit")

    st.success("📋 Data Visualization")

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# FEATURED PROJECTS
# =====================================================

st.markdown("## 🚀 Featured Projects")

r1c1, r1c2 = st.columns(2)

with r1c1:

    st.info(
        """
### 🏦 Loan Risk Predictor

**Tech Stack**

Python • Machine Learning • Streamlit

✔ Loan Approval Prediction

✔ Classification Model

✔ Business Decision Support
"""
    )

with r1c2:

    st.info(
        """
### 🍽 Restaurant Analytics

**Tech Stack**

Power BI • SQL • Excel

✔ Revenue Analysis

✔ Customer Behaviour

✔ Sales Dashboard
"""
    )

r2c1, r2c2 = st.columns(2)

with r2c1:

    st.info(
        """
### 🏥 Healthcare Dashboard

**Tech Stack**

Power BI • Excel

✔ Patient Analysis

✔ Hospital KPIs

✔ Operational Dashboard
"""
    )

with r2c2:

    st.info(
        """
### 📈 Finance Analytics

**Tech Stack**

Power BI • Python

✔ Financial KPIs

✔ Profit Analysis

✔ Executive Dashboard
"""
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
"""
> 📌 Explore the **Projects** page to view detailed case studies, dashboards, datasets, business problems, and insights.
"""
)


# =====================================================
# CERTIFICATIONS PREVIEW
# =====================================================

st.markdown("---")

st.markdown("## 🏆 Certifications")

st.write(
    """
Continuous learning is an important part of my journey.
I have earned certifications in Data Analytics, SQL, Python,
Power BI, Excel, Machine Learning, and Business Intelligence.
"""
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("Google")

with c2:
    st.success("Microsoft")

with c3:
    st.success("Python")

with c4:
    st.success("Power BI")

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# WHY HIRE ME
# =====================================================

st.markdown("## ⭐ Why Work With Me?")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### ✔ Business Understanding

I focus on solving real-world business problems using
data-driven decision making rather than simply creating dashboards.
""")

    st.markdown("""
### ✔ Analytical Thinking

Strong problem-solving skills with experience in
Python, SQL, Power BI, and Machine Learning.
""")

with col2:

    st.markdown("""
### ✔ Interactive Dashboards

Create professional dashboards that help stakeholders
monitor KPIs and make better business decisions.
""")

    st.markdown("""
### ✔ Continuous Learning

Always exploring new tools, technologies, and
analytics techniques to improve my skills.
""")

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# CALL TO ACTION
# =====================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:25px;">

<h2 style="color:#2563EB;">
Let's Turn Data Into Decisions 📊
</h2>

<p style="font-size:18px;color:#555;">
I'm actively seeking opportunities in
Data Analytics, Business Intelligence,
and Machine Learning where I can contribute,
learn, and grow.
</p>

</div>
""",
unsafe_allow_html=True
)

cta1, cta2 = st.columns(2)

with cta1:
    if st.button("📄 View Resume", key="resume_bottom", use_container_width=True):
        st.switch_page("pages/05_📄_Resume.py")

with cta2:
    if st.button("📧 Contact Me", key="contact_bottom", use_container_width=True):
        st.switch_page("pages/06_📞_Contact.py")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center; padding:20px;">

<h4>Vanshika Soni</h4>

<p>
📊 Data Analyst | Power BI | SQL | Python | Machine Learning
</p>

<p>
Designed & Developed using ❤️ Streamlit
</p>

<p style="color:gray;font-size:14px;">
© 2026 Vanshika Soni. All Rights Reserved.
</p>

</div>
""",
unsafe_allow_html=True
)