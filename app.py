# rodar local:  streamlit run app.py
import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px
import time

st.header('O melhor site de análise de carros americanos. ')

car_data = pd.read_csv('vehicles.csv')
car_data = car_data.dropna(subset=['price'])

st.write('Filtre o seu carro ideal:')
cola, colb, colc = st.columns(3)

with cola:
    slider_price = st.select_slider(
        'Valor do veículo',
        options=car_data['price'].sort_values(),
        value=(int(car_data['price'].min()), int(car_data['price'].max())))
with colb:
    seletor_fuel = st.multiselect(
        # criar um botão
        'Selecione o combustivel', car_data['fuel'].unique(), default=car_data['fuel'].unique()[0])
with colc:
    seletor_transmission = st.multiselect(
        # criar um botão
        'Selecione a trasnmissão', car_data['transmission'].unique(),  default=car_data['transmission'].unique()[1])

car_data_filtrado = car_data[
    (car_data['price'] >= slider_price[0]) &          # preço mínimo
    (car_data['price'] <= slider_price[1]) &          # preço máximo
    (car_data['fuel'].isin(seletor_fuel)) &           # combustível selecionado
    # transmissão selecionada
    (car_data['transmission'].isin(seletor_transmission))
]


st.dataframe(data=car_data_filtrado)


# 1. Cria duas colunas lado a lado
col1, col2 = st.columns(2)

# 2. Coloca o primeiro botão na coluna 1
with col1:
    hist_button = st.checkbox('Criar histograma de milhas')  # criar um botão

# 3. Coloca o segundo botão na coluna 2
with col2:
    graf_button = st.checkbox(
        'Criar gráfico dispersão milhas')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de milhas rodadas por quantidade de veiculos.')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    fig.update_layout(
        xaxis_title="Quilometragem (milhas)",
        yaxis_title="Quantidade"
    )
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if graf_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico para o conjunto de milhas rodadas por preço')

    # criar um histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.update_layout(
        xaxis_title="Quilometragem (milhas)",
        yaxis_title="Preço($)"
    )
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
