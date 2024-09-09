import streamlit as st
import pandas as pd
import joblib

# Load the dataset and model
df = pd.read_csv("NFLX.csv")
model = joblib.load("Netflix Stocks ET.pkl")  # Replace with your model path

def predict_page():
    st.title("Netflix Stock Price Prediction Web App")

    def user_input_features():
        features = {}
        features['Open'] = st.sidebar.slider('Open', 100.0, 5000.0, float(df['Open'].mean()))
        features['High'] = st.sidebar.slider('High', 100.0, 5000.0, float(df['High'].mean()))
        features['Low'] = st.sidebar.slider('Low', 100.0, 5000.0, float(df['Low'].mean()))
        features['Adj Close'] = st.sidebar.slider('Adj Close', 100.0, 5000.0, float(df['Adj Close'].mean()))
        features['Volume'] = st.sidebar.slider('Volume', 100.0, 200000000.0, float(df['Volume'].mean()))
        return pd.DataFrame(features, index=[0])

    input_df = user_input_features()
    st.subheader('User Input Features')
    st.write(input_df)

    prediction = model.predict(input_df)
    st.subheader('Prediction Result')
    st.success(f"📈 The predicted stock price based on the input features is: **{prediction[0]}**")
