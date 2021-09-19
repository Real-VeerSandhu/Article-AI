# Main app page (sets up navigation and routing)

import streamlit as st
from multiapp import MultiApp
from components import summarize, web_search

# Set up MultiApp feature (allows for multiple pages)
app = MultiApp()

st.set_page_config(page_title="Diplomatica Summarization AI", page_icon="⬛", layout='centered', initial_sidebar_state="collapsed")

st.markdown("""
# Diplomatica Summarization AI
Use our Natural Language Processing algorithms to obtain articles and **produce brief summaries**
""")

st.markdown('<button style="border-color: black; border-radius: 10;" ><a style="-webkit-appearance: button; -moz-appearance: button; appearance: button; text-decoration: none; color: initial;" href="https://diplomatica.vercel.app/dashboard" target="_blank">Return to Dashboard</a></button>', unsafe_allow_html=True)

# Other pages
app.add_app("Article Summary via Search", web_search.app)
app.add_app("Article Summary via URL", summarize.app)

# The main app
app.run()