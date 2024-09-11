import streamlit as st

# Define custom CSS to style the page
st.markdown("""
    <style>
    .main {
        background-color: black;
        color: white;
    }
    .css-1v3fvcr {
        background-color: black;
    }
    .css-1zkmya5 {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def about_page():
    st.title("About Page")
    st.write("This app predicts Netflix stock prices based on user inputs.")
    st.markdown("""
        Developed by Devanik, aspiring AI Ops Engineer, and Niki (ChatGPT).
    """)

    # Add CSS box styling
    st.markdown("""
        <style>
        .info-box {
            border: 2px solid white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            background-color: #333;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="info-box">Welcome to the About Page! Here you can learn more about the app and its creators.</div>', unsafe_allow_html=True)

# Main function to run the app
if __name__ == "__main__":
    about_page()
import streamlit as st

# Define custom CSS to style the page
st.markdown("""
    <style>
    .main {
        background-color: black;
        color: white;
    }
    .css-1v3fvcr {
        background-color: black;
    }
    .css-1zkmya5 {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def about_page():
    st.title("About Page")
    st.write("This app predicts Netflix stock prices based on user inputs.")
    st.markdown("""
        Developed by Devanik, aspiring AI Ops Engineer, and Niki (ChatGPT).
    """)

    # Add CSS box styling
    st.markdown("""
        <style>
        .info-box {
            border: 2px solid white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            background-color: #333;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="info-box">Welcome to the About Page! Here you can learn more about the app and its creators.</div>', unsafe_allow_html=True)

# Main function to run the app
if __name__ == "__main__":
    about_page()
