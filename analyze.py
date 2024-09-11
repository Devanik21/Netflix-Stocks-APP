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
def plot_histograms_kde(data, columns):
    if not columns:
        st.warning("Please select at least one column for histograms.")
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
        st.warning("Please select at least one column for KDE plots.")
        return

    st.write(f"Visualizing KDE plots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        sns.kdeplot(data[col], ax=ax, color='green')
        ax.set_title(f'{col} KDE Plot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot scatter matrix
def plot_scatter_matrix(data, columns):
    if not columns or len(columns) < 2:
        st.warning("Please select at least two columns for scatter matrix.")
        return

    st.write(f"Visualizing scatter matrix for the selected columns: {', '.join(columns)}")

    scatter_data = data[columns]
    fig = sns.pairplot(scatter_data, diag_kind='kde')
    st.pyplot(fig)

# Function to plot bar plots
def plot_bar_plots(data, columns):
    if not columns:
        st.warning("Please select at least one column for bar plots.")
        return

    st.write(f"Visualizing bar plots for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        data[col].value_counts().plot(kind='bar', ax=ax, color='purple')
        ax.set_title(f'{col} Bar Plot')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot heatmaps
def plot_heatmaps(data, columns):
    if not columns:
        st.warning("Please select at least one column for heatmaps.")
        return

    st.write(f"Visualizing heatmaps for the selected columns: {', '.join(columns)}")

    num_plots = len(columns)
    fig, axes = plt.subplots(1, num_plots, figsize=(20, 5))
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, columns):
        matrix = pd.crosstab(data[col], data[col])
        sns.heatmap(matrix, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title(f'{col} Heatmap')
        ax.set_xlabel('')
        ax.set_ylabel('')

    st.pyplot(fig)

# Function to plot hexbin plots
def plot_hexbin_plots(data, columns):
    if len(columns) != 2:
        st.warning("Please select exactly two columns for hexbin plots.")
        return

    x_col, y_col = columns
    st.write(f"Visualizing hexbin plot for {x_col} vs {y_col}")

    fig, ax = plt.subplots(figsize=(10, 7))
    hb = ax.hexbin(data[x_col], data[y_col], gridsize=30, cmap='Blues')
    cb = fig.colorbar(hb, ax=ax)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f'Hexbin Plot of {x_col} vs {y_col}')

    st.pyplot(fig)

# Function to plot regression pairs
def plot_regression_pairs(data, columns):
    if len(columns) < 2:
        st.warning("Please select at least two columns for regression pairs.")
        return

    st.write(f"Visualizing regression pairs for the selected columns: {', '.join(columns)}")

    reg_data = data[columns]
    fig = sns.pairplot(reg_data, kind='reg')
    st.pyplot(fig)

# Function to plot swarm plots
def plot_swarm_plots(data, columns):
    if len(columns) != 2:
        st.warning("Please select exactly two columns for swarm plots.")
        return

    x_col, y_col = columns
    st.write(f"Visualizing swarm plot for {x_col} vs {y_col}")

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.swarmplot(data=data, x=x_col, y=y_col, ax=ax, color='orange')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f'Swarm Plot of {x_col} vs {y_col}')

    st.pyplot(fig)

# Main analyze page function
def analyze_page():
    st.title("Analyze Page")
    st.write("This page contains various data visualizations.")

    # Load the data
    data = load_data()

    # User selects columns for each type of plot
    columns = st.multiselect("Select columns for plots", data.select_dtypes(include='number').columns)

    # Display each plot function with user-selected columns
    plot_histograms_kde(data, columns)
    plot_kde_plots(data, columns)
    plot_scatter_matrix(data, columns)
    plot_bar_plots(data, columns)
    plot_heatmaps(data, columns)
    plot_hexbin_plots(data, columns)
    plot_regression_pairs(data, columns)
    plot_swarm_plots(data, columns)

# Run the analyze page
if __name__ == '__main__':
    analyze_page()
