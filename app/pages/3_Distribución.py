import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
#import scipy

#df_inicial=pd.read_csv('..\dataset_IRM_psu_2003-2018 .csv')
#definimos filtros 
#selected_columns = ["Lenguaje", "Matemáticas", "Historia", "Ciencias"]
st.header('Ajuste de la distribución de puntajes')
df_boxplots = pd.read_pickle("app/df_boxplots.pkl")

with st.expander("Descripcion"):
    st.write("""  Representación detallada de la distribución de puntajes en función de su frecuencia para las distintas materias evaluadas. 
    Es posible seleccionar las materias cuya distribución desea ser visualizada.
""")
with st.expander('Utilidad'):
    st.write('''1) Visualizar de manera detallada la forma de la distribución analizando su inclinación o sesgo. 
2) Comparar las distribuciones de resultados de materias con competencias similares (Matemática/Ciencias - Lenguaje/Historia)
''')

asignaturas = df_boxplots['Asignatura'].drop_duplicates()
asignatura = st.sidebar.selectbox('Seleccione asgnatura', options = asignaturas)
años = df_boxplots['Año'].drop_duplicates()
año = st.sidebar.selectbox('Seleccione año', options = años)

filtro_mujer = (df_boxplots['Genero'] == 'F') & (df_boxplots['Asignatura']==asignatura) & (df_boxplots['Año']== año)
filtro_varon = (df_boxplots['Genero'] =='M' ) & (df_boxplots['Asignatura']==asignatura) & (df_boxplots['Año']== año)


#st.dataframe(df_boxplots)

# Add histogram data con 'NaNs' filtrados
x1 = df_boxplots[filtro_mujer]['Puntaje']
x1_filtered = [val for val in x1 if not np.isnan(val)]

x2 = df_boxplots[filtro_varon]['Puntaje']
x2_filtered = [val for val in x2 if not np.isnan(val)]


# Group data together
hist_data = [x1_filtered, x2_filtered]

group_labels = ['F', 'M']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, show_hist = False, show_curve=True)
#bin_size=[.1, .25, .5], 
fig.update_layout(
    xaxis_title='Puntaje',
    yaxis_title='Frecuencia'
)
# Plot!
st.plotly_chart(fig, use_container_width=True)