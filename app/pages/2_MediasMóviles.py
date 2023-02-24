import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df_boxplots = pd.read_pickle("app/df_boxplots.pkl")
st.header('Evolución de puntajes 2002 - 2018' )
df_inicial=pd.read_pickle('app/df_inicial.pkl')
with st.expander("Descripcion"):
    st.write(""" Monitoramento de la evolución anual de los resultados promedio de cada grupo, 
    pudiendo visualizar los cambios en las pendientes en los rendimientos. 
    En este caso, se grafican las medias de los resultados PSU para las distintas materias a través de los años.
""")
with st.expander('Utilidad'):
    st.write('''1) Visualizar la evolución del rendimiento en cada materia.
2) Comparar la evolución del rendimiento de las materias con competencias similares
3) Reconocer de forma precisa los años de mejor o peor rendimiento en determinadas materias con sus fluctuaciones respectivas, para relacionarlos a prácticas educativas
''')
generos = df_boxplots['Genero'].drop_duplicates()
genero = st.sidebar.selectbox('Seleccione genero', options = generos)
filtro = df_inicial['Sexo'] == genero

#date = st.select_slider("Seleccione la fecha de predicción:", options=años, key=1)

df_inicial.drop(['Etiqueta'],axis=1, inplace=True)
df_promedios = df_inicial[filtro].groupby(['Año']).mean()
#tiempo = df_promedios.index
#df_promedios['Año'] = tiempo
#df_promedios.reset_index()

fig = px.line(
            data_frame=df_promedios,
            x=df_promedios.index,
            y=df_promedios.columns,
            title="Evolucion de puntajes por género",
            #color="Asignatura",
            labels={
                "Año",
                "Puntaje"
            },
        )
st.plotly_chart(figure_or_data=fig, use_container_width=True)
#st.dataframe(df_promedios)