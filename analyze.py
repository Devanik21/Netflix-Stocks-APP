import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import andrews_curves, parallel_coordinates, radviz, lag_plot, autocorrelation_plot

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('NFLX.csv')  # Adjust path as needed
    return data

# Function to generate various visualizations
def generate_plots(numeric_data):
    # Dropdowns to choose columns for each plot
    selected_pairplot_cols = st.multiselect("Select columns for Pairplot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    selected_boxplot_col = st.selectbox("Select column for Boxplot", numeric_data.columns.tolist())
    selected_violinplot_col = st.selectbox("Select column for Violin Plot", numeric_data.columns.tolist())
    selected_corr_cols = st.multiselect("Select columns for Correlation Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    selected_ridgeplot_col = st.selectbox("Select column for Ridge Plot", numeric_data.columns.tolist())
    selected_andrews_cols = st.multiselect("Select columns for Andrews Curves", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    selected_hexbin_cols = st.multiselect("Select 2 columns for Hexbin Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])

    st.subheader("Pairplot")
    if selected_pairplot_cols:
        sns.pairplot(numeric_data[selected_pairplot_cols])
        st.pyplot(plt)
        plt.clf()

    st.subheader("Boxplot")
    sns.boxplot(x=numeric_data[selected_boxplot_col])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Violin Plot")
    sns.violinplot(x=numeric_data[selected_violinplot_col])
    st.pyplot(plt)
    plt.clf()

    st.subheader("Correlation Heatmap")
    if selected_corr_cols:
        corr = numeric_data[selected_corr_cols].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        st.pyplot(plt)
        plt.clf()

    st.subheader("Ridge Plot")
    sns.kdeplot(numeric_data[selected_ridgeplot_col], fill=True, common_norm=False, alpha=0.5)
    st.pyplot(plt)
    plt.clf()




    st.subheader("Hexbin Plot")
    if len(selected_hexbin_cols) == 2:
        plt.hexbin(numeric_data[selected_hexbin_cols[0]], numeric_data[selected_hexbin_cols[1]], gridsize=25, cmap='Blues')
        plt.colorbar(label='count')
        plt.xlabel(selected_hexbin_cols[0])
        plt.ylabel(selected_hexbin_cols[1])
        st.pyplot(plt)
        plt.clf()

    # Add 20 more numeric plots (user chooses columns)
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
    st.subheader("Histogram")
    hist_col = st.selectbox("Select column for Histogram", numeric_data.columns.tolist())
    plt.hist(numeric_data[hist_col], bins=20, color='blue', alpha=0.7)
    st.pyplot(plt)
    plt.clf()



     st.subheader("Andrews Curves")
     if len(selected_andrews_cols) > 1:
        # Limit the number of unique 'Date' categories in the legend
        unique_dates = data['Date'].unique()[:5]  # Limit to the first 5 unique dates
        filtered_data = numeric_data[selected_andrews_cols].join(data[data['Date'].isin(unique_dates)])
        
        # Plot Andrews Curves with a shortened legend
        plt.figure(figsize=(10, 6))
        andrews_curves(filtered_data, 'Date')
        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1), ncol=1)  # Adjust legend position if needed
        st.pyplot(plt)
        plt.clf()


    # 6. KDE Plot
    st.subheader("KDE Plot")
    kde_col = st.selectbox("Select column for KDE Plot", numeric_data.columns.tolist())
    sns.kdeplot(data=numeric_data[kde_col], shade=True)
    st.pyplot(plt)
    plt.clf()

    # 7. Autocorrelation Plot
    st.subheader("Autocorrelation Plot")
    autocorr_col = st.selectbox("Select column for Autocorrelation Plot", numeric_data.columns.tolist())
    autocorrelation_plot(numeric_data[autocorr_col])
    st.pyplot(plt)
    plt.clf()

    # 8. Lag Plot
    st.subheader("Lag Plot")
    lag_col = st.selectbox("Select column for Lag Plot", numeric_data.columns.tolist())
    lag_plot(numeric_data[lag_col])
    st.pyplot(plt)
    plt.clf()

    # 9. Parallel Coordinates
    st.subheader("Parallel Coordinates")
    parallel_cols = st.multiselect("Select columns for Parallel Coordinates", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    
    if len(parallel_cols) > 1:
        plt.figure(figsize=(10, 6))

        # Limit the number of unique categories for the legend
        unique_values = numeric_data[parallel_cols[0]].unique()[:5]  # Limit to first 5 unique categories
        filtered_data = numeric_data[numeric_data[parallel_cols[0]].isin(unique_values)]
        
        # Plot Parallel Coordinates with reduced legend
        parallel_coordinates(filtered_data, parallel_cols[0])
        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1), ncol=1)  # Adjust legend position if necessary
        st.pyplot(plt)
        plt.clf()

    # 10. RadViz
    st.subheader("RadViz")
    radviz_cols = st.multiselect("Select columns for RadViz", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if len(radviz_cols) > 1:
        radviz(numeric_data[radviz_cols], radviz_cols[0])
        st.pyplot(plt)
        plt.clf()

    # Additional 10 more plots based on numeric data

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

    # 20. Line Plot (advanced)
    st.subheader("Advanced Line Plot")
    adv_line_cols = st.multiselect("Select two columns for advanced Line Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:2])
    if len(adv_line_cols) == 2:
        sns.lineplot(x=adv_line_cols[0], y=adv_line_cols[1], data=numeric_data)
        st.pyplot(plt)
        plt.clf()


# Streamlit app
def analyze_page():
    st.title("Analyze Data (Numeric Columns Only)")
    
    # Load data
    data = load_data()
    
    # Filter numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    
    if not numeric_data.empty:
        st.write(numeric_data.describe())  # Display basic statistics
        generate_plots(numeric_data)  # Generate visualizations
    else:
        st.write("No numeric columns found in the dataset.")

# Run the Streamlit app
if __name__ == "__main__":
    analyze_page()
