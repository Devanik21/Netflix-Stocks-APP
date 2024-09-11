import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix, andrews_curves, parallel_coordinates

# Function to load data
def load_data():
    data = pd.read_csv('NFLX.csv')  # Modify path as necessary
    return data

# Function to generate visualizations
def generate_visualizations(data):
    # Ensure that only numeric columns are used where appropriate
    numeric_data = data.select_dtypes(include=[np.number])

    # Scatter Plot
    st.subheader("Scatter Plot")
    scatter_x = st.selectbox("Select X-axis for Scatter Plot", numeric_data.columns.tolist())
    scatter_y = st.selectbox("Select Y-axis for Scatter Plot", numeric_data.columns.tolist())
    sns.scatterplot(x=numeric_data[scatter_x], y=numeric_data[scatter_y])
    st.pyplot(plt)
    plt.clf()

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    heatmap_cols = st.multiselect("Select columns for Correlation Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:5])
    if heatmap_cols:
        corr = numeric_data[heatmap_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        st.pyplot(plt)
        plt.clf()

    # Histogram
    st.subheader("Histogram")
    hist_col = st.selectbox("Select column for Histogram", numeric_data.columns.tolist())
    sns.histplot(numeric_data[hist_col], kde=True, bins=30)
    st.pyplot(plt)
    plt.clf()

    # Box Plot
    st.subheader("Box Plot")
    box_col = st.selectbox("Select column for Box Plot", numeric_data.columns.tolist())
    sns.boxplot(numeric_data[box_col])
    st.pyplot(plt)
    plt.clf()

    # Line Plot
    st.subheader("Line Plot")
    line_col = st.selectbox("Select column for Line Plot", numeric_data.columns.tolist())
    sns.lineplot(x=numeric_data.index, y=numeric_data[line_col])
    st.pyplot(plt)
    plt.clf()

    # Pair Plot
    st.subheader("Pair Plot")
    pair_cols = st.multiselect("Select columns for Pair Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if pair_cols:
        sns.pairplot(numeric_data[pair_cols])
        st.pyplot(plt)
        plt.clf()

    # Bar Plot
    st.subheader("Bar Plot")
    bar_x = st.selectbox("Select X-axis for Bar Plot", numeric_data.columns.tolist())
    bar_y = st.selectbox("Select Y-axis for Bar Plot", numeric_data.columns.tolist())
    sns.barplot(x=numeric_data[bar_x], y=numeric_data[bar_y])
    st.pyplot(plt)
    plt.clf()

    # Ridge Plot
    st.subheader("Ridge Plot")
    ridge_col = st.selectbox("Select column for Ridge Plot", numeric_data.columns.tolist())
    sns.kdeplot(numeric_data[ridge_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # FacetGrid
    st.subheader("FacetGrid")
    facet_col = st.selectbox("Select column for FacetGrid", numeric_data.columns.tolist())
    g = sns.FacetGrid(data, col=facet_col)
    g.map(sns.scatterplot, numeric_data.columns[0], numeric_data.columns[1])
    st.pyplot(plt)
    plt.clf()

    # ECDF Plot
    st.subheader("ECDF Plot")
    ecdf_col = st.selectbox("Select column for ECDF Plot", numeric_data.columns.tolist())
    sns.ecdfplot(numeric_data[ecdf_col])
    st.pyplot(plt)
    plt.clf()

    # Bootstrap Plot
    st.subheader("Bootstrap Plot")
    bootstrap_col = st.selectbox("Select column for Bootstrap Plot", numeric_data.columns.tolist())
    from seaborn.bootstrap import bootstrap
    bootstrapped = bootstrap(numeric_data[bootstrap_col])
    sns.lineplot(data=bootstrapped)
    st.pyplot(plt)
    plt.clf()

    # Additional Plots
    # 1. KDE Plot
    st.subheader("KDE Plot")
    kde_col = st.selectbox("Select column for KDE Plot", numeric_data.columns.tolist())
    sns.kdeplot(data=numeric_data[kde_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # 2. Autocorrelation Plot
    st.subheader("Autocorrelation Plot")
    autocorr_col = st.selectbox("Select column for Autocorrelation Plot", numeric_data.columns.tolist())
    from pandas.plotting import autocorrelation_plot
    autocorrelation_plot(numeric_data[autocorr_col])
    st.pyplot(plt)
    plt.clf()

    # 3. Lag Plot
    st.subheader("Lag Plot")
    lag_col = st.selectbox("Select column for Lag Plot", numeric_data.columns.tolist())
    from pandas.plotting import lag_plot
    lag_plot(numeric_data[lag_col])
    st.pyplot(plt)
    plt.clf()

    # 4. Parallel Coordinates
    st.subheader("Parallel Coordinates")
    parallel_cols = st.multiselect("Select columns for Parallel Coordinates", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(parallel_cols) > 1:
        parallel_coordinates(numeric_data[parallel_cols], parallel_cols[0])
        st.pyplot(plt)
        plt.clf()

    # 5. RadViz
    st.subheader("RadViz")
    radviz_cols = st.multiselect("Select columns for RadViz", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    from pandas.plotting import radviz
    if len(radviz_cols) > 1:
        radviz(numeric_data[radviz_cols], radviz_cols[0])
        st.pyplot(plt)
        plt.clf()

    # 6. Strip Plot
    st.subheader("Strip Plot")
    strip_col = st.selectbox("Select column for Strip Plot", numeric_data.columns.tolist())
    sns.stripplot(x=numeric_data[strip_col])
    st.pyplot(plt)
    plt.clf()

    # 7. Point Plot
    st.subheader("Point Plot")
    point_col = st.selectbox("Select column for Point Plot", numeric_data.columns.tolist())
    sns.pointplot(x=numeric_data.index, y=numeric_data[point_col])
    st.pyplot(plt)
    plt.clf()

    # 8. Area Plot
    st.subheader("Area Plot")
    area_col = st.selectbox("Select column for Area Plot", numeric_data.columns.tolist())
    plt.fill_between(numeric_data.index, numeric_data[area_col], color="skyblue", alpha=0.4)
    st.pyplot(plt)
    plt.clf()

    # 9. Count Plot
    st.subheader("Count Plot")
    count_col = st.selectbox("Select column for Count Plot", numeric_data.columns.tolist())
    sns.countplot(x=numeric_data[count_col])
    st.pyplot(plt)
    plt.clf()

    # 10. Swarm Plot
    st.subheader("Swarm Plot")
    swarm_col = st.selectbox("Select column for Swarm Plot", numeric_data.columns.tolist())
    sns.swarmplot(x=numeric_data[swarm_col])
    st.pyplot(plt)
    plt.clf()

    # 11. Heatmap (without correlation)
    st.subheader("Heatmap")
    heatmap_cols = st.multiselect("Select columns for Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(heatmap_cols) > 1:
        sns.heatmap(numeric_data[heatmap_cols], cmap="YlGnBu")
        st.pyplot(plt)
        plt.clf()

    # 12. Jointplot
    st.subheader("Jointplot")
    jointplot_cols = st.multiselect("Select two columns for Jointplot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    if len(jointplot_cols) == 2:
        sns.jointplot(x=jointplot_cols[0], y=jointplot_cols[1], data=numeric_data)
        st.pyplot(plt)
        plt.clf()

    # 13. Pair Grid
    st.subheader("Pair Grid")
    pair_grid_cols = st.multiselect("Select columns for Pair Grid", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(pair_grid_cols) > 1:
        grid = sns.PairGrid(numeric_data[pair_grid_cols])
        grid.map_diag(sns.histplot)
        grid.map_offdiag(sns.scatterplot)
        st.pyplot(plt)
        plt.clf()

    # 14. Rug Plot
    st.subheader("Rug Plot")
    rug_col = st.selectbox("Select column for Rug Plot", numeric_data.columns.tolist())
    sns.rugplot(x=numeric_data[rug_col])
    st.pyplot(plt)
    plt.clf()

    # 15. Hexbin Plot
    st.subheader("Hexbin Plot")
    hexbin_x = st.selectbox("Select X-axis for Hexbin Plot", numeric_data.columns.tolist())
    hexbin_y = st.selectbox("Select Y-axis for Hexbin Plot", numeric_data.columns.tolist())
    plt.hexbin(numeric_data[hexbin_x], numeric_data[hexbin_y], gridsize=50, cmap='Blues')
    st.pyplot(plt)
    plt.clf()

    # 16. ECDF Plot
    st.subheader("ECDF Plot")
    ecdf_col = st.selectbox("Select column for ECDF Plot", numeric_data.columns.tolist())
    sns.ecdfplot(data=numeric_data[ecdf_col])
    st.pyplot(plt)
    plt.clf()

    # 17. Violin Plot
    st.subheader("Violin Plot")
    violin_col = st.selectbox("Select column for Violin Plot", numeric_data.columns.tolist())
    sns.violinplot(x=numeric_data[violin_col])
    st.pyplot(plt)
    plt.clf()

    # 18. KDE Plot (with multiple columns)
    st.subheader("KDE Plot")
    kde_cols = st.multiselect("Select columns for KDE Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if kde_cols:
        sns.kdeplot(data=numeric_data[kde_cols], common_norm=False)
        st.pyplot(plt)
        plt.clf()

    # 19. Pairwise Relationships
    st.subheader("Pairwise Relationships")
    pairwise_cols = st.multiselect("Select columns for Pairwise Relationships", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(pairwise_cols) > 1:
        sns.pairplot(numeric_data[pairwise_cols])
        st.pyplot(plt)
        plt.clf()

    # 20. Parallel Coordinates Plot
    st.subheader("Parallel Coordinates Plot")
    parallel_cols = st.multiselect("Select columns for Parallel Coordinates Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(parallel_cols) > 1:
        parallel_coordinates(numeric_data[parallel_cols], parallel_cols[0])
        st.pyplot(plt)
        plt.clf()

    # 21. RadViz Plot
    st.subheader("RadViz Plot")
    radviz_cols = st.multiselect("Select columns for RadViz Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(radviz_cols) > 1:
        radviz(numeric_data[radviz_cols], radviz_cols[0])
        st.pyplot(plt)
        plt.clf()

# Streamlit App
def main():
    st.title("Data Visualization Dashboard")
    data = load_data()

    st.sidebar.header("Visualization Settings")
    choice = st.sidebar.selectbox("Choose Visualization Type", [
        "Scatter Plot", "Correlation Heatmap", "Histogram", "Box Plot", "Line Plot",
        "Pair Plot", "Bar Plot", "Ridge Plot", "FacetGrid", "ECDF Plot", "Bootstrap Plot",
        "KDE Plot", "Autocorrelation Plot", "Lag Plot", "Parallel Coordinates", 
        "RadViz", "Strip Plot", "Point Plot", "Area Plot", "Count Plot", "Swarm Plot", 
        "Heatmap", "Jointplot", "Pair Grid", "Rug Plot", "Hexbin Plot", "Violin Plot", 
        "Pairwise Relationships", "Parallel Coordinates Plot", "RadViz Plot"
    ])

    # Call function based on selection
    generate_visualizations(data)

if __name__ == "__main__":
    main()
