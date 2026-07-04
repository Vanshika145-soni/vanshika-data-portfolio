import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Loan Risk Analytics",
    page_icon="🏦",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================

st.markdown(
"""
<div class="hero-container">

<div class="hero-box">

<div class="hero-title">
🏦 Loan Risk Predictor
</div>

<div class="hero-subtitle">
Machine Learning • Banking • Risk Analytics
</div>

<br>

<div class="hero-text">

An end-to-end analytics solution developed to help banks and
financial institutions evaluate loan applications, identify
high-risk customers, and support smarter lending decisions
using Machine Learning, Power BI, SQL, and Streamlit.

</div>

</div>

</div>
""",
unsafe_allow_html=True
)

# =========================
# QUICK PROJECT STATS
# =========================

st.markdown("## 📊 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Dataset",
        "1000+ Records"
    )

with c2:
    st.metric(
        "Model",
        "Random Forest"
    )

with c3:
    st.metric(
        "Accuracy",
        "82%"
    )

with c4:
    st.metric(
        "Dashboard",
        "Power BI"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# PROJECT OVERVIEW
# =========================

st.markdown("## 📌 Project Overview")

st.write(
"""
The **Loan Risk Predictor** is a Business Intelligence and Machine Learning
project designed to predict whether a loan applicant is likely to be a
**Good Risk** or **Bad Risk**.

The solution combines:

- 📊 Interactive Power BI Dashboard
- 🐍 Python Data Analysis
- 🤖 Machine Learning Prediction
- 🗄 SQL-based Data Handling
- 🌐 Streamlit Web Application

to assist financial institutions in making faster and more accurate
loan approval decisions.
"""
)

st.markdown("---")

# =====================================================
# BUSINESS PROBLEM
# =====================================================

st.markdown("## 🎯 Business Problem")

left, right = st.columns([2,1])

with left:

    st.write("""
Financial institutions receive thousands of loan applications every day.

Approving high-risk customers increases the probability of loan defaults,
while rejecting genuine applicants reduces business growth.

The objective of this project is to build a Machine Learning model that
predicts whether an applicant is **Good Risk** or **Bad Risk**, enabling
banks to make smarter, data-driven lending decisions.
""")

with right:

    st.info("""
### 🎯 Objective

✔ Reduce Loan Defaults

✔ Improve Approval Accuracy

✔ Support Decision Making

✔ Automate Risk Prediction
""")

st.markdown("---")

# =====================================================
# DATASET
# =====================================================

st.markdown("## 📂 Dataset")

c1, c2 = st.columns([2,1])

with c1:

    st.write("""
The project uses the **German Credit Risk Dataset**, which contains customer
demographic and financial information used for credit risk assessment.
""")

    st.markdown("""
### Features

- Age
- Job Type
- Housing
- Credit Amount
- Savings Account
- Checking Account
- Employment Status
- Loan Duration
""")

with c2:

    st.success("📄 Dataset")

    st.write("German Credit Risk")

    st.success("🎯 Target")

    st.write("Good Risk / Bad Risk")

    st.success("📊 Type")

    st.write("Classification")

st.markdown("---")

# =====================================================
# DATA PREPROCESSING
# =====================================================

st.markdown("## 🧹 Data Preprocessing")

col1, col2 = st.columns(2)

with col1:

    st.success("✔ Removed Duplicate Records")

    st.success("✔ Missing Value Treatment")

    st.success("✔ Standardized Column Names")

with col2:

    st.success("✔ Encoded Categorical Features")

    st.success("✔ Checked Data Consistency")

    st.success("✔ Feature Engineering")

st.markdown("---")

# =====================================================
# EXPLORATORY DATA ANALYSIS
# =====================================================

st.markdown("## 📊 Exploratory Data Analysis")

st.write(
"""
Several exploratory analyses were performed to understand customer
behavior and identify the major factors affecting loan repayment risk.
"""
)

eda1, eda2 = st.columns(2)

with eda1:

    st.info("""
### Customer Analysis

• Age Distribution

• Job Category

• Housing Type

• Employment Status
""")

    st.info("""
### Financial Analysis

• Credit Amount

• Savings Analysis

• Checking Account

• Loan Duration
""")

with eda2:

    st.info("""
### Risk Analysis

• Good vs Bad Risk

• Default Percentage

• High Risk Segments

• Risk by Age
""")

    st.info("""
### Business Insights

• Loan Trends

• Customer Behaviour

• Financial Patterns

• Risk Indicators
""")

st.markdown("---")

# =====================================================
# MACHINE LEARNING MODEL
# =====================================================

st.markdown("## 🤖 Machine Learning Model")

left, right = st.columns([2,1])

with left:

    st.write("""
The prediction model is built using the **Random Forest Classifier**,
an ensemble learning algorithm known for its robustness, high accuracy,
and ability to handle both numerical and categorical features.

The model predicts whether a customer belongs to the **Good Risk**
or **Bad Risk** category based on their financial profile.
""")

with right:

    st.info("""
### Model

🌲 Random Forest

### Problem

Classification

### Output

Good Risk

Bad Risk
""")

st.markdown("### 📈 Model Evaluation")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("Accuracy Score")

with c2:
    st.success("Confusion Matrix")

with c3:
    st.success("Classification Report")

st.markdown("---")

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

st.markdown("## ⭐ Important Features")

col1, col2 = st.columns(2)

with col1:

    st.success("💰 Credit Amount")

    st.success("💵 Savings")

    st.success("🏠 Housing")

with col2:

    st.success("👤 Age")

    st.success("📅 Loan Duration")

    st.success("💼 Employment")

st.markdown("---")

# =====================================================
# POWER BI DASHBOARD
# =====================================================

st.markdown("## 📊 Power BI Dashboard")

st.write("""
An interactive Power BI dashboard was created to help decision makers
monitor customer risk profiles, financial KPIs, and loan trends.
""")

k1, k2 = st.columns(2)

with k1:

    st.info("""
### Dashboard KPIs

• Total Customers

• Good Risk %

• Bad Risk %

• Average Credit Amount
""")

with k2:

    st.info("""
### Dashboard Analysis

• Age Analysis

• Housing Analysis

• Savings Analysis

• Employment Analysis
""")

st.markdown("### 🖼 Dashboard Preview")

st.image(
    "dashboards/loanrisk.png",
    use_container_width=True
)

st.markdown("---")

# =====================================================
# STREAMLIT APPLICATION
# =====================================================

st.markdown("## 💻 Streamlit Application")

st.write("""
The project was deployed as an interactive Streamlit application,
allowing users to enter applicant details and instantly receive
a loan risk prediction.
""")

s1, s2, s3 = st.columns(3)

with s1:

    st.success("🏠 Home")

    st.caption("Project Overview")

with s2:

    st.success("📊 Analytics")

    st.caption("Interactive Charts")

with s3:

    st.success("🤖 Prediction")

    st.caption("Real-time Loan Prediction")

st.markdown("---")

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

st.markdown("## 📈 Key Business Insights")

st.success("✔ Customers with low savings accounts have a higher probability of default.")

st.success("✔ Higher credit amounts significantly increase lending risk.")

st.success("✔ Housing status strongly influences repayment behaviour.")

st.success("✔ Younger applicants with unstable employment show higher default rates.")

st.success("✔ Data-driven approvals reduce financial risk for banks.")

st.markdown("---")

# =====================================================
# TECH STACK
# =====================================================

st.markdown("## 🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.success("🐍 Python")

with t2:
    st.success("📊 Power BI")

with t3:
    st.success("🗄 SQL")

with t4:
    st.success("🌐 Streamlit")

st.markdown("---")

# =====================================================
# FUTURE IMPROVEMENTS
# =====================================================

st.markdown("## 🚀 Future Scope")

left, right = st.columns(2)

with left:

    st.markdown("""
- ✅ XGBoost Implementation

- ✅ Explainable AI (SHAP)

- ✅ Hyperparameter Tuning

- ✅ Better Feature Engineering
""")

with right:

    st.markdown("""
- ✅ Cloud Deployment

- ✅ Live Database Integration

- ✅ REST API Development

- ✅ Real-time Loan Processing
""")

st.markdown("---")

# =====================================================
# PROJECT SUMMARY
# =====================================================

st.markdown(
"""
<div class="hero-container">

<h2 style="text-align:center;color:#2563EB;">
Project Outcome
</h2>

<p style="text-align:center;font-size:18px;line-height:1.8;">

This project demonstrates the complete Data Analytics workflow,
from data preprocessing and exploratory analysis to Machine Learning,
dashboard development, and deployment using Streamlit.

It showcases practical skills in Python, SQL, Power BI,
Machine Learning, and Business Intelligence for solving
real-world financial problems.

</p>

</div>
""",
unsafe_allow_html=True
)

st.success("🎉 Loan Risk Predictor Project Completed Successfully")