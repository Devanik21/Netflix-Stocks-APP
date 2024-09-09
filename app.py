import streamlit as st
from home import show_home_page
from predict import show_predict_page
from analyze import show_analyze_page
from visualize import show_visualize_page
from insights import show_insights_page
from feedback import show_feedback_page
from about import show_about_page

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "Predict", "Analyze", "Visualize", "Insights", "Feedback", "About"]
selection = st.sidebar.radio("Go to", pages)

# Display the selected page
if selection == "Home":
    show_home_page()
elif selection == "Predict":
    show_predict_page()
elif selection == "Analyze":
    show_analyze_page()
elif selection == "Visualize":
    show_visualize_page()
elif selection == "Insights":
    show_insights_page()
elif selection == "Feedback":
    show_feedback_page()
elif selection == "About":
    show_about_page()
