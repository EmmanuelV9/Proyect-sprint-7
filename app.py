import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma')
st.header('Histograma y grafico de conjunto de datos venta de coches')
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.button('Construir un grafico de dispersion')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispersion para la columna odómetro')
    fig = px.scatter(car_data,x="odometer",y="price")
    st.plotly_chart(fig, use_container_width=True)