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
def plot_pairwise(data, columns):
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
def plot_histograms(data, columns):
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
def plot_boxplots(data, columns):
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
def plot_violin_plots(data, columns):
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
def plot_pair_plots(data, columns):
    if not columns:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing pair plots for the selected columns: {', '.join(columns)}")

    pair_data = data[columns]
    fig = sns.pairplot(pair_data, diag_kind='kde')
    st.pyplot(fig)

# Function to plot line plots (if 'Date' column is present)
def plot_line_plots(data, columns):
    if 'Date' not in data.columns:
        st.warning("No 'Date' column found in the dataset.")
        return

    st.write(f"Visualizing line plots for the selected columns: {', '.join(columns)}")

    fig, ax = plt.subplots(figsize=(15, 7))
    for col in columns:
        sns.lineplot(data=data, x='Date', y=col, ax=ax, label=col)
    ax.set_title('Line Plot Over Time')
    ax.legend()

    st.pyplot(fig)

# Function to plot histograms with KDE
def plot_histograms_kde(data, columns):
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing histograms with KDE for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.histplot(data[col], kde=True, ax=ax, color='blue')
        ax.set_title(f'{col} Histogram with KDE')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot KDE plots
def plot_kde_plots(data, columns):
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing KDE plots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.kdeplot(data[col], ax=ax, color='red')
        ax.set_title(f'{col} KDE Plot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot scatter matrix
def plot_scatter_matrix(data, columns):
    if not columns:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing scatter matrix for the selected columns: {', '.join(columns)}")

    scatter_data = data[columns]
    fig = sns.pairplot(scatter_data, hue=None)
    st.pyplot(fig)

# Function to plot bar plots
def plot_bar_plots(data, columns):
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing bar plots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        data[col].value_counts().plot(kind='bar', ax=ax, color='cyan')
        ax.set_title(f'{col} Bar Plot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot heatmaps for numeric columns
def plot_heatmaps(data, columns):
    if not columns:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing heatmaps for the selected columns: {', '.join(columns)}")

    fig, axes = plt.subplots(len(columns), len(columns), figsize=(20, 20))
    for i, col1 in enumerate(columns):
        for j, col2 in enumerate(columns):
            ax = axes[i, j]
            if col1 == col2:
                sns.heatmap(data[[col1]].corr(), annot=True, cmap='viridis', ax=ax)
                ax.set_title(f'{col1} Heatmap')
            else:
                sns.heatmap(data[[col1, col2]].corr(), annot=True, cmap='viridis', ax=ax)
                ax.set_title(f'{col1} vs {col2}')
            ax.set_xlabel('')
            ax.set_ylabel('')

    st.pyplot(fig)

def plot_hexbin_plots(data, columns):
    if not columns or len(columns) < 2:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing hexbin plots for the selected columns: {', '.join(columns)}")

    fig, ax = plt.subplots(figsize=(10, 8))
    hb = ax.hexbin(data[columns[0]], data[columns[1]], gridsize=50, cmap='inferno')
    cb = plt.colorbar(hb, ax=ax)
    cb.set_label('Count')
    ax.set_title(f'Hexbin plot of {columns[0]} vs {columns[1]}')

    st.pyplot(fig)


# Function to plot pairwise comparisons with regression
def plot_regression_pairs(data, columns):
    if not columns or len(columns) < 2:
        st.warning("Please select at least two columns for visualization.")
        return

    st.write(f"Visualizing pairwise regression for the selected columns: {', '.join(columns)}")

    pair_data = data[columns]
    fig = sns.pairplot(pair_data, kind='reg', diag_kind='kde')
    st.pyplot(fig)

# Function to plot swarm plots
def plot_swarm_plots(data, columns):
    if not columns:
        st.warning("Please select at least one column for visualization.")
        return

    st.write(f"Visualizing swarm plots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.swarmplot(data[col], ax=ax, color='brown')
        ax.set_title(f'{col} Swarm Plot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

def plot_ridge_plot(data, column, category):
    st.write(f"Visualizing ridge plot for {column} by {category}.")
    
    # Ensure the category column is in the dataset
    if category not in data.columns:
        st.warning(f"Category column '{category}' not found in the dataset.")
        return
    
    # Ridge plot uses a categorical variable to create overlapping density plots
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, x=column, hue=category, multiple='stack')
    plt.title(f'Ridge Plot of {column} by {category}')
    
    st.pyplot()

# Main analyze page function
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
        plot_pairwise(data, selected_columns)
        plot_histograms(data, selected_columns)
        plot_boxplots(data, selected_columns)
        plot_violin_plots(data, selected_columns)
        plot_correlation_heatmap(data)
        plot_pair_plots(data, selected_columns)
        plot_line_plots(data, selected_columns)
        plot_histograms_kde(data, selected_columns)
        plot_kde_plots(data, selected_columns)
        plot_scatter_matrix(data, selected_columns)
        plot_bar_plots(data, selected_columns)
        plot_heatmaps(data, selected_columns)
        plot_hexbin_plots(data, selected_columns)
        plot_regression_pairs(data, selected_columns)
        plot_swarm_plots(data, selected_columns)
    else:
        st.info("Select columns to generate visualizations.")
