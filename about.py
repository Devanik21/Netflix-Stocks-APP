import streamlit as st

def about_page():

    
    # Apply custom CSS
    st.markdown("""
        <style>
            .main {
                background-color: #000000;
                color: #ffffff;
            }
            .container {
                background-color: #2d2d2d;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            .title {
                color: #e0b3ff;
                font-size: 36px;
                font-weight: bold;
            }
            .subheader {
                color: #b3a0ff;
                font-size: 24px;
                font-weight: bold;
            }
            .text {
                color: #ffffff;
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Create layout
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<div class="title">About Page</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">This app predicts Netflix stock prices based on user inputs.</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Developed by Devanik, aspiring AI Ops Engineer, and Niki (ChatGPT).</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
