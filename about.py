import streamlit as st

def about_page():
    # Custom CSS
    st.markdown("""
        <style>
        .about-container {
            background-color: #f0f8ff;  /* Light AliceBlue background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .box {
            background-color: #e6f9ff;  /* Light cyan background */
            border-left: 5px solid #00aaff; /* Blue left border */
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .title {
            color: #00aaff; /* Blue color for title */
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .description {
            color: #333333; /* Dark gray text color */
            font-size: 18px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("About Page")

    st.markdown("""
        <div class="about-container">
            <div class="box">
                <p class="title">Application Overview</p>
                <p class="description">This app predicts Netflix stock prices based on user inputs. It provides visualizations and insights to help users understand stock trends and make informed decisions.</p>
            </div>
            <div class="box">
                <p class="title">Developers</p>
                <p class="description">Developed by Devanik, aspiring AI Ops Engineer, and Niki (ChatGPT). We aim to leverage advanced machine learning techniques to provide accurate stock predictions and actionable insights.</p>
            </div>
            <div class="box">
                <p class="title">Contact Information</p>
                <p class="description">For any questions or feedback, please reach out to us through the contact form on our website or via email.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Streamlit App
def main():
    st.title("Data Analysis Dashboard")
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Select Page", ["About"])

    if page == "About":
        about_page()

if __name__ == "__main__":
    main()
