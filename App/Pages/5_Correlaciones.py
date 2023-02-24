import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df_boxplots = pd.read_pickle("df_boxplots.pkl")
st.header('Correlaciones entre asignaturas')
df_inicial=pd.read_pickle('df_inicial.pkl')
#años = df_boxplots['Año'].drop_duplicates()with st.expander("Descripcion herramienta"):
with st.expander('Descripción'):
    st.write(""" Esta herramienta muestra las correlaciones entre las asignaturas. Valores cercanos a 1 indican mayor correlación
    entre las variables, mientras que valores cercanos a cero, menor o nula correlación """)
with st.expander('Utilidad'):
    st.write('''1) Monitorear la correlación entre materias que desarrollan habilidades similares.
2) Ayudar a profesores de materias diferentes a mejorar metodologías en conjunto
''')


generos = df_boxplots['Genero'].drop_duplicates()
genero= st.sidebar.selectbox('Seleccione genero', options = generos)
años = df_boxplots['Año'].drop_duplicates()

año = st.sidebar.selectbox('Seleccione año', options = años)

filtro = (df_inicial['Sexo'] == genero) & (df_inicial['Año']==año)
df_correlaciones = df_inicial[filtro].drop(['Etiqueta','Sexo','Año'], axis=1)
#st.dataframe(df_correlaciones)
corr = df_correlaciones.corr().round(2)
#st.write(corr)

fig = px.imshow(corr, text_auto=True)
st.plotly_chart(figure_or_data=fig, use_container_width=True)