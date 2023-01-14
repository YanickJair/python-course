import streamlit as st

st.set_page_config(page_title="Conceitos Básicos", page_icon="🚀")

st.markdown(f"# Conceitos Básicos")

concepts = st.sidebar.selectbox(
    "Conceitos",
    ["Olá, Mundo", "Tipos de dados", "Operadores", "Controlo de Fluxo", "Funções", ""],
)


def hello_world():
    from PIL import Image
    st.markdown(
    """ 
        Como em qualquer outra linguagem de programação, vamos começar pelo famoso 'Hello, world', ou 'Olá, mundo'.

        Cria um ficheiro no seu editor de texto prefirido, no meu caso estou a usar o [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=linux),
        podes chamar o ficheiro de 'hello_world.py' e cole o código abaixo.
    """
    )

    st.code(""" 
    print('Olá, mundo!')
    """, language="python")

    st.markdown(""" 
    Para executar o código no Pycharm vai no botão de play como mostra a imagem abaixo e clica 'Run'
    """)
    
    st.image(Image.open("src/images/run_code.png"))


    st.text("Resultado:")
    st.code("Olá, mundo!", language="sh")

    st.markdown("""
        ### Vamos 'dissecar' o nosso código
        
        Na nosso "super-programa" de uma linha de código só, temos uma função, o  **print**.
        **Print** é uma função que recebe como argumento um objecto, no nosso caso um texto "Olá, mundo!" e impremi-o
        para o utilizador.

    """)

concepts_dic = {
    "Olá, Mundo": hello_world
}

concepts_dic[concepts]()