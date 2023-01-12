def installation():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# Instalação")
    st.write(
        """
                This demo shows how to use
        [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
        to display geospatial data.
        """
    )
