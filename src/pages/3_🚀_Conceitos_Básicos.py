import streamlit as st

from topics import data_types

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

    st.code(
        """ 
    print('Olá, mundo!')
    """,
        language="python",
    )

    st.markdown(
        """ 
    Para executar o código no Pycharm vai no botão de play como mostra a imagem abaixo e clica 'Run'
    """
    )

    st.image(Image.open("src/images/run_code.png"))

    st.text("Resultado:")
    st.code(":> Olá, mundo!", language="sh")

    st.markdown(
        """
        ### Vamos 'dissecar' o nosso código
        
        Na nosso "super-programa" de uma linha de código só, temos uma função, o  **print**.
        **Print** é uma função que recebe como argumento um objecto, no nosso caso um texto "Olá, mundo!" e impremi-o
        para o utilizador.

        Podemos inclusive passar números para a nossa função **print** ou fazer operações
        artiméticas e impremir logo o resultado. Vejamos:\n\n
    """
    )

    st.code(
        """ 
    print(3 + 2)
    """
    )
    st.text("Resultado:")
    st.code(":> 5", language="sh")

    st.markdown("***")

    st.markdown("Próximo vamos ver os **Tipos de Dados** em mais detalhes.\n")


def __data_types():
    st.markdown(
        """ 
        Aqui vamos falar sobre os tipos de dados ou **Data Types** básicos no Python.
        Tipos de dados, como o próprio nome diz, representa to tipo de valor que
        pretendemos guardar ou processar, e cada tipo de dado no Python é um objeto
        e cada objeto permite-nos fazer um conjunto de operações.

        Cada tipo de dados em Python tem a sua própria especificidade e o Python faz
        a gestão da memória de acordo com o tipo de dados estás a criar.
    """
    )

    st.markdown(
        """ 
    Os principais tipos de dados que são já parte do Python e que vamos abordar são
    os seguintes:

    Tipos de Dados |
    ---|
    list | 
    set |
    frozenset |
    dict |
    int |
    str |
    """
    )

    data_types.string()


concepts_dic = {
    "Olá, Mundo": hello_world,
    "Tipos de dados": __data_types,
}

concepts_dic[concepts]()
