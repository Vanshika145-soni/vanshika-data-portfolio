import streamlit as st

st.set_page_config(
    page_title="Restaurant Intelligence Analytics",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Restaurant Intelligence Analytics")

st.markdown("""
### 📌 Project Overview

Restaurant Intelligence Analytics is an end-to-end analytics project developed to analyze restaurant performance across multiple cities and predict restaurant ratings using Machine Learning.

The project combines data cleaning, exploratory data analysis, predictive modeling, an interactive Streamlit application, and a Power BI dashboard to generate valuable business insights.
""")

st.divider()

# ---------------------------------------------------------

st.header("🎯 Business Problem")

st.write("""
Restaurant owners and food delivery platforms require insights into customer preferences,
pricing strategies, and restaurant performance.

The objective was to analyze restaurant data and build a model capable of predicting restaurant ratings using operational and business attributes.
""")

st.divider()

# ---------------------------------------------------------

st.header("📂 Dataset")

st.write("""
Restaurant datasets were collected from multiple public sources and merged into a master dataset.

Important Features:

- Restaurant Name
- City
- Cuisine
- Price Range
- Online Delivery
- Table Booking
- Votes
- Average Cost
- Rating
""")

st.divider()

# ---------------------------------------------------------

st.header("🧹 Data Cleaning")

st.markdown("""
- Merged multiple datasets
- Removed duplicate restaurants
- Handled missing values
- Standardized column names
- Cleaned categorical values
- Verified data consistency
""")

st.divider()

# ---------------------------------------------------------

st.header("📊 Exploratory Data Analysis")

st.markdown("""
EDA included:

- City-wise Restaurant Distribution
- Cuisine Analysis
- Price Range Distribution
- Rating Distribution
- Online Delivery Analysis
- Cost vs Rating
- Top Rated Cities
- Popular Cuisine Analysis
""")

st.divider()

# ---------------------------------------------------------

st.header("🤖 Machine Learning")

st.write("""
Model Used

✅ Random Forest Classifier

Objective

Predict restaurant ratings using business attributes.
""")

st.markdown("""
Model Evaluation

- Accuracy Score
- Feature Importance
- Prediction Analysis
""")

st.divider()

# ---------------------------------------------------------

st.header("⭐ Important Features")

st.markdown("""
Most influential features:

- Cuisine
- City
- Price Range
- Average Cost
- Online Delivery
- Votes
""")

st.divider()

# ---------------------------------------------------------

st.header("📈 Power BI Dashboard")

st.markdown("""
Dashboard Features

- Total Restaurants
- Average Rating
- Average Price
- City-wise Analysis
- Cuisine Analysis
- Price Segment Analysis
- Map Visualization
- Interactive Filters
""")

st.divider()


st.image(
    "dashboards/restaurant.png",
    caption="Restaurant Intelligence Dashboard",
    use_container_width=True
)

# ---------------------------------------------------------

st.header("💻 Streamlit Web Application")

st.markdown("""
The application consists of two modules.

### Analytics Dashboard

Interactive visualizations

### Rating Predictor

Users enter restaurant information and receive a predicted restaurant rating.
""")

st.divider()

# ---------------------------------------------------------

st.header("📌 Business Insights")

st.markdown("""
✔ Restaurants serving multiple cuisines generally receive higher ratings.

✔ Premium restaurants perform better in metropolitan cities.

✔ Online delivery positively impacts customer ratings.

✔ Customer votes strongly influence restaurant ratings.
""")

st.divider()

# ---------------------------------------------------------

st.header("🛠 Tech Stack")

c1,c2,c3,c4=st.columns(4)

c1.success("Python")
c2.success("Power BI")
c3.success("Machine Learning")
c4.success("Streamlit")

st.divider()

# ---------------------------------------------------------

st.header("🚀 Future Improvements")

st.markdown("""
- Deep Learning Model
- Recommendation System
- Live Restaurant API
- Customer Sentiment Analysis
- Cloud Deployment
""")

st.divider()

st.success("Project Completed Successfully ✅")