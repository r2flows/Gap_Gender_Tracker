import streamlit as st
import pandas as pd
import plotly.express as px


dataframe = st.session_state.get("data")

if dataframe is not None:
    st.title("Diagramas de caja comparados por género")

    with st.expander("Descripción"):
        st.write(
            """
            Representación proyectada de la Campana de Gauss estratificada en cuartiles de rendimiento. 
            En el eje vertical encontramos la escala de puntajes y en el eje horizontal las distintas materias evaluadas.
            La mayor cantidad de puntajes se encuentra justamente en las cajas que representan el centro de la campana de Gauss.
            """
        )
    with st.expander("Utilidad"):
        st.write(
            """
            1) Dar una visualización de la distribución detallada en cuartiles de rendimiento.
            2) Reconocer variaciones importantes en los resultados de aprendizaje entre dos grupos diferentes separados por género
            """
        )

    años = dataframe["Año"].unique()
    año = st.sidebar.selectbox("Seleccione año", options=años)
    asignaturas = dataframe.drop(columns=["Sexo", "Etiqueta", "Año"]).columns
    data_long = pd.melt(
        dataframe,
        id_vars=["Sexo", "Año"],
        value_vars=asignaturas,
        var_name="Asignatura",
        value_name="Puntaje",
    )
    filtro = data_long["Año"] == año

    fig = px.box(
        data_long[filtro],
        x="Asignatura",
        y="Puntaje",
        color="Sexo",
        color_discrete_sequence=["red", "blue"],
    )

    st.plotly_chart(fig)

else:
    st.info(
        "Actualmente no hay datos ingresados, por favor cargue su archivo csv en la pestaña de Home",
        icon="💡",
    )
