import streamlit as st

from frontend.sidebar import render_sidebar

st.set_page_config(
    page_title="Quiz Generator",
    page_icon="Q",
    layout="wide",
    initial_sidebar_state="expanded"
)

difficulty, theme, language = render_sidebar()

st.title("Generate Quiz with GenAI") 