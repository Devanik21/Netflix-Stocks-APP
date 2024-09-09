import streamlit as st
from home import home_page
from predict import predict_page
from analyze import analyze_page
from visualize import visualize_page
from insights import insights_page
from feedback import feedback_page
from about import about_page
from PIL import Image

# Custom CSS to style the app
st.markdown("""
    <style>
    /* Add background color */
    .reportview-container {
        background-color: #F0F2F6;
    }
    
    /* Style sidebar */
    .sidebar .sidebar-content {
        background-color: #F4E5FF;
        color: #6A0DAD;
    }
    
    /* Change the color of sidebar titles */
    .sidebar .sidebar-content h1 {
        color: #6A0DAD;
    }

    /* Style for navigation selectbox */
    .stSelectbox > div:first-child {
        background-color: #D5A6E6;
        border-radius: 10px;
        padding: 10px;
    }

    /* Style the main app title */
    .main h1 {
        color: #6A0DAD;
        font-size: 3em;
    }

    /* Style for images */
    .main img {
        border: 2px solid #6A0DAD;
        border-radius: 10px;
    }

    /* General padding and alignment adjustments */
    .main {
        padding: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("🚀 Navigation")

# Use st.selectbox to create a scrollable dropdown menu for navigation
pages = ["🏠 Home", "📈 Predict", "🔍 Analyze", "📊 Visualize", "💡 Insights", "📝 Feedback", "📚 About"]
selection = st.sidebar.selectbox("Go to", pages)  # This makes the sidebar scrollable

# Display the selected page
if selection == "🏠 Home":
    home_page()
elif selection == "📈 Predict":
    predict_page()
elif selection == "🔍 Analyze":
    analyze_page()
elif selection == "📊 Visualize":
    visualize_page()
elif selection == "💡 Insights":
    insights_page()
elif selection == "📝 Feedback":
    feedback_page()
elif selection == "📚 About":
    about_page()

# Load and display images with borders and improved captions
image = Image.open("20058538_6197033.jpg")  # Replace with your image path
st.image(image, caption="✨ Welcome to the Netflix Stock Prediction App! ✨", use_column_width=True)

# Optionally add custom CSS for scrolling
st.markdown("""
    <style>
    .main {
        overflow-y: auto;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)
