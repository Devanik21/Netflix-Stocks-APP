import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load the dataset
df = pd.read_csv("/mnt/data/NFLX.csv")

# Load the trained model (adjust the path to where your model is saved)
model = joblib.load("Netflix Stocks ET.pkl")  # Replace with your actual model path

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "Predict", "Analyze", "Visualize", "Insights", "Feedback", "About"]
selection = st.sidebar.radio("Go to", pages)

# Function to handle user input for predictions
def user_input_features():
    features = {}
    features['Open'] = st.sidebar.slider('Open', 100.0, 5000.0, float(df['Open'].mean()))
    features['High'] = st.sidebar.slider('High', 100.0, 5000.0, float(df['High'].mean()))
    features['Low'] = st.sidebar.slider('Low', 100.0, 5000.0, float(df['Low'].mean()))
    features['Adj Close'] = st.sidebar.slider('Adj Close', 100.0, 5000.0, float(df['Adj Close'].mean()))
    features['Volume'] = st.sidebar.slider('Volume', 100.0, 200000000.0, float(df['Volume'].mean()))
    input_df = pd.DataFrame(features, index=[0])
    return input_df

# Display the selected page
if selection == "Home":
    st.title("Welcome to the Netflix Stock Price Prediction App")
    
    # Welcome message
    st.markdown("""
    <div style="text-align: center;">
        <h2>📊 Welcome! Predict Netflix Stock Prices with Ease!</h2>
        <p>This app helps you forecast Netflix stock prices based on historical data. Use the navigation to explore various features of the app.</p>
    </div>
    """, unsafe_allow_html=True)

    # Load and display images
    image = Image.open("welcome_image.jpg")  # Replace with your image path
    st.image(image, caption="Welcome to the Stock Prediction App", use_column_width=True)

elif selection == "Predict":
    st.title("Netflix Stock Price Prediction Web App")
    
    input_df = user_input_features()
    st.subheader('User Input Features')
    st.write(input_df)

    prediction = model.predict(input_df)
    st.subheader('Prediction Result')
    st.success(f"📈 The predicted stock price based on the input features is: **{prediction[0]}**")

elif selection == "Analyze":
    st.title("Analyze Page")
    st.write("This page will contain data analysis details.")

elif selection == "Visualize":
    st.title("Visualize Page")
    st.write("This page will contain visualizations.")

elif selection == "Insights":
    st.title("Insights Page")
    st.write("This page will contain insights.")

elif selection == "Feedback":
    st.title("Feedback Page")
    st.write("This page will collect feedback from users.")

elif selection == "About":
    st.title("About Page")
    st.write("This app predicts Netflix stock prices based on user inputs.")
    st.markdown("""
        Developed by Devanik, aspiring AI Ops Engineer, and Niki (ChatGPT).
    """)

# Optionally add custom CSS for scrolling
st.markdown("""
    <style>
    .main {
        overflow-y: auto;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)
