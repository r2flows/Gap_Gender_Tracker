import streamlit as st
import plotly.express as px


dataframe = st.session_state.get("data")

if dataframe is not None:
    st.title("Ajuste de la distribución de puntajes")

    with st.expander("Descripción"):
        st.write(
            """
            Representación detallada de la distribución de puntajes en función de su frecuencia para las distintas materias evaluadas. 
            Es posible seleccionar las materias cuya distribución desea ser visualizada.
            """
        )
    with st.expander("Utilidad"):
        st.write(
            """
            1) Visualizar de manera detallada la forma de la distribución analizando su inclinación o sesgo. 
            2) Comparar las distribuciones de resultados de materias con competencias similares (Matemática/Ciencias - Lenguaje/Historia)
            """
        )

    asignaturas = dataframe.drop(columns=["Sexo", "Etiqueta", "Año"]).columns
    asignatura = st.sidebar.selectbox("Seleccione genero", options=asignaturas)
    años = dataframe["Año"].unique()
    año = st.sidebar.selectbox("Seleccione año", options=años)

    fig = px.violin(
        data_frame=dataframe[dataframe["Año"] == año],
        x=asignatura,
        violinmode="overlay",
        orientation="h",
        color="Sexo",
        color_discrete_sequence=["red", "blue"],
    )

    fig.update_traces(
        selector=dict(marker=dict(color="red")),
        side="positive",
    )
    
    fig.update_traces(
        selector=dict(marker=dict(color="blue")),
        side="positive",
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info(
        "Actualmente no hay datos ingresados, por favor cargue su archivo csv en la pestaña de Home",
        icon="💡",
    )
