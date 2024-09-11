import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load data
def load_data():
    data = pd.read_csv('NFLX.csv')  # Modify path as necessary
    return data

# Function to generate data analysis
def visualize_page(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    
    st.subheader("Pairwise Plot")
    pair_cols = st.multiselect("Select columns for Pairwise Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(pair_cols) > 1:
        sns.pairplot(numeric_data[pair_cols])
        st.pyplot(plt)
        plt.clf()

    st.subheader("Box Plot")
    box_col = st.selectbox("Select column for Box Plot", numeric_data.columns.tolist())
    sns.boxplot(data[numeric_data[box_col]])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Violin Plot")
    violin_col = st.selectbox("Select column for Violin Plot", numeric_data.columns.tolist())
    sns.violinplot(data[numeric_data[violin_col]])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Correlation Heatmap")
    heatmap_cols = st.multiselect("Select columns for Correlation Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:5])
    if heatmap_cols:
        corr = numeric_data[heatmap_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        st.pyplot(plt)
        plt.clf()

    st.subheader("Line Plot")
    line_col = st.selectbox("Select column for Line Plot", numeric_data.columns.tolist())
    sns.lineplot(data=numeric_data, x=numeric_data.index, y=line_col)
    st.pyplot(plt)
    plt.clf()

    # Additional 10 plots for numeric columns
    # 1. Histogram
    st.subheader("Histogram")
    hist_col = st.selectbox("Select column for Histogram", numeric_data.columns.tolist())
    sns.histplot(numeric_data[hist_col], kde=True, bins=30)
    st.pyplot(plt)
    plt.clf()

    # 2. Pair Grid
    st.subheader("Pair Grid")
    pair_grid_cols = st.multiselect("Select columns for Pair Grid", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(pair_grid_cols) > 1:
        grid = sns.PairGrid(numeric_data[pair_grid_cols])
        grid.map_diag(sns.histplot)
        grid.map_offdiag(sns.scatterplot)
        st.pyplot(plt)
        plt.clf()

    # 3. Swarm Plot
    st.subheader("Swarm Plot")
    swarm_col = st.selectbox("Select column for Swarm Plot", numeric_data.columns.tolist())
    sns.swarmplot(x=numeric_data[swarm_col])
    st.pyplot(plt)
    plt.clf()

    # 4. Bar Plot
    st.subheader("Bar Plot")
    bar_col = st.selectbox("Select column for Bar Plot", numeric_data.columns.tolist())
    sns.barplot(x=numeric_data.index, y=numeric_data[bar_col])
    st.pyplot(plt)
    plt.clf()

    # 5. KDE Plot
    st.subheader("KDE Plot")
    kde_col = st.selectbox("Select column for KDE Plot", numeric_data.columns.tolist())
    sns.kdeplot(data=numeric_data[kde_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # 6. Autocorrelation Plot
    st.subheader("Autocorrelation Plot")
    autocorr_col = st.selectbox("Select column for Autocorrelation Plot", numeric_data.columns.tolist())
    from pandas.plotting import autocorrelation_plot
    autocorrelation_plot(numeric_data[autocorr_col])
    st.pyplot(plt)
    plt.clf()

    # 7. Lag Plot
    st.subheader("Lag Plot")
    lag_col = st.selectbox("Select column for Lag Plot", numeric_data.columns.tolist())
    from pandas.plotting import lag_plot
    lag_plot(numeric_data[lag_col])
    st.pyplot(plt)
    plt.clf()

    # 8. Ridge Plot
    st.subheader("Ridge Plot")
    ridge_col = st.selectbox("Select column for Ridge Plot", numeric_data.columns.tolist())
    sns.kdeplot(numeric_data[ridge_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # 9. Heatmap (without correlation)
    st.subheader("Heatmap")
    heatmap_cols = st.multiselect("Select columns for Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(heatmap_cols) > 1:
        sns.heatmap(numeric_data[heatmap_cols], cmap="YlGnBu")
        st.pyplot(plt)
        plt.clf()

    # 10. Jointplot
    st.subheader("Jointplot")
    jointplot_cols = st.multiselect("Select two columns for Jointplot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    if len(jointplot_cols) == 2:
        sns.jointplot(x=jointplot_cols[0], y=jointplot_cols[1], data=numeric_data)
        st.pyplot(plt)
        plt.clf()

# Main function to run the app
def analyze_page():
    st.title("Data Analysis")
    data = load_data()
    generate_analysis(data)
