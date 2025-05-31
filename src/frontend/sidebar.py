import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("Quiz Settings")

        # Difficulty Settings
        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"],
            index=1
        )

        # Quiz Thema Settings
        theme = st.text_input(
            "Thema",
            placeholder="Example: History, Programming, Science, etc."
        )

        # Language Settings
        language = st.radio(
            "Language",
            ["Japanese", "English"],
            index=0
        )

        return difficulty, theme, language