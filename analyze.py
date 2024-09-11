import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample data loading function (replace with your actual data loading code)
@st.cache_data
def load_data():
    # Replace with your actual CSV file path
    return pd.read_csv('NFLX.csv')

# Function to plot pairwise scatter and histograms
def plot_pairwise(data):
    columns = st.multiselect("Select columns for pairwise scatter plots", data.select_dtypes(include='number').columns)
    if not columns or len(columns) < 2:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(num_plots, num_plots, figsize=(20, 20))
    fig.tight_layout(pad=3.0)

    for i, col1 in enumerate(columns):
        for j, col2 in enumerate(columns):
            ax = axes[i, j]
            if col1 == col2:
                sns.histplot(data[col1], kde=True, ax=ax, color='blue')
                ax.set_title(f'{col1} Distribution')
            else:
                sns.scatterplot(data=data, x=col1, y=col2, ax=ax, color='green')
                ax.set_title(f'{col1} vs {col2}')
            ax.set_xlabel('')
            ax.set_ylabel('')
    
    st.pyplot(fig)

# Function to plot histograms for selected columns
def plot_histograms(data):
    columns = st.multiselect("Select columns for histograms", data.select_dtypes(include='number').columns)
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing histograms for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.histplot(data[col], kde=True, ax=ax, color='blue')
        ax.set_title(f'{col} Histogram')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot boxplots for selected columns
def plot_boxplots(data):
    columns = st.multiselect("Select columns for boxplots", data.select_dtypes(include='number').columns)
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing boxplots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.boxplot(data[col], ax=ax, color='purple')
        ax.set_title(f'{col} Boxplot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot violin plots for selected columns
def plot_violin_plots(data):
    columns = st.multiselect("Select columns for violin plots", data.select_dtypes(include='number').columns)
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing violin plots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.violinplot(data[col], ax=ax, color='orange')
        ax.set_title(f'{col} Violin Plot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot correlation heatmap
def plot_correlation_heatmap(data):
    st.write("Visualizing the correlation heatmap.")
    
    # Filter out non-numeric columns
    numeric_data = data.select_dtypes(include='number')
    
    if numeric_data.empty:
        st.warning("No numeric columns available to compute the correlation heatmap.")
        return

    corr = numeric_data.corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')

    st.pyplot(fig)

# Function to plot pair plots
def plot_pair_plots(data):
    columns = st.multiselect("Select columns for pair plots", data.select_dtypes(include='number').columns)
    if not columns:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing pair plots for the selected columns: {', '.join(columns)}")

    pair_data = data[columns]
    fig = sns.pairplot(pair_data, diag_kind='kde')
    st.pyplot(fig)

# Function to plot line plots (if 'Date' column is present)
def plot_line_plots(data):
    if 'Date' not in data.columns:
        st.warning("No 'Date' column found in the dataset.")
        return

    columns = st.multiselect("Select columns for line plots", data.select_dtypes(include='number').columns)
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing line plots for the selected columns: {', '.join(columns)}")

    fig, ax = plt.subplots(figsize=(15, 7))
    for col in columns:
        sns.lineplot(data=data, x='Date', y=col, ax=ax, label=col)
    ax.set_title('Line Plot Over Time')
    ax.legend()

    st.pyplot(fig)

# Main analyze page function
def analyze_page():
    st.title("Analyze Page")
    st.write("This page contains various data visualizations.")

    # Load the data
    data = load_data()

    # Display each plot function with a user-selectable column interface
    plot_pairwise(data)
    plot_histograms(data)
    plot_boxplots(data)
    plot_violin_plots(data)
    plot_correlation_heatmap(data)
    plot_pair_plots(data)
    plot_line_plots(data)

# Run the analyze page
if __name__ == '__main__':
    analyze_page()
