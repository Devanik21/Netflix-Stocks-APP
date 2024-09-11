import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix, andrews_curves, parallel_coordinates

# Function to load data (you can modify this to fit your data source)
def load_data():
    # Load your dataset here
    data = pd.read_csv('NFLX.csv')  # Modify path as necessary
    return data

# Function to generate visualizations
def generate_visualizations(data):
    st.subheader("Scatter Plot")
    scatter_x = st.selectbox("Select X-axis for Scatter Plot", data.columns.tolist())
    scatter_y = st.selectbox("Select Y-axis for Scatter Plot", data.columns.tolist())
    sns.scatterplot(x=data[scatter_x], y=data[scatter_y])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Correlation Heatmap")
    heatmap_cols = st.multiselect("Select columns for Correlation Heatmap", data.columns.tolist(), default=data.columns[:5])
    if heatmap_cols:
        corr = data[heatmap_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        st.pyplot(plt)
        plt.clf()

    st.subheader("Histogram")
    hist_col = st.selectbox("Select column for Histogram", data.columns.tolist())
    sns.histplot(data[hist_col], kde=True, bins=30)
    st.pyplot(plt)
    plt.clf()

    st.subheader("Box Plot")
    box_col = st.selectbox("Select column for Box Plot", data.columns.tolist())
    sns.boxplot(data[box_col])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Line Plot")
    line_col = st.selectbox("Select column for Line Plot", data.columns.tolist())
    sns.lineplot(data=data[line_col])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Pair Plot")
    pair_cols = st.multiselect("Select columns for Pair Plot", data.columns.tolist(), default=data.columns[:3])
    if pair_cols:
        sns.pairplot(data[pair_cols])
        st.pyplot(plt)
        plt.clf()

    st.subheader("Bar Plot")
    bar_x = st.selectbox("Select X-axis for Bar Plot", data.columns.tolist())
    bar_y = st.selectbox("Select Y-axis for Bar Plot", data.columns.tolist())
    sns.barplot(x=data[bar_x], y=data[bar_y])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Ridge Plot")
    ridge_col = st.selectbox("Select column for Ridge Plot", data.columns.tolist())
    sns.kdeplot(data[ridge_col], shade=True)
    st.pyplot(plt)
    plt.clf()

# Streamlit app
def visualize_page():
    st.title("Visualize Data")

    # Load data
    data = load_data()

    if not data.empty:
        st.write(data.head())  # Display first few rows of the dataset
        generate_visualizations(data)  # Generate visualizations
    else:
        st.write("No data available.")

# Run the Streamlit app
if __name__ == "__main__":
    visualize_page()
