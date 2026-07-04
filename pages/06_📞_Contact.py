import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Contact",
    page_icon="📞",
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

st.title("📬 Let's Connect")

st.write(
"""
I'm always open to discussing **Data Analytics**, **Business Intelligence**,
**Machine Learning**, internships, freelance projects, and full-time opportunities.

Feel free to reach out through any of the platforms below.
"""
)

st.markdown("---")

# ==========================================
# CONTACT CARDS
# ==========================================

c1, c2 = st.columns(2)

with c1:

    st.info(
"""
### 📧 Email

**sonivanshika14@gmail.com**

Preferred mode of communication.
"""
    )

    st.info(
"""
### 📱 Phone

**+91 9928970324**

Available during business hours.
"""
    )

    st.info(
"""
### 📍 Location

**Indore, Madhya Pradesh, India**
"""
    )

with c2:

    st.info(
"""
### 💼 LinkedIn

Connect with me professionally for networking and opportunities.

🔗 https://www.linkedin.com/in/vanshika-soni-b58216328/
"""
    )

    st.info(
"""
### 💻 GitHub

Explore my analytics projects and source code.

🔗 https://github.com/Vanshika145-soni
"""
    )

    st.info(
"""
### 📄 Resume

A downloadable resume is available on the **Resume** page.
"""
    )

st.markdown("---")

# ==========================================
# WHY CONTACT ME
# ==========================================

st.header("🤝 Why Connect?")

a, b, c = st.columns(3)

with a:

    st.success("💼 Internship Opportunities")

    st.write(
        "Open to Data Analyst, Business Analyst and BI internships."
    )

with b:

    st.success("🚀 Freelance Projects")

    st.write(
        "Available for dashboard development and analytics projects."
    )

with c:

    st.success("🤝 Collaboration")

    st.write(
        "Interested in collaborating on analytics and ML projects."
    )

st.markdown("---")

# ==========================================
# MESSAGE FORM
# ==========================================

st.header("💬 Send a Message")

with st.form("contact_form"):

    name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    subject = st.text_input("Subject")

    message = st.text_area(
        "Message",
        height=180
    )

    submit = st.form_submit_button("📨 Send Message")

    if submit:

        if name == "" or email == "" or message == "":

            st.error("Please fill all required fields.")

        else:

            st.success(
                f"Thank you {name}! Your message has been received. (Demo Portfolio)"
            )

st.markdown("---")

# ==========================================
# CURRENT STATUS
# ==========================================

st.header("📈 Current Availability")

st.success("✅ Available for Internships")

st.success("✅ Open to Full-Time Opportunities")

st.success("✅ Open for Freelance Analytics Projects")

st.success("✅ Available for Collaboration")

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.markdown(
"""
<div style="text-align:center;padding:20px;">

<h3>Let's Build Something Amazing Together 🚀</h3>

<p>
Thank you for taking the time to explore my portfolio.
I look forward to connecting with you.
</p>

</div>
""",
unsafe_allow_html=True
)