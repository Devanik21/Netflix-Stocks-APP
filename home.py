import streamlit as st
from PIL import Image

def home_page():
    st.title("📈 Welcome to the Netflix Stock Price Prediction App")

    # Welcome message with styling
    st.markdown("""
    <div style="text-align: center;">
        <h2>📊 Predict Netflix Stock Prices with Ease!</h2>
        <p style="font-size: 1.2em; color: #555;">This app allows you to forecast Netflix stock prices based on historical data. Navigate through the app to explore its features and insights.</p>
    </div>
    """, unsafe_allow_html=True)
    

    # Add a call-to-action or additional information
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <h3>Get Started:</h3>
        <p style="font-size: 1.1em;">Use the sidebar to navigate to different sections of the app. Start with the <strong>Predict</strong> page to make predictions on Netflix stock prices based on historical data.</p>
    </div>
    """, unsafe_allow_html=True)
