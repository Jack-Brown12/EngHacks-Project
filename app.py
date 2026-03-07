import streamlit as st
import pandas as pd


st.set_page_config(
    page_title=" >> Hire Honker <<",
    page_icon="🪿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title(">> Hire Honker <<")

with st.sidebar:
    st.markdown("Upload your files here:")

    #Should only be uploaded once
    uploaded_resume = st.file_uploader("Upload your Resume", type="pdf")

    st.button("Save Resume")

    #Should have to be changed every time
    uploaded_job_desc = st.file_uploader("Upload the job description", type="pdf")

    st.button("Analyze Job")

    if uploaded_resume and not uploaded_job_desc:
        pass

