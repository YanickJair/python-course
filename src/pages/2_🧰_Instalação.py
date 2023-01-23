import streamlit as st
from PIL import Image

st.set_page_config(page_title="Instalação", page_icon="📈")

st.markdown(f"# Instalação")
st.sidebar.markdown(f"# Instalar Python")


def install_windows():

    st.markdown(
        """ 
        De modo a poder acompanhar e tirar melhor proveito garante que tens o 
        Python instalado no seu 💻

        ### Python no Windows
        Para instalar no Windows, baixe [aqui](https://www.howtogeek.com/197947/how-to-install-python-on-windows/) 
        o Python primeiro.

    """
    )
    st.image(Image.open("src/images/install_windows.png"))


def install_linux():
    st.markdown(
        """ 
        ### Python Linux
        O bom do Linux é que já vem com Python instalado, por isso não tens de preocupar com isso.

        Mas caso não esteja instalado, podes seguir as instruções [aqui](https://www.geeksforgeeks.org/how-to-install-python-on-linux/).
    """
    )


def install_ide():
    st.markdown(
        """ 
    ### Instalar Editor de Textos ou IDE

    Editor de Textos é onde vais escrever o teu código que depois irás executar.
    Existem vários editores de textos que podes escolher para começares a programar.

    Tem uns que são específicos para cada **Linguagem** e tem outras que pode ser
    usado para qualquer linguagem onde podes instalar *plugins* ou extensões de modo
    a personaliza-lo para que fique a gosto.

    Eu no meu dia-a-dia uso ou o [Pycharm](https://www.jetbrains.com/pycharm/download/#section=linux) 
    ou o [Visual Studio Code](https://code.visualstudio.com/Download).

    Recomendo começares com o [Pycharm](https://www.jetbrains.com/pycharm/download/#section=linux) pois
    é o Editor que vou usar em caso tenha que dar algum exemplo relacionado ao Editores.
    """
    )


install_windows()
install_linux()
install_ide()
