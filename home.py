import streamlit as st
from PIL import Image

def home_page():
    st.title("📈 Welcome to the Netflix Stock Price Prediction App")

    # Welcome message with professional styling
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <p style="font-size: 1.3em; color: #333; line-height: 1.5;">
            Use our app to accurately forecast Netflix stock prices based on historical data. Explore various features through the sidebar to gain valuable insights and predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Add a call-to-action or additional information with polished styling
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <h3 style="font-size: 1.5em; color: #6A0DAD;">Get Started:</h3>
        <p style="font-size: 1.2em; color: #555; line-height: 1.5;">
            Use the <strong>Predict</strong> page to start forecasting Netflix stock prices. Navigate through the sidebar to explore more features and insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

   
