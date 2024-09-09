import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data loading function (replace with your actual data loading code)
@st.cache_data
def load_data():
    # Replace with your actual CSV file path
    return pd.read_csv('NFLX.csv')

# Function to plot various visualizations
def plot_visualizations(data, columns):
    if not columns or len(columns) < 2:
        st.warning("Please select at least two columns for visualization.")
        return
    
    st.write(f"Visualizing the selected columns: {', '.join(columns)}")
    
    # Create a grid of subplots
    num_plots = len(columns)
    fig, axes = plt.subplots(num_plots + 4, num_plots + 4, figsize=(20, 20))
    fig.tight_layout(pad=3.0)

    # Plot pairwise visualizations
    for i, col1 in enumerate(columns):
        for j, col2 in enumerate(columns):
            ax = axes[i, j]
            if col1 == col2:
                sns.histplot(data[col1], kde=True, ax=ax, color=sns.color_palette("husl")[i % 8])
                ax.set_title(f'{col1} Distribution')
            else:
                sns.scatterplot(data=data, x=col1, y=col2, ax=ax, color=sns.color_palette("husl")[i % 8])
                ax.set_title(f'{col1} vs {col2}')
            ax.set_xlabel('')
            ax.set_ylabel('')
    
    # Additional Plots
    # Boxplots
    for i, col in enumerate(columns):
        sns.boxplot(data=data[col], ax=axes[num_plots + i, 0], color=sns.color_palette("husl")[i % 8])
        axes[num_plots + i, 0].set_title(f'{col} Boxplot')

    # Violin plots
    for i, col in enumerate(columns):
        sns.violinplot(data=data[col], ax=axes[num_plots + i, 1], color=sns.color_palette("husl")[i % 8])
        axes[num_plots + i, 1].set_title(f'{col} Violin Plot')

    # Heatmap of correlations
    corr_matrix = data[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axes[num_plots, 2], vmin=-1, vmax=1)
    axes[num_plots, 2].set_title('Correlation Heatmap')

    # Line plots (if the data has a time component)
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
        for i, col in enumerate(columns):
            sns.lineplot(data=data, x='Date', y=col, ax=axes[num_plots + 2, i], color=sns.color_palette("husl")[i % 8])
            axes[num_plots + 2, i].set_title(f'{col} Over Time')

    st.pyplot(fig)

def analyze_page():
    st.title("Analyze Page")
    st.write("This page contains various data visualizations.")

    # Load the data
    data = load_data()
    
    # List of numeric columns
    numeric_columns = data.select_dtypes(include='number').columns.tolist()
    
    if len(numeric_columns) < 2:
        st.warning("Not enough numeric columns to visualize.")
        return

    # Multi-select widget for column selection
    selected_columns = st.multiselect("Select columns to visualize", options=numeric_columns, default=numeric_columns[:2])
    
    if selected_columns:
        plot_visualizations(data, selected_columns)
    else:
        st.info("Select columns to generate visualizations.")
