import streamlit as st
import pandas as pd

# Set page config and theme
st.set_page_config(page_title="IndiaCity GDP Dashboard", layout="wide")
st.markdown(
    """
    <style>
        div.stApp {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-image: linear-gradient(45deg, #ff99cc, #9933ff);
        }
       
        body {
            background: linear-gradient(120deg, orange, green);
            color: black; /* Optional: Adjust text color for better contrast */
        }
        .stButton>button {
            background-color: orange;
            color: white;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

# Login Page
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state["logged_in"] = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials. Please try again.")

# Project Overview
def project_overview():
    st.title("Project Overview")
    st.image(r"C:\Users\Sofia\Downloads\indiagdp.jpg", caption="IndiaCity GDP Dashboard")
    overview_text = """This project, *IndiaCity GDP: A Visualization of Urban Economic Metrics*, provides 
    detailed insights into the GDP contributions of various cities in India. The dashboard 
    showcases data trends, economic performance, and comparative analytics, aiming to 
    help stakeholders make informed decisions."""
    st.write(overview_text)

# Dashboard Section
def dashboard_section():
    st.title("Dashboard")

    # Overview Page
    st.write("### Overview")
    city_filter = st.selectbox("Select City", ["All", "Mumbai", "Delhi", "Bangalore", "Chennai"])
    st.write(f"Filtered by city: {city_filter}")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWRlNTEyM2MtNDM2Yy00OGZhLTk1M2QtNGVmYzI1YmI5MjA5IiwidCI6ImE3MTA5YzlkLTgzNGUtNDM5YS04MWYxLTU2NDAwZTVmNGE5ZCJ9&pageName=7049d803120135a6816b", height=600, width=1000)

    # Region-wise GDP
    st.write("### Region-wise GDP")
    region_filter = st.radio("Select Region", ["All", "East", "West", "North", "South"])
    st.write(f"Filtered by region: {region_filter}")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWRlNTEyM2MtNDM2Yy00OGZhLTk1M2QtNGVmYzI1YmI5MjA5IiwidCI6ImE3MTA5YzlkLTgzNGUtNDM5YS04MWYxLTU2NDAwZTVmNGE5ZCJ9&pageName=03f96d5b51da8830595a", height=600, width=1000)

    # Sector-wise GDP
    st.write("### Sector-wise GDP")
    st.write("GDP contributions by various economic sectors.")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWRlNTEyM2MtNDM2Yy00OGZhLTk1M2QtNGVmYzI1YmI5MjA5IiwidCI6ImE3MTA5YzlkLTgzNGUtNDM5YS04MWYxLTU2NDAwZTVmNGE5ZCJ9&pageName=d349e9ae5d43b41e6ab1", height=600, width=1000)

    # Year-wise GDP
    st.write("### Year-wise GDP")
    year_filter = st.slider("Select Year", min_value=2000, max_value=2025, value=(2010, 2020))
    st.write(f"Filtered by years: {year_filter[0]} - {year_filter[1]}")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWRlNTEyM2MtNDM2Yy00OGZhLTk1M2QtNGVmYzI1YmI5MjA5IiwidCI6ImE3MTA5YzlkLTgzNGUtNDM5YS04MWYxLTU2NDAwZTVmNGE5ZCJ9&pageName=88cfcba9b89b5ac9a58c", height=600, width=1000)

# Insights Page
def insights_page():
    st.title("Insights")
    st.write("""
    ### Dashboard Features:
    - **Dashboard Overview:** A summary view of India's GDP metrics.
    - **Region-wise GDP:** Dive into GDP data by cities and regions.
    - **Sector-wise GDP:** Analyze contributions from agriculture, industry, and services.
    - **Year-wise GDP:** Track GDP growth trends across different years.
    Use the sidebar to navigate and filter data interactively for detailed analysis.
    """)

# Feedback Page
def feedback_page():
    st.title("Feedback")
    st.text_input("Name")
    st.text_input("Email")
    st.text_area("Comments/Feedback")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# Streamlit App Flow
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
else:
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Project Overview", "Dashboard", "Insights", "Feedback"])

    if page == "Project Overview":
        project_overview()
    elif page == "Dashboard":
        dashboard_section()
    elif page == "Insights":
        insights_page()
    elif page == "Feedback":
        feedback_page()