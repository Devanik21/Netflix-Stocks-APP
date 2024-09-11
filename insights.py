import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load data
def load_data():
    data = pd.read_csv('NFLX.csv')  # Modify path as necessary
    return data

def insights_page():
    st.title("Insights Page")
    st.write("Welcome to the Insights Page. Here you can find detailed analyses and insights into the data.")

    # Load data
    data = load_data()
    numeric_data = data.select_dtypes(include=[np.number])

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(numeric_data.describe())

    # Histogram of Numeric Columns
    st.subheader("Histogram of Numeric Columns")
    hist_col = st.selectbox("Select column for Histogram", numeric_data.columns.tolist())
    st.write(f"Histogram for {hist_col}")
    fig, ax = plt.subplots()
    sns.histplot(numeric_data[hist_col], kde=True, bins=30, ax=ax)
    st.pyplot(fig)
    plt.clf()

    # Box Plot
    st.subheader("Box Plot")
    box_col = st.selectbox("Select column for Box Plot", numeric_data.columns.tolist())
    st.write(f"Box Plot for {box_col}")
    fig, ax = plt.subplots()
    sns.boxplot(data[numeric_data[box_col]], ax=ax)
    st.pyplot(fig)
    plt.clf()

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    heatmap_cols = st.multiselect("Select columns for Correlation Heatmap", numeric_data.columns.tolist(), default=numeric_data.columns[:5])
    if heatmap_cols:
        st.write(f"Correlation Heatmap for {', '.join(heatmap_cols)}")
        fig, ax = plt.subplots()
        corr = numeric_data[heatmap_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
        plt.clf()

    # Pair Plot
    st.subheader("Pair Plot")
    pair_cols = st.multiselect("Select columns for Pair Plot", numeric_data.columns.tolist(), default=numeric_data.columns[:3])
    if pair_cols:
        st.write(f"Pair Plot for {', '.join(pair_cols)}")
        fig = sns.pairplot(numeric_data[pair_cols])
        st.pyplot(fig)
        plt.clf()

    # Line Plot
    st.subheader("Line Plot")
    line_col = st.selectbox("Select column for Line Plot", numeric_data.columns.tolist())
    st.write(f"Line Plot for {line_col}")
    fig, ax = plt.subplots()
    sns.lineplot(x=numeric_data.index, y=numeric_data[line_col], ax=ax)
    st.pyplot(fig)
    plt.clf()

    # Ridge Plot
    st.subheader("Ridge Plot")
    ridge_col = st.selectbox("Select column for Ridge Plot", numeric_data.columns.tolist())
    st.write(f"Ridge Plot for {ridge_col}")
    fig, ax = plt.subplots()
    sns.kdeplot(numeric_data[ridge_col], shade=True, ax=ax)
    st.pyplot(fig)
    plt.clf()

    # ECDF Plot
    st.subheader("ECDF Plot")
    ecdf_col = st.selectbox("Select column for ECDF Plot", numeric_data.columns.tolist())
    st.write(f"ECDF Plot for {ecdf_col}")
    fig, ax = plt.subplots()
    sns.ecdfplot(numeric_data[ecdf_col], ax=ax)
    st.pyplot(fig)
    plt.clf()

    # Bootstrap Plot
    st.subheader("Bootstrap Plot")
    bootstrap_col = st.selectbox("Select column for Bootstrap Plot", numeric_data.columns.tolist())
    st.write(f"Bootstrap Plot for {bootstrap_col}")
    fig, ax = plt.subplots()
    from seaborn.bootstrap import bootstrap
    bootstrapped = bootstrap(numeric_data[bootstrap_col])
    sns.lineplot(data=bootstrapped, ax=ax)
    st.pyplot(fig)
    plt.clf()

    # Additional Insights
    st.subheader("Additional Insights")
    st.write("Here you can add any additional insights or observations about the data based on the visualizations above.")
    st.write("Consider highlighting key trends, patterns, or anomalies that can be useful for further analysis or decision-making.")

    # User Feedback
    st.subheader("Feedback")
    feedback = st.text_area("Share your feedback or suggestions for this insights page:")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")

# Streamlit App
def main():
    st.title("Data Analysis Dashboard")
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Insights"])

    if page == "Insights":
        insights_page()

if __name__ == "__main__":
    main()
