import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
#import statsmodels.api as sm

df_boxplots = pd.read_pickle("df_boxplots.pkl")
st.header('Diagramas de caja comparados por género')

with st.expander("Descripcion"):
    st.write(""" Representación proyectada de la Campana de Gauss estratificada en cuartiles de rendimiento. 
En el eje vertical encontramos la escala de puntajes y en el eje horizontal las distintas materias evaluadas.
La mayor cantidad de puntajes se encuentra justamente en las cajas que representan el centro de la campana de Gauss.
""")
with st.expander('Utilidad'):
    st.write('''1) Dar una visualización de la distribución detallada en cuartiles de rendimiento.
2) Reconocer variaciones importantes en los resultados de aprendizaje entre dos grupos diferentes separados por género
''')

años = df_boxplots['Año'].drop_duplicates()

año = st.sidebar.selectbox('Seleccione año', options = años)
filtro = df_boxplots['Año'] == año

fig = px.box(df_boxplots[filtro], x ="Asignatura", y ="Puntaje", color ="Genero", color_discrete_sequence=['red','blue'])

#fig.update_traces(quartilemethod="exclusive") 

st.plotly_chart(fig)

