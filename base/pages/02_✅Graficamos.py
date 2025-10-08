import streamlit as st
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt


lagos = pd.read_csv('lagos_arg.csv')
st.title("Gráfico")
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = lagos['Ubicación'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Provincia')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de Lagos por provincia')

# Mostrar el gráfico
st.pyplot(fig)
