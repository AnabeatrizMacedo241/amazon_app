import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
st.set_page_config(page_title="Books", page_icon=":book:")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set page title and description
st.title("Book Recommendation App")
st.write("Welcome to the Book Recommendation App! This app provides book recommendations in three categories: Sports Analytics, Data Science, and Self Growth and Development.")

# Define objectives
st.header("Objectives")

# Objective 1: Sports Analytics
st.subheader("1. Sports Analytics")
st.write("Provide book recommendations on topics related to Sports Analytics, including mathematical analysis and data-driven insights in sports.")

# Objective 2: Data Science
st.subheader("2. Data Science")
st.write("Offer book recommendations for Data Science enthusiasts, covering various aspects of data analysis, machine learning, and statistical modeling.")

# Objective 3: Self Growth and Development
st.subheader("3. Self Growth and Development")
st.write("Suggest books focused on personal growth, productivity, and self-improvement, helping users in their professional and personal development journeys.")

# Note to user
st.write("Please navigate through the tabs to explore book recommendations in each category.")