import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('/mnt/data/NFLX.csv')  # Change this to the correct path if needed
    return data

# Function to display general statistics
def display_statistics(data):
    st.subheader("Data Overview")
    st.write(data.head())
    
    st.subheader("Basic Statistics")
    st.write(data.describe())
    
    st.subheader("Data Types")
    st.write(data.dtypes)

# Function to display visualizations
def display_visualizations(data):
    st.subheader("Data Visualizations")
    
    # User input for column selection
    numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
    
    if numeric_cols:
        selected_cols = st.multiselect("Select numeric columns for analysis:", numeric_cols, default=numeric_cols[:3])
    
        if selected_cols:
            # Pairplot
            st.subheader("Pairplot")
            sns.pairplot(data[selected_cols])
            st.pyplot(plt)
            
            # Correlation Heatmap
            st.subheader("Correlation Heatmap")
            corr = data[selected_cols].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
            st.pyplot(plt)
            
            # Boxplot
            st.subheader("Boxplot")
            for col in selected_cols:
                sns.boxplot(x=data[col])
                st.pyplot(plt)
                plt.clf()

            # Violin Plot
            st.subheader("Violin Plot")
            for col in selected_cols:
                sns.violinplot(x=data[col])
                st.pyplot(plt)
                plt.clf()

            # Ridge Plot
            st.subheader("Ridge Plot")
            for col in selected_cols:
                sns.kdeplot(data[col], fill=True, common_norm=False, alpha=0.5)
            st.pyplot(plt)
            plt.clf()

            # Andrews Curves (if more than one numeric column selected)
            if len(selected_cols) > 1:
                st.subheader("Andrews Curves")
                from pandas.plotting import andrews_curves
                andrews_curves(data[selected_cols].join(data['Date']), 'Date')  # Assuming 'Date' is present
                st.pyplot(plt)
                plt.clf()

            # Hexbin plot for the first two selected columns
            if len(selected_cols) >= 2:
                st.subheader("Hexbin Plot")
                plt.hexbin(data[selected_cols[0]], data[selected_cols[1]], gridsize=25, cmap='Blues')
                st.colorbar(label='count')
                st.xlabel(selected_cols[0])
                st.ylabel(selected_cols[1])
                st.pyplot(plt)
                plt.clf()

def main():
    st.title("Data Analysis App")
    
    # Load data
    data = load_data()
    
    # Display statistics
    display_statistics(data)
    
    # Display visualizations
    display_visualizations(data)

if __name__ == '__main__':
    main()
