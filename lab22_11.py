import streamlit as st
import pandas as pd
import numpy as np

#streamlit: h1-h3
st.set_page_config(page_title="Hello") #it must be the first commend

st.title("Welcome to ISOM3400 Evaluator")
#st.text("Objective: Discover whether you will fail the course")
st.write("Objective: Discover whether you will fail the course")
st.markdown('---')
st.header("Requirement Check for the course")
st.subheader("Check List")
st.write("""1. Group Exercise
2. Assignment
3. Final Exam""")
st.markdown('---')
st.subheader("Requirement Check for the Assignment")
st.markdown(
"""
The following list won't indent no matter what I try:
- Item 1
- Item 2
- Item 3
"""
)
