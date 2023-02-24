import streamlit as st
from PIL import Image
st.header('Gender Gap Tracker')

st.write('''Esta App se enfoca en monitorear la brecha de resultados de la prueba de selección universitaria 
entre hombres y mujeres de un establecimiento en particular. Con una interfaz fácil de usar, 
el Dashboard permite a los usuarios visualizar de manera clara y detallada los resultados de rendimiento
 de ambos géneros en diferentes áreas de estudio. Se ofrece una serie de herramientas de análisis 
 que permiten a los usuarios profundizar en los resultados y contribuir al análisis de posibles causas 
 de la brecha de género.''')

image = Image.open("gender.jpg")
st.write("")
st.image(image, caption="")