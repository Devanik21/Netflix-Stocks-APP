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

    st.subheader("Scatter Plot")
    scatter_x = st.selectbox("Select X-axis for Scatter Plot", numeric_data.columns.tolist())
    scatter_y = st.selectbox("Select Y-axis for Scatter Plot", numeric_data.columns.tolist())
    sns.scatterplot(x=data[scatter_x], y=data[scatter_y])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Correlation Heatmap")
    heatmap_cols = st.multiselect("Select columns for Correlation Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:5])
    if heatmap_cols:
        corr = numeric_data[heatmap_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        st.pyplot(plt)
        plt.clf()

    st.subheader("Histogram")
    hist_col = st.selectbox("Select column for Histogram", numeric_data.columns.tolist())
    sns.histplot(numeric_data[hist_col], kde=True, bins=30)
    st.pyplot(plt)
    plt.clf()

    st.subheader("Box Plot")
    box_col = st.selectbox("Select column for Box Plot", numeric_data.columns.tolist())
    sns.boxplot(numeric_data[box_col])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Line Plot")
    line_col = st.selectbox("Select column for Line Plot", numeric_data.columns.tolist())
    sns.lineplot(data=numeric_data, x=numeric_data.index, y=line_col)
    st.pyplot(plt)
    plt.clf()

    st.subheader("Pair Plot")
    pair_cols = st.multiselect("Select columns for Pair Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if pair_cols:
        sns.pairplot(numeric_data[pair_cols])
        st.pyplot(plt)
        plt.clf()

    st.subheader("Bar Plot")
    bar_x = st.selectbox("Select X-axis for Bar Plot", numeric_data.columns.tolist())
    bar_y = st.selectbox("Select Y-axis for Bar Plot", numeric_data.columns.tolist())
    sns.barplot(x=data[bar_x], y=data[bar_y])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Ridge Plot")
    ridge_col = st.selectbox("Select column for Ridge Plot", numeric_data.columns.tolist())
    sns.kdeplot(numeric_data[ridge_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # Additional 20 plots
    # 1. Distplot
    st.subheader("Distplot")
    distplot_col = st.selectbox("Select column for Distplot", numeric_data.columns.tolist())
    sns.histplot(numeric_data[distplot_col], kde=True)
    st.pyplot(plt)
    plt.clf()

    # 2. Lineplot
    st.subheader("Lineplot")
    lineplot_col = st.selectbox("Select column for Lineplot", numeric_data.columns.tolist())
    sns.lineplot(data=numeric_data, x=numeric_data.index, y=lineplot_col)
    st.pyplot(plt)
    plt.clf()

    # 3. Scatterplot
    st.subheader("Scatterplot")
    scatterplot_cols = st.multiselect("Select two columns for Scatterplot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    if len(scatterplot_cols) == 2:
        sns.scatterplot(x=numeric_data[scatterplot_cols[0]], y=numeric_data[scatterplot_cols[1]])
        st.pyplot(plt)
        plt.clf()

    # 4. Barplot
    st.subheader("Barplot")
    barplot_col = st.selectbox("Select column for Barplot", numeric_data.columns.tolist())
    sns.barplot(x=numeric_data.index, y=numeric_data[barplot_col])
    st.pyplot(plt)
    plt.clf()

    # 5. Histogram


    # 6. KDE Plot
    st.subheader("KDE Plot")
    kde_col = st.selectbox("Select column for KDE Plot", numeric_data.columns.tolist())
    sns.kdeplot(data=numeric_data[kde_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # 7. Autocorrelation Plot
    st.subheader("Autocorrelation Plot")
    autocorr_col = st.selectbox("Select column for Autocorrelation Plot", numeric_data.columns.tolist())
    from pandas.plotting import autocorrelation_plot
    autocorrelation_plot(numeric_data[autocorr_col])
    st.pyplot(plt)
    plt.clf()

    # 8. Lag Plot
    st.subheader("Lag Plot")
    lag_col = st.selectbox("Select column for Lag Plot", numeric_data.columns.tolist())
    from pandas.plotting import lag_plot
    lag_plot(numeric_data[lag_col])
    st.pyplot(plt)
    plt.clf()

    # 9. Parallel Coordinates
    st.subheader("Parallel Coordinates")
    parallel_cols = st.multiselect("Select columns for Parallel Coordinates", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(parallel_cols) > 1:
        parallel_coordinates(numeric_data[parallel_cols], parallel_cols[0])
        st.pyplot(plt)
        plt.clf()

    # 10. RadViz
    st.subheader("RadViz")
    radviz_cols = st.multiselect("Select columns for RadViz", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    from pandas.plotting import radviz
    if len(radviz_cols) > 1:
        radviz(numeric_data[radviz_cols], radviz_cols[0])
        st.pyplot(plt)
        plt.clf()

    # 11. Strip Plot
    st.subheader("Strip Plot")
    strip_col = st.selectbox("Select column for Strip Plot", numeric_data.columns.tolist())
    sns.stripplot(x=numeric_data[strip_col])
    st.pyplot(plt)
    plt.clf()

    # 12. Point Plot
    st.subheader("Point Plot")
    point_col = st.selectbox("Select column for Point Plot", numeric_data.columns.tolist())
    sns.pointplot(x=numeric_data.index, y=numeric_data[point_col])
    st.pyplot(plt)
    plt.clf()

    # 13. Area Plot
    st.subheader("Area Plot")
    area_col = st.selectbox("Select column for Area Plot", numeric_data.columns.tolist())
    plt.fill_between(numeric_data.index, numeric_data[area_col], color="skyblue", alpha=0.4)
    st.pyplot(plt)
    plt.clf()

    # 14. Count Plot
    st.subheader("Count Plot")
    count_col = st.selectbox("Select column for Count Plot", numeric_data.columns.tolist())
    sns.countplot(x=numeric_data[count_col])
    st.pyplot(plt)
    plt.clf()

    # 15. Swarm Plot
    st.subheader("Swarm Plot")
    swarm_col = st.selectbox("Select column for Swarm Plot", numeric_data.columns.tolist())
    sns.swarmplot(x=numeric_data[swarm_col])
    st.pyplot(plt)
    plt.clf()

    # 16. Heatmap (without correlation)
    st.subheader("Heatmap")
    heatmap_cols = st.multiselect("Select columns for Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(heatmap_cols) > 1:
        sns.heatmap(numeric_data[heatmap_cols], cmap="YlGnBu")
        st.pyplot(plt)
        plt.clf()

    # 17. Jointplot
    st.subheader("Jointplot")
    jointplot_cols = st.multiselect("Select two columns for Jointplot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    if len(jointplot_cols) == 2:
        sns.jointplot(x=jointplot_cols[0], y=jointplot_cols[1], data=numeric_data)
        st.pyplot(plt)
        plt.clf()

    # 18. Pair Grid
    st.subheader("Pair Grid")
    pair_grid_cols = st.multiselect("Select columns for Pair Grid", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(pair_grid_cols) > 1:
        grid = sns.PairGrid(numeric_data[pair_grid_cols])
        grid.map_diag(sns.histplot)
        grid.map_offdiag(sns.scatterplot)
        st.pyplot(plt)
        plt.clf()

    # 19. Rug Plot
    st.subheader("Rug Plot")
    rug_col = st.selectbox("Select column for Rug Plot", numeric_data.columns.tolist())
    sns.rugplot(x=numeric_data[rug_col])
    st.pyplot(plt)
    plt.clf()

    # 20. Hexbin Plot
    st.subheader("Hexbin Plot")
    hexbin_x = st.selectbox("Select X-axis for Hexbin Plot", numeric_data.columns.tolist())
    hexbin_y = st.selectbox("Select Y-axis for Hexbin Plot", numeric_data.columns.tolist())
    plt.hexbin(data[hexbin_x], data[hexbin_y], gridsize=30, cmap='Blues')
    plt.colorbar()
    st.pyplot(plt)
    plt.clf()

# Main function to run the app
def visualize_page():
    st.title("Data Visualization")
    data = load_data()
    generate_visualizations(data)
