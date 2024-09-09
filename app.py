import streamlit as st
from home import home_page
from predict import predict_page
from analyze import analyze_page
from visualize import visualize_page
from insights import insights_page
from feedback import feedback_page
from about import about_page
from PIL import Image

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "Predict", "Analyze", "Visualize", "Insights", "Feedback", "About"]
selection = st.sidebar.radio("Go to", pages)

# Display the selected page
if selection == "Home":
    home_page()
elif selection == "Predict":
    predict_page()
elif selection == "Analyze":
    analyze_page()
elif selection == "Visualize":
    visualize_page()
elif selection == "Insights":
    insights_page()
elif selection == "Feedback":
    feedback_page()
elif selection == "About":
    about_page()

    # Load and display images
image = Image.open("20058538_6197033.jpg")  # Replace with your image path
st.image(image, caption="Welcome to the Stock Prediction App", use_column_width=True)
# Optionally add custom CSS for scrolling
st.markdown("""
    <style>
    .main {
        overflow-y: auto;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)
