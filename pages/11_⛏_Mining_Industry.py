import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Mining Industry Data Compilation",
    page_icon="⛏",
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

st.title("⛏ Mining Industry Data Compilation")

st.markdown(
"""
### 📌 Project Overview

The Mining Industry Data Compilation project focused on creating a structured
dataset of mining companies operating across Rajasthan. The objective was to
collect, verify, clean, and organize industry information that can support
future Business Intelligence dashboards and industrial analytics.

Instead of analyzing an existing dataset, this project involved building the
dataset from scratch through detailed research and manual data compilation.
"""
)

st.markdown("---")

# =====================================================

st.header("🎯 Business Objective")

st.write("""
Mining information is often scattered across multiple online sources,
making it difficult to perform industry analysis.

The objective of this project was to:

- Identify major mining companies operating in Rajasthan.
- Compile industry information into a structured dataset.
- Standardize company and location information.
- Create a clean dataset ready for analytics and dashboard development.
""")

st.markdown("---")

# =====================================================

st.header("🌍 Research Methodology")

st.markdown("""
The dataset was created through extensive research using publicly available
sources.

Research included:

- Company Websites
- Industry Directories
- Government Resources
- Public Business Information
- Online Mining Industry Sources

Each record was manually verified before inclusion in the dataset.
""")

st.markdown("---")

# =====================================================

st.header("📂 Dataset Structure")

st.write("The compiled dataset contains the following information:")

st.markdown("""
- Company Name
- City
- District
- Mineral Type
- Ownership Information
- Industry Category
- Operational Location
""")

st.markdown("---")

# =====================================================

st.header("🧹 Data Cleaning & Standardization")

st.markdown("""
The collected data was carefully cleaned before analysis.

Cleaning steps included:

- Removing duplicate company records
- Standardizing city names
- Correcting inconsistent company names
- Categorizing minerals
- Verifying operational locations
- Organizing data into a structured Excel format
""")

st.markdown("---")

# =====================================================

st.header("🪨 Major Minerals Covered")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🪨 Marble")
    st.success("🪨 Limestone")

with col2:
    st.success("⚒ Zinc")
    st.success("⚒ Lead")

with col3:
    st.success("🥈 Silver")
    st.success("🧱 Gypsum")

st.success("🪨 Rock Phosphate")

st.markdown("---")

# =====================================================

st.header("📍 Major Mining Locations")

st.markdown("""
The research covered mining industries located across Rajasthan, including:

- Udaipur
- Jaipur
- Makrana
- Nagaur
- Bhilwara
- Chittorgarh
- Bikaner
""")

st.markdown("---")

# =====================================================

st.header("📈 Key Findings")

st.markdown("""
✔ Rajasthan hosts a diverse range of mining industries.

✔ Different districts specialize in different mineral resources.

✔ Marble industries are concentrated around Makrana.

✔ Zinc, Lead, and Silver mining are prominent in southern Rajasthan.

✔ A structured dataset significantly improves future analytics and reporting.
""")

st.markdown("---")

# =====================================================

st.header("📸 Dataset Preview")

st.image(
    "dashboards/mining.png",
    caption="Mining Industry Dataset (Excel Preview)",
    use_container_width=True
)

st.info(
"""
📌 The image above represents a preview of the manually compiled Excel dataset
used for future analytics and dashboard development.
"""
)

st.markdown("---")

# =====================================================

st.header("📊 Future Dashboard Opportunities")

st.markdown("""
This dataset can be extended into an interactive Business Intelligence dashboard
including:

- Total Mining Companies KPI
- Mineral-wise Distribution
- District-wise Company Count
- Mining Industry Map
- Company Category Analysis
- Interactive Filters
""")

st.markdown("---")

# =====================================================

st.header("🛠 Skills Demonstrated")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🔍 Industry Research")
    st.success("📑 Data Collection")

with c2:
    st.success("🧹 Data Cleaning")
    st.success("📊 Data Organization")

with c3:
    st.success("📈 Data Preparation")
    st.success("📂 Excel Management")

st.markdown("---")

# =====================================================

st.header("💻 Tech Stack")

a, b, c, d = st.columns(4)

with a:
    st.success("Excel")

with b:
    st.success("Research")

with c:
    st.success("Data Cleaning")

with d:
    st.success("Business Analysis")

st.markdown("---")

# =====================================================

st.header("🚀 Future Improvements")

st.markdown("""
Future enhancements planned for this project include:

- Interactive Power BI Dashboard
- District-wise GIS Mapping
- Mineral Production Analysis
- Company Performance Dashboard
- Automated Data Collection
- SQL Database Integration
""")

st.markdown("---")

st.success("Project Completed Successfully ✅")