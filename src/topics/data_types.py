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
    st.code("print(nome_completo)")
    st.text("Resultado")
    st.code("YanickAndrade", language="sh")

    st.markdown(""" 
    Reparaste que o **Primeiro Nome** e o **Apelido** ficaram 'colados'?
    Pois. Podemos resolver isso concatenando mais uma **string** em branco no meio das duas.
    """)

    st.code(""" 
    nome_completo = primeiro_nome + ' ' + apelido
    """)
    st.code("print(nome_completo)")
    st.text("Resultado")
    st.code("Yanick Andrade", language="sh")


    st.markdown(
        """
        #### A segunda forma de Concatenar

        A segunda forma de concatenar é usando **f-string**, que é o abreviativo de **Formatted string literals**.

        F-strings dá-nos uma forma de incorporar uma string dentro de uma outra string/texto 
        usando uma sintaxe mais flexivel e minimalista.
    """
    )
    st.code(
        """primeiro_nome = 'Yanick'\napelido = 'Andrade'\nnome_completo = f'{primeiro_nome} {apelido}
    """
    )
    st.code("print(nome_completo)")
    st.text("Resultado")
    st.code("Yanick Andrade", language="sh")

    st.markdown(""" 
    Outra forma de usar o f-strings por exemplo é escrevendo um texto e usar a variavél com o nome
    para fazer o *auto-complete*.
    """)
    st.code("print(f'Olá, meu nome é {nome_completo}')")
    st.text("Resultado")
    st.code("Olá, meu nome é Yanick Andrade", language="sh")





    
