import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dataframe = st.session_state.get("data")

if dataframe is not None:
    st.title("Correlaciones entre asignaturas")
    with st.expander("Descripción"):
        st.write(
            """
            Esta herramienta muestra las correlaciones entre las asignaturas. Valores cercanos a 1 indican mayor correlación
            entre las variables, mientras que valores cercanos a cero, menor o nula correlación
            """
        )
    with st.expander("Utilidad"):
        st.write(
            """
            1) Monitorear la correlación entre materias que desarrollan habilidades similares.
            2) Ayudar a profesores de materias diferentes a mejorar metodologías en conjunto
            """
        )

    años = dataframe["Año"].unique()

    año = st.sidebar.selectbox("Seleccione año", options=años)

    filtro_varon = (dataframe["Año"] == año) & (dataframe["Sexo"] == "M")
    filtro_mujer = (dataframe["Año"] == año) & (dataframe["Sexo"] == "F")

    df_corr_varon = dataframe[filtro_varon].drop(["Etiqueta", "Sexo", "Año"], axis=1)
    df_corr_mujer = dataframe[filtro_mujer].drop(["Etiqueta", "Sexo", "Año"], axis=1)

    corr_varon = df_corr_varon.corr().round(2)
    corr_mujer = df_corr_mujer.corr().round(2)

    fig = make_subplots(
        cols=2, shared_yaxes=True, subplot_titles=("Masculino", "Femenino")
    )

    fig.add_trace(
        trace=go.Heatmap(
            z=corr_varon,
            zmax=1,
            zmin=0,
            name="Masculino",
            x=corr_varon.columns,
            y=corr_varon.index,
            colorscale="RdBu",
            text=corr_varon,
            texttemplate="%{z}",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        trace=go.Heatmap(
            z=corr_mujer,
            zmax=1,
            zmin=0,
            name="Femenino",
            x=corr_mujer.columns,
            colorscale="RdBu",
            text=corr_mujer,
            texttemplate="%{z}",
        ),
        row=1,
        col=2,
    )
    st.plotly_chart(figure_or_data=fig, use_container_width=True)

else:
    st.info(
        "Actualmente no hay datos ingresados, por favor cargue su archivo csv en la pestaña de Home",
        icon="💡",
    )
