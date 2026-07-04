import streamlit as st

st.set_page_config(
    page_title="Supply Chain & Inventory Analytics",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Supply Chain & Inventory Analytics")

st.markdown("""
### 📌 Project Overview

Supply Chain & Inventory Analytics is an end-to-end business intelligence project developed using the DataCo Smart Supply Chain dataset.

The project focuses on delivery performance, revenue analysis, inventory monitoring, profitability, and operational efficiency through advanced analytics and interactive dashboards.
""")

st.divider()

# ---------------------------------------------------------

st.header("🎯 Business Problem")

st.write("""
Organizations often face delayed deliveries, inventory inefficiencies,
and profit losses due to poor supply chain visibility.

The objective was to analyze operational data and identify opportunities
to improve logistics performance and business profitability.
""")

st.divider()

# ---------------------------------------------------------

st.header("📂 Dataset")

st.write("""
Dataset Used

DataCo Smart Supply Chain Dataset (Kaggle)

Dataset Size

- 180,000+ Orders
- 53 Columns

Major Features

- Order Details
- Delivery Status
- Product Category
- Customer Segment
- Market
- Region
- Sales
- Profit
""")

st.divider()

# ---------------------------------------------------------

st.header("🧹 Data Cleaning & Feature Engineering")

st.markdown("""
Cleaning

- Removed high-missing columns
- Filled missing numeric values
- Converted date columns
- Renamed columns

Engineered Features

- delay_days
- profit_margin_pct
- is_late
- order_year
- order_month
- revenue_tier
""")

st.divider()

# ---------------------------------------------------------

st.header("📊 Exploratory Data Analysis")

st.markdown("""
EDA Included

- Delivery Performance
- Late Delivery Rate
- Regional Analysis
- Product Profitability
- Customer Segment Analysis
- Monthly Sales Trend
- Revenue Distribution
- Correlation Heatmap
- Department Profit Analysis
""")

st.divider()

# ---------------------------------------------------------

st.header("📈 Power BI Dashboard")

st.markdown("""
Dashboard Features

- Total Orders
- Total Revenue
- Total Profit
- Late Delivery Rate
- Average Delay Days
- Regional Heatmap
- Delivery Status Analysis
- Stockout Risk Monitor
- 30-Day Demand Forecast
""")

st.divider()



st.image(
    "dashboards/Supplychain.png",
    caption="Supply Chain Dashboard",
    use_container_width=True
)

# ---------------------------------------------------------

st.header("📌 Business Insights")

st.markdown("""
✔ Certain regions experience significantly higher delivery delays.

✔ Product profitability varies across departments.

✔ Seasonal demand trends impact inventory planning.

✔ Late deliveries negatively affect overall operational performance.
""")

st.divider()

# ---------------------------------------------------------

st.header("🛠 Tech Stack")

c1,c2,c3,c4=st.columns(4)

c1.success("Python")
c2.success("Power BI")
c3.success("Pandas")
c4.success("Streamlit")

st.divider()

# ---------------------------------------------------------

st.header("🚀 Future Improvements")

st.markdown("""
- Inventory Forecasting Model
- Delay Prediction Model
- Real-Time Supply Chain Dashboard
- Warehouse Optimization
- Live ERP Integration
""")

st.divider()

st.success("Project Completed Successfully ✅")