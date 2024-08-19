import streamlit as st
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv("C:\\imp\\ml JUPYTER\\MY ML PROJECTS(BOOK)\\3.Deep learning\\ANN\\Recreation\\STOCK PREDICTION\\Netflix stock pred APP\\NFLX.csv")

# Load the trained model (adjust the path to where your model is saved)
model = joblib.load("C:\\imp\\ml JUPYTER\\MY ML PROJECTS(BOOK)\\3.Deep learning\\ANN\\Recreation\\STOCK PREDICTION\\Netflix stock pred APP\\Netflix Stocks ET.pkl")  # Replace with your actual model path

# Title of the web app
st.title("Netflix Stock Price Prediction Web App")

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input_features():
    # Create sliders for each numerical feature in the dataset
    features = {}
    features['Open'] = st.sidebar.slider('Open', float(df['Open'].min()), float(df['Open'].max()), float(df['Open'].mean()))
    features['High'] = st.sidebar.slider('High', float(df['High'].min()), float(df['High'].max()), float(df['High'].mean()))
    features['Low'] = st.sidebar.slider('Low', float(df['Low'].min()), float(df['Low'].max()), float(df['Low'].mean()))
    
    # Add Adj Close slider between Low and Volume
    features['Adj Close'] = st.sidebar.slider('Adj Close', float(df['Adj Close'].min()), float(df['Adj Close'].max()), float(df['Adj Close'].mean()))
    
    features['Volume'] = st.sidebar.slider('Volume', float(df['Volume'].min()), float(df['Volume'].max()), float(df['Volume'].mean()))

    

    input_df = pd.DataFrame(features, index=[0])
    return input_df

# Get user input
input_df = user_input_features()

# Display user input
st.subheader('User Input Features')
st.write(input_df)

# Make prediction
prediction = model.predict(input_df)

# Display the prediction result
st.subheader('Prediction Result')

# Customize the prediction message
st.success(f"📈 The predicted stock price based on the input features is: **{prediction[0]}**")

# Optionally, you can add more details or a description below the result
st.markdown("""
<div style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
    <strong>Note:</strong> The prediction is based on the model's analysis of the provided financial indicators.
</div>
""", unsafe_allow_html=True)
