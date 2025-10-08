import pandas as pd
import streamlit as st

lagos =  pd.read_csv('lagos_arg.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
filas, columnas = lagos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = lagos.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
nombres_ubic = lagos['Sup Tamaño'].unique()
cant_ubic = len(lagos['Sup Tamaño'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna **Sup Tamaño**?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **Sup Tamaño**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas ?"):
   
    st.write(lagos.columns)

        