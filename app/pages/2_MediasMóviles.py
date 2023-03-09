import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


dataframe = st.session_state.get("data")

if dataframe is not None:
    st.title("Evolución de puntajes 2002 - 2018")

    with st.expander("Descripcion"):
        st.write(
            """ 
            Monitoramento de la evolución anual de los resultados promedio de cada grupo, 
            pudiendo visualizar los cambios en las pendientes en los rendimientos. 
            En este caso, se grafican las medias de los resultados PSU para las distintas materias a través de los años.
            """
        )

    with st.expander("Utilidad"):
        st.write(
            """
            1) Visualizar la evolución del rendimiento en cada materia.
            2) Comparar la evolución del rendimiento de las materias con competencias similares
            3) Reconocer de forma precisa los años de mejor o peor rendimiento en determinadas materias con sus fluctuaciones respectivas, para relacionarlos a prácticas educativas
            """
        )

    asignaturas = dataframe.drop(columns=["Sexo", "Etiqueta", "Año"]).columns
    asignatura = st.sidebar.selectbox("Seleccione genero", options=asignaturas)

    fig = px.line(
        data_frame=dataframe.groupby(["Sexo", "Año"]).mean().reset_index(),
        x="Año",
        y=asignatura,
        title="Evolución de puntajes por género",
        color="Sexo",
        labels={"Año", "Puntaje"},
        color_discrete_sequence=["red", "blue"],
    )
    st.plotly_chart(figure_or_data=fig, use_container_width=True)
else:
    st.info(
        "Actualmente no hay datos ingresados, por favor cargue su archivo csv en la pestaña de Home",
        icon="💡",
    )
