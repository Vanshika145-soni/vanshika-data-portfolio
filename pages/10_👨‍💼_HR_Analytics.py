import streamlit as st

st.set_page_config(
    page_title="HR Analytics - Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 HR Analytics: Employee Attrition Prediction")

st.markdown("""
### 📌 Project Overview

The HR Analytics project was developed to help organizations understand employee attrition patterns and predict employees who are at high risk of leaving the company.

The project combines data preprocessing, exploratory data analysis, Machine Learning, SHAP Explainable AI, an interactive Streamlit web application, and a Power BI dashboard to support data-driven HR decision making.
""")

st.divider()

# ---------------------------------------------------------

st.header("🎯 Business Problem")

st.write("""
Employee attrition results in high recruitment costs, productivity loss,
and knowledge gaps within organizations.

The objective of this project is to identify employees who are likely to leave
the organization in advance so HR teams can take proactive retention measures.
""")

st.divider()

# ---------------------------------------------------------

st.header("📂 Dataset")

st.write("""
**Dataset Used**

IBM HR Analytics Employee Attrition Dataset

**Dataset Size**

- 1,470 Employee Records
- 35 Features

Important Features

- Age
- Department
- Job Role
- Monthly Income
- Overtime
- Years at Company
- Job Satisfaction
- Distance From Home
- Education
- Marital Status

Target Variable

Employee Attrition (Yes / No)
""")

st.divider()

# ---------------------------------------------------------

st.header("🧹 Data Cleaning & Feature Engineering")

st.markdown("""
### Data Cleaning

- Removed constant columns
- Encoded categorical variables
- Converted target variable into binary
- Checked missing values
- Removed unnecessary features

### Feature Engineering

Created new business features:

- Age Group
- Salary Band
- Tenure Band
- Overall Satisfaction
- Promotion Risk
- Distance Risk

Handled class imbalance using **SMOTE Oversampling**.
""")

st.divider()

# ---------------------------------------------------------

st.header("📊 Exploratory Data Analysis")

st.markdown("""
EDA Covered

- Age Group Analysis
- Department-wise Attrition
- Job Role Analysis
- Salary Band Analysis
- Overtime Analysis
- Job Satisfaction Analysis
- Promotion History
- Tenure Analysis
- Correlation Heatmap
- Department × Age Group Heatmap
""")

st.divider()

# ---------------------------------------------------------

st.header("🤖 Machine Learning Models")

st.markdown("""
### Models Used

✅ Random Forest Classifier

✅ Logistic Regression

### Model Validation

- 5-Fold Cross Validation
- Accuracy Score
- Precision
- Recall
- F1 Score
- ROC-AUC
""")

st.write("""
**Random Forest Performance**

- Accuracy : 86%
- F1 Score : 0.68
- ROC-AUC : 0.89

**Logistic Regression**

- ROC-AUC : 0.84
""")

st.divider()

# ---------------------------------------------------------

st.header("🧠 Explainable AI (SHAP)")

st.markdown("""
To improve model transparency, SHAP (SHapley Additive Explanations) was implemented.

Generated Explainability Visualizations

- SHAP Summary Plot
- SHAP Beeswarm Plot
- Waterfall Plot
- Individual Prediction Explanation

This allows HR managers to understand why a particular employee is predicted as high-risk.
""")

st.divider()

# ---------------------------------------------------------

st.header("📈 Power BI Dashboard")

st.markdown("""
Dashboard Features

- Total Employees
- Attrition Rate
- Employees Left
- Average Income
- Average Tenure
- Average Satisfaction
- Department-wise Attrition
- Age Group Analysis
- Job Role Analysis
- Attrition Heatmap
- Satisfaction vs Attrition
- Smart Narrative
- Interactive Filters
""")

st.divider()



st.image(
    "dashboards/hr.png",
    caption="HR Analytics Dashboard",
    use_container_width=True
)

# ---------------------------------------------------------

st.header("💻 Streamlit Web Application")

st.markdown("""
The application consists of four modules.

### 📊 Overview

- KPI Cards
- Department Filters
- Employee Summary

### 📈 EDA Dashboard

Interactive Plotly Charts

### 🤖 Attrition Predictor

HR managers enter employee details and receive

- Attrition Prediction
- Risk Probability
- SHAP Explanation
- Retention Recommendation

### 📋 HR Recommendation System

- Replacement Cost Estimator
- Risk Insights
- Employee Retention Strategies
""")

st.divider()

# ---------------------------------------------------------

st.header("📌 Key Business Insights")

st.markdown("""
✔ Sales department showed the highest employee attrition.

✔ Employees working overtime were nearly 2–3 times more likely to leave.

✔ Lower salary bands experienced significantly higher attrition.

✔ Employees with low job satisfaction had greater resignation risk.

✔ Promotion delays increased employee turnover.

✔ SHAP analysis identified Overtime, Monthly Income, Years at Company, and Job Satisfaction as the strongest predictors of attrition.
""")

st.divider()

# ---------------------------------------------------------

st.header("🛠 Tech Stack")

c1, c2, c3, c4 = st.columns(4)

c1.success("Python")
c2.success("Power BI")
c3.success("Machine Learning")
c4.success("Streamlit")

st.divider()

# ---------------------------------------------------------

st.header("📚 Python Libraries Used")

st.markdown("""
- Pandas
- NumPy
- Scikit-learn
- Plotly
- SHAP
- Imbalanced-learn (SMOTE)
- Joblib
- Streamlit
""")

st.divider()

# ---------------------------------------------------------

st.header("🚀 Future Improvements")

st.markdown("""
- XGBoost & LightGBM Models
- Real-Time HR Dashboard
- Employee Retention Score
- Cloud Deployment
- HR Database Integration
- Automated Email Alerts
- Explainable AI Dashboard
""")

st.divider()

st.success("Project Completed Successfully ✅")