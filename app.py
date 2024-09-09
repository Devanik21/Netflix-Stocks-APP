import streamlit as st
from home import home_page
from predict import predict_page
from analyze import analyze_page
from visualize import visualize_page
from insights import insights_page
from feedback import feedback_page
from about import about_page
from PIL import Image
    # Load and display an image with enhanced styling
image = Image.open("gold.jpg")  # Replace with your image path
st.sidebar.image(image, use_column_width=True)

# Custom CSS to style the app
st.markdown("""
    <style>
    /* Overall background color */
    .reportview-container {
        background-color: #F0F2F6;
    }
    
    /* Sidebar styles */
    .sidebar .sidebar-content {
        background-color: #F4E5FF;
        color: #6A0DAD;
    }
    
    /* Sidebar titles color */
    .sidebar .sidebar-content h1 {
        color: #6A0DAD;
    }

    /* Navigation selectbox styling */
    .stSelectbox > div:first-child {
        background-color: #D5A6E6;
        border-radius: 10px;
        padding: 10px;
    }

    /* Main app title styling */
    .main h1 {
        color: #6A0DAD;
        font-size: 3em;
        text-align: center;
    }

    /* Image styling */
    .main img {
        border: 2px solid #6A0DAD;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }

    /* Adjust padding and alignment */
    .main {
        padding: 20px;
    }

    /* Custom scrollbar */
    .main::-webkit-scrollbar {
        width: 10px;
    }

    .main::-webkit-scrollbar-thumb {
        background: #6A0DAD;
        border-radius: 10px;
    }

    .main::-webkit-scrollbar-track {
        background: #F0F2F6;
    }

    /* Style for headers in main content */
    .main h2, .main h3 {
        color: #6A0DAD;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title(" Navigation")

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
        height: calc(100vh - 60px); /* Adjust height to fit the viewport */
    }
    </style>
    """, unsafe_allow_html=True)
