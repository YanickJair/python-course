import streamlit as st


def string():
    st.markdown(
        """ 
    ## Strings

    Strings são basicamente sequências de caracteres. Em Python a palavra reservada para
    referir-mo-nos ao *String* é o **str**.

    Em Python para criarmos uma *string* usamos o **Aspas** ou **Plicas**.
    Vejamos o exemplo abaixo para criar uma váriavel **nome**:
    """
    )

    st.code(
        """ 
    nome = 'Yanick Andrade'
    """
    )

    st.markdown(
        """ 
    Usando a função *print*, podemos imprimir o nome
    """
    )

    st.code(
        """ 
    print(nome)
    """
    )
    st.code("Yanick Andrade", language="sh")

    st.markdown("***")
    st.markdown(
        """ 
    Podemos juntar duas ou mais *strings* para criar uma só. A isso chamamos de "Concatenação".
    Em Python existe 3 formas mais comuns de se fazer e vamos vê-las agora.
    """
    )
    st.markdown(
        """
        #### A primeira forma de Concatenar

        Podemos juntar duas ou mais strings usando o sinal + (mais)
    """
    )
    st.code(
        """primeiro_nome = 'Yanick'\napelido = 'Andrade'\nnome_completo = primeiro_nome + apelido
    """
    )
    st.text("Resultado")
    st.code("YanickAndrade", language="sh")
