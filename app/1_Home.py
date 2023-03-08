import streamlit as st
import pandas as pd
from PIL import Image
from time import sleep

st.title("Gender Gap Tracker")

st.write(
    """Esta App se enfoca en monitorear la brecha de resultados de la prueba de selección universitaria 
entre hombres y mujeres de un establecimiento en particular. Con una interfaz fácil de usar, 
el Dashboard permite a los usuarios visualizar de manera clara y detallada los resultados de rendimiento
 de ambos géneros en diferentes áreas de estudio. Se ofrece una serie de herramientas de análisis 
 que permiten a los usuarios profundizar en los resultados y contribuir al análisis de posibles causas 
 de la brecha de género."""
)

image = Image.open("app/gender.jpg")

st.image(image, use_column_width="always", caption="")

uploaded_file = st.file_uploader(label="Sube tu archivo aquí", type=["csv"])

if uploaded_file is not None:
    try:
        dataframe = pd.read_csv(uploaded_file)
    except:
        st.error("Error al cargar el archivo", icon="❌")
    else:
        if st.session_state.get("data") is None:
            st.session_state["data"] = dataframe
            placeholder = st.empty()
            placeholder.success("El archivo fue cargado con éxito", icon="✅")
            sleep(3)
            placeholder.empty()
        else:
            st.session_state["data"] = dataframe
            placeholder = st.empty()
            placeholder.warning(
                "Estas sobrescribiendo los datos anteriores",
                icon="⚠",
            )
            sleep(3)
            placeholder.empty()
