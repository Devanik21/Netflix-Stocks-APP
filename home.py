import streamlit as st
from PIL import Image

def home_page():
    st.title("📈 Welcome to the Netflix Stock Price Prediction App")

    # Welcome message with updated styling
    st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 1.2em; color: #555;">Forecast Netflix stock prices using historical data. Explore the app through the sidebar to find various features and insights.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a call-to-action or additional information
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <h3>Get Started:</h3>
        <p style="font-size: 1.1em;">Navigate to the <strong>Predict</strong> page to begin forecasting Netflix stock prices.</p>
    </div>
    """, unsafe_allow_html=True)
