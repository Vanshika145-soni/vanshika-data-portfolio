import streamlit as st
from PIL import Image

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Projects",
    page_icon="📂",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================

st.title("🚀 Analytics Projects")

st.write(
    "A collection of real-world Data Analytics, Business Intelligence, Machine Learning, and Dashboarding projects."
)

st.markdown("---")

# =====================================================
# PROJECT LIST
# =====================================================

projects = [

    {
        "title": "Loan Risk Predictor",
        "category": "Machine Learning",
        "image": "dashboards/loanrisk.png",
        "desc": "Predict loan approval using Machine Learning based on applicant financial information.",
        "tools": ["Python", "SQL", "Machine Learning", "Streamlit"],
        "skills": "EDA • Classification • Feature Engineering",
        "page": "pages/07_🏦_Loan_Risk.py"
    },

    {
        "title": "Restaurant Intelligence Analytics",
        "category": "Power BI",
        "image": "dashboards/restaurant.png",
        "desc": "Restaurant rating prediction and interactive business intelligence dashboard.",
        "tools": ["Python", "Power BI", "Machine Learning"],
        "skills": "Visualization • Prediction • Dashboard",
        "page": "pages/08_🍽_Restaurant.py"
    },

    {
        "title": "Supply Chain Analytics",
        "category": "Power BI",
        "image": "dashboards/Supplychain.png",
        "desc": "Supply Chain & Inventory analytics dashboard for business monitoring.",
        "tools": ["Python", "Power BI"],
        "skills": "Inventory • KPI • Analytics",
        "page": "pages/09_📦_Supply_Chain.py"
    },

    {
        "title": "HR Analytics",
        "category": "Machine Learning",
        "image": "dashboards/hr.png",
        "desc": "Employee attrition prediction using Machine Learning and Power BI.",
        "tools": ["Python", "Power BI", "Machine Learning"],
        "skills": "Classification • HR Analytics",
        "page": "pages/10_👨‍💼_HR_Analytics.py"
    },
   {
        "title":"Mining Industry Data Compilation",
         "image":"dashboards/mining.png",
         "desc":"Compiled and cleaned a structured dataset of mining industries across Rajasthan for future analytics and dashboard development.",
         "tools":["Excel","Data Collection","Data Cleaning","Research"],
         "skills":"Data Collection • Data Cleaning • Industry Research",
        "page":"pages/11_⛏_Mining_Industry.py"
    },

    {
        "title": "Healthcare Data Preparation",
        "category": "Data Preparation",
        "image": "dashboards/Healthcare.png",
        "desc": "Built a unified healthcare dataset by integrating multiple healthcare datasets using data cleaning, standardization, merging, and Excel validation.",
        "tools": ["Excel", "Python", "Data Cleaning", "Data Integration"],
        "skills": "Data Cleaning • Data Integration • Excel",
        "page": "pages/12_🏥_Healthcare_Preparation.py"
    }

]

# =====================================================
# FILTER
# =====================================================

st.subheader("🔍 Filter Projects")

category = st.selectbox(
    "Select Category",
    [
        "All",
        "Machine Learning",
        "Power BI"
    ]
)

st.markdown("---")

# =====================================================
# DISPLAY PROJECTS
# =====================================================

for project in projects:

    if category != "All" and project["category"] != category:
        continue

    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    st.image(
        Image.open(project["image"]),
        use_container_width=True
    )

    st.markdown(
        f'<div class="project-title">{project["title"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="project-desc">{project["desc"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown("#### 🛠 Tech Stack")

    badges = ""

    for tool in project["tools"]:
        badges += f'<span class="tech-badge">{tool}</span>'

    st.markdown(
        badges,
        unsafe_allow_html=True
    )

    st.markdown("")

    st.markdown(
        f"**🎯 Skills:** {project['skills']}"
    )

    st.markdown("")

    if st.button(
        "📖 View Project",
        key=project["title"]
    ):
        st.switch_page(project["page"])

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)