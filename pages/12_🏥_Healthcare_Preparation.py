import streamlit as st

st.set_page_config(
    page_title="Healthcare Data Preparation",
    page_icon="🏥",
    layout="wide"
)

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🏥 Healthcare Data Preparation")

st.markdown(
"""
### 📌 Project Overview

This project focused on preparing a structured healthcare dataset by integrating
multiple publicly available datasets into a single master dataset suitable for
future analytics and machine learning applications.

The project emphasized data cleaning, standardization, merging, and validation
to ensure consistency and usability.
"""
)

st.divider()

# --------------------------------------------------------

st.header("🎯 Business Objective")

st.write("""
Healthcare data is often distributed across multiple sources.

The objective was to create a unified dataset containing disease information,
symptoms, descriptions, precautions, and medicine details that could later be
used for exploratory analysis, dashboards, and predictive models.
""")

st.divider()

# --------------------------------------------------------

st.header("📂 Datasets Used")

st.markdown("""
The following public healthcare datasets were integrated:

- Disease Symptoms
- Disease Descriptions
- Precautions
- Medicine Details
- Medicine Composition
- Manufacturer Information
""")

st.divider()

# --------------------------------------------------------

st.header("🧹 Data Preparation")

st.markdown("""
The following preprocessing steps were performed:

- Removed duplicate records
- Standardized disease names
- Corrected inconsistent values
- Merged datasets using Disease Name
- Checked missing values
- Validated merged records
""")

st.divider()

# --------------------------------------------------------

st.header("📊 Excel Techniques Applied")

st.markdown("""
During the project, several Excel functions were used:

- IF Statements
- VLOOKUP
- Data Validation
- Conditional Formatting
- Filtering & Sorting
- Data Cleaning
""")

st.divider()

# --------------------------------------------------------

st.header("📸 Dataset Preview")

st.image(
    "dashboards/healthcare.png",
    caption="Healthcare Master Dataset",
    use_container_width=True
)

st.divider()

# --------------------------------------------------------

st.header("⭐ Final Dataset")

st.markdown("""
The final dataset contains:

- Disease Name
- Symptoms
- Description
- Precautions
- Medicine Name
- Composition
- Manufacturer
""")

st.divider()

# --------------------------------------------------------

st.header("📌 Key Learning")

st.markdown("""
✔ Data integration from multiple sources

✔ Dataset standardization

✔ Excel-based validation

✔ Data quality improvement

✔ Preparation of analytics-ready datasets
""")

st.divider()

# --------------------------------------------------------

st.header("🛠 Tech Stack")

c1, c2, c3, c4 = st.columns(4)

c1.success("Excel")
c2.success("Python")
c3.success("Data Cleaning")
c4.success("Data Integration")

st.divider()

# --------------------------------------------------------

st.header("🚀 Future Scope")

st.markdown("""
The prepared dataset can be extended with:

- Exploratory Data Analysis (EDA)
- Disease Prediction Models
- Healthcare Business Insights
- Interactive Streamlit Application
""")

st.divider()

st.success("Healthcare Dataset Preparation Completed ✅")