import streamlit as st

# Title and Header
st.title("My Streamlit App")
st.header("Streamlit Basics")

# Text and Markdown
st.text("Welcome to the Streamlit app.")
st.markdown("**This is bold text**, _this is italic_, and this is a [link](https://streamlit.io).")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.markdown("Use this for navigation or input.")

# Input widgets
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
rating = st.slider("Rate the app", 0, 5)

# Buttons
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old.")


# File uploader
import pandas as pd
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Display uploaded file
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of the dataset:")
    st.dataframe(data)
