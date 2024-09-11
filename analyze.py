import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import andrews_curves

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('NFLX.csv')  # Adjust path as needed
    return data

# Analyze page function
def analyze_page():
    st.title("Data Analysis Page")

    # Load the dataset
    data = load_data()

    # Select only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    
    if numeric_data.empty:
        st.error("No numeric columns available for analysis.")
        return

    st.subheader("Data Overview")
    st.write(numeric_data.head())

    # Show basic statistics
    st.subheader("Basic Statistics")
    st.write(numeric_data.describe())

    # Visualizations
    st.subheader("Data Visualizations")

    # Multiselect to choose columns for visualizations
    selected_cols = st.multiselect("Select columns for visualization", numeric_data.columns.tolist(), default=numeric_data.columns[:2])

    if selected_cols:
        # Pairplot
        st.subheader("Pairplot")
        sns.pairplot(numeric_data[selected_cols])
        st.pyplot(plt)
        plt.clf()

        # Correlation Heatmap
        st.subheader("Correlation Heatmap")
        corr = numeric_data[selected_cols].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        st.pyplot(plt)
        plt.clf()

        # Boxplot
        st.subheader("Boxplot")
        for col in selected_cols:
            sns.boxplot(x=numeric_data[col])
            st.pyplot(plt)
            plt.clf()

        # Violin Plot
        st.subheader("Violin Plot")
        for col in selected_cols:
            sns.violinplot(x=numeric_data[col])
            st.pyplot(plt)
            plt.clf()

        # Ridge Plot
        st.subheader("Ridge Plot")
        for col in selected_cols:
            sns.kdeplot(numeric_data[col], fill=True, common_norm=False, alpha=0.5)
        st.pyplot(plt)
        plt.clf()

        # Andrews Curves (only if more than one column is selected)
        if len(selected_cols) > 1:
            st.subheader("Andrews Curves")
            try:
                andrews_curves(numeric_data[selected_cols].join(data['Date']), 'Date')
                st.pyplot(plt)
            except KeyError:
                st.error("No 'Date' column found in the dataset.")
            plt.clf()

        # Hexbin Plot (for first two selected columns)
        if len(selected_cols) >= 2:
            st.subheader("Hexbin Plot")
            plt.hexbin(numeric_data[selected_cols[0]], numeric_data[selected_cols[1]], gridsize=25, cmap='Blues')
            plt.colorbar(label='count')
            plt.xlabel(selected_cols[0])
            plt.ylabel(selected_cols[1])
            st.pyplot(plt)
            plt.clf()

# Main function to run the app
def main():
    analyze_page()

if __name__ == "__main__":
    main()
