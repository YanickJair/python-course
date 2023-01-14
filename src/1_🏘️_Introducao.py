import streamlit as st

st.set_page_config(
    page_title="Python para Iniciantes",
    page_icon="👋",
)

st.write("# Bem vindo ao Python para Iniciantes! 👋")
st.sidebar.success("Programa de Estudo :point_up:")


st.markdown(
    f"""
    Aprenda os conceitos básicos de Python desde a sua introdução,
    como instalar e onde pode ser aplicado com exemplos de projectos
    desde o mais básico ao mais complexo.

    **👈 Selecione os tópicos na nemu do painel** para comçares a aprender!

    ### O que é Python :confused: :question:

    Python é uma Linguagem de Programção de alto nível, criado por [Guido van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) em 1991.
    Hoje, Python é gerido pela [Python Software Foundation](https://www.python.org), que tem como missão promover, proteger e desenvolver ainda mais
    a linguagem.

    Por ser uma linguagem interpretada, Python permite-nos poupar tempo durante o desenvolvimento
    pois não precisamos de compilar o nosso código.

    Só para esclarecer, uma Linguagem de Programação diz-se ser "Interpretada" quando ela executa os 
    códigos linha-a-linha ao invés de tudo de uma só vez.

    Segundo a o tutotial oficial do [Python 3.10](https://docs.python.org/3.10/tutorial/), Python é
    uma linguagem poderosa e fácil de se aprender. Python é 100% Open Sourc (Código Aberto), e tem uma
    larguissíma comunidade ativa que vai dando suporte e garantido que a linguagem continue a crescer e
    sendo uma das mais usadas por grandes empresas em todo o mundo.      
"""
)

st.markdown(
    """ 
    #### Mas por que usar Python :question:
    Boa pergunta. Um dos principais objetivos do [Guido van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) quando criou a linguagem
    foi permitir ao programador ter maior foco em fazer o seu trabalho, desenvolver código, ao invés de focar nas partes computacionais, 
    deixando isso ao encargo do Python.

    Python pode ser aplicadas nas mais diversas áreas tais como:
    - Desenvolvimento Web (essa página foi feita usando [Streamlit](https://streamlit.io/))
    - Intiligência Artificial de Aprendizado de Máquina
    - Ciência de Dados
    - Desenvolvimento de [Aplicativos Desktop](https://docs.python.org/3/library/tkinter.html)
    - etc.

    As áreas onde podes usar Python :point_up: são das mais bem pagas, isso também conta
    como um dos motivos para aprenderes Python
"""
)
st.metric(label="Sálario médio Europa/Ano", value="€62,500K", delta="€78K")
st.markdown(
    """ 
    O Salário pode ser muito superior a isso dependendo da área e do páis claro.
"""
)

st.markdown(
    """ 
    ## Agora que já sabes um  bocadinho sobre Python que tal começar a aprender :question:
"""
)
