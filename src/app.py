import streamlit as st

from frontend.sidebar import render_sidebar
from backend.generate_question import generate_question

st.set_page_config(
    page_title="Quiz Generator",
    page_icon="Q",
    layout="wide",
    initial_sidebar_state="expanded"
)

difficulty, theme, language = render_sidebar()

st.title("Generate Quiz with GenAI") 

if st.button("Generate Question", type="primary"):
    question = generate_question(difficulty, theme, language)
    st.write(question)
    