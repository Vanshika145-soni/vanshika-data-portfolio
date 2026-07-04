import streamlit as st
from PIL import Image

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="About Me",
    page_icon="👩‍💻",
    layout="wide"
)

# ==========================================
# LOAD CSS
# ==========================================

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================================
# TITLE
# ==========================================

st.title("👩‍💻 About Me")

st.markdown("---")

# ==========================================
# PROFILE SECTION
# ==========================================

col1, col2 = st.columns([1,2])

with col1:
    st.image(
        "assets/profile.png",
        use_container_width=True
    )

with col2:

    st.markdown("## Vanshika Soni")

    st.markdown("""
### 📊 Aspiring Data Analyst

I am a passionate Data Analytics student with interests in:

- 📊 Data Analytics
- 📈 Business Intelligence
- 🗄 SQL
- 🐍 Python
- 🤖 Machine Learning
- 📊 Power BI

I enjoy transforming raw data into meaningful insights and building
interactive dashboards that help organizations make better decisions.
""")

st.markdown("---")

# ==========================================
# EDUCATION
# ==========================================

st.header("🎓 Education")

st.info("""
MBA Tech

Computer Science & Engineering

NMIMS University

Current CGPA: 3.83
""")

st.markdown("---")

# ==========================================
# SKILLS
# ==========================================

st.header("💻 Technical Skills")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🐍 Python")
    st.success("📦 Pandas")
    st.success("📊 NumPy")

with c2:
    st.success("🗄 SQL")
    st.success("📊 Power BI")
    st.success("📈 Excel")

with c3:
    st.success("🤖 Machine Learning")
    st.success("📉 Statistics")
    st.success("🎨 Streamlit")

st.markdown("---")

# ==========================================
# EXPERIENCE
# ==========================================

st.header("💼 Experience")

st.markdown("""
### 📊 Data Analytics Projects

Worked on multiple end-to-end analytics projects including:

- Loan Risk Analytics
- Restaurant Intelligence Analytics
- HR Analytics
- Supply Chain Analytics
- HealthCare Data Preparation
- Rajasthan Mining Data Preparation
- Finance & Refinance Analytics System 

Projects involved:

- Data Cleaning
- Exploratory Data Analysis
- Dashboard Development
- Machine Learning
- Business Insights Generation
""")

st.markdown("---")

# ==========================================
# ACHIEVEMENTS
# ==========================================

st.header("🏆 Achievements")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", "10+")

with col2:
    st.metric("Certificates", "7+")

with col3:
    st.metric("Dashboards", "10+")

st.markdown("---")

# ==========================================
# CAREER GOAL
# ==========================================

st.header("🎯 Career Goal")

st.write("""
My goal is to build a career in Data Analytics and Business Intelligence,
leveraging data-driven solutions to solve real-world business problems.

I am continuously improving my skills in analytics, visualization,
machine learning, and decision support systems.
""")

st.markdown("---")

# ==========================================
# PERSONAL INTERESTS
# ==========================================

st.header("🌟 Interests")

st.write("""
📊 Data Analytics

📈 Business Intelligence

🤖 Machine Learning

💻 Technology

📚 Continuous Learning

🚀 Building Real-World Projects
""")

st.markdown("---")

st.success("Thank you for visiting my portfolio! 🚀")