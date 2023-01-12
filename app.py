import streamlit as st

from src.pages import installation, python_intro

def intro():
    import streamlit as st

    st.write("# Bem vindo ao Python para Iniciantes! 👋")
    st.sidebar.success("Programa de Estudo :point_up:")

    st.markdown(
        """
        Aprenda os conceitos básicos de Python desde a sua introdução,
        como instalar e onde pode ser aplicado com exemplos de projectos
        desde o mais básico ao mais complexo.

        **👈 Selecione os tópicos na nemu do painel** para comçares a aprender!

        ### O que é Python :confused: :question:

        Python é uma Linguagem de Programção de alto nível, criado por [Guido van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) em 1991.
        Hoje, Python é gerido pela [Python Software Foundation](https://www.python.org), que tem como missão promover, proteger e desenvolver ainda mais
        a linguagem.

        #### Mas proqué usar Python :question:
        Boa pergunta. Um dos principais objetivos do [Guido van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) quando criou a linguagem
        foi permitir ao programador ter maior foco em fazer o seu trabalho, desenvolver código, ao invés de focar nas partes computacionais, 
        deixando isso ao encargo do Python.

        Python pode ser aplicadas nas mais diversas áreas tais como:
        - Desenvolvimento Web (essa página foi feita usando [Streamlit](https://streamlit.io/))
        - Intiligência Artificial de Aprendizado de Máquina
        - Ciência de Dados
        - Desenvolvimento de [Aplicativos Desktop](https://docs.python.org/3/library/tkinter.html)
        - etc.

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )




page_names_to_funcs = {
    "—": intro,
    "Introdução ao Python": python_intro,
    "Instalação": installation
}

st.set_page_config(
    page_title="Python Para Iniciantes",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)
demo_name = st.sidebar.selectbox("Conteudos", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()