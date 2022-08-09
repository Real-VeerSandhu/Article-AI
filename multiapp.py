"""Framework for running multiple Streamlit applications as a single app. Pre 1.1.0
"""
import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.radio(
        # app = st.sidebar.selectbox(
            'Select Summary Method',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
