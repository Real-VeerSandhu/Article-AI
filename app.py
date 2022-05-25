# Main app page (sets up navigation and routing)

import streamlit as st
from multiapp import MultiApp
from components import url_summarize, web_summarize

# Set up MultiApp feature (allows for multiple pages)
app = MultiApp()

st.set_page_config(page_title="Article AI", page_icon="📝", layout='centered', initial_sidebar_state="expanded")

st.markdown("""
# Article AI ◉
Use Natural Language Processing to query articles and **produce brief summaries**
""")

st.markdown('----')

# Other pages
app.add_app("Via Search Term", web_summarize.app)
app.add_app("Via URL", url_summarize.app)

# The main app
app.run()