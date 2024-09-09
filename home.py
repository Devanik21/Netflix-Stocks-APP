import streamlit as st
from PIL import Image

def home_page():
    st.title("Welcome to the Netflix Stock Price Prediction App")

    # Welcome message
    st.markdown("""
    <div style="text-align: center;">
        <h2>📊 Welcome! Predict Netflix Stock Prices with Ease!</h2>
        <p>This app helps you forecast Netflix stock prices based on historical data. Use the navigation to explore various features of the app.</p>
    </div>
    """, unsafe_allow_html=True)


   # st.sidebar.image('gold-bull-backgrounds-graphics-elements-related-financial-sector', 
                 #    caption="Welcome to the Stock Prediction App", 
                #     use_column_width=True)
