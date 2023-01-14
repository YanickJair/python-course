from collections.abc import Callable

import streamlit as st


class MultiPage:
    def __init__(self) -> None:
        """
        :Description
            Constructor class to generate a list which will store
            all our applications as an instance variable
        """
        self.pages = []

    def add_page(self, title: str, func: Callable) -> None:
        """
        :Description
            Class method to add pages to project

        :Args
            title (str): The title of the page we are adding
            func (callable): Python function to render this page in Streamlit
        """
        self.pages.append({"title": title, "function": func})

    def run(self) -> None:
        page = st.sidebar.selectbox(
            "App Navigation", self.pages, format_func=lambda page: page["title"]
        )

        page["function"]()
