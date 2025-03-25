import pandas as pd
import streamlit as st
import plotly.express as px

# Função para carregar dados com cache
@st.cache_data
def load_data():
    df = pd.read_excel('sigefcamposproducaodesementes.xlsx')
    df['Data de Colheita'] = pd.to_datetime(df['Data de Colheita'], errors='coerce')
    df['Data do Plantio'] = pd.to_datetime(df['Data do Plantio'], errors='coerce')
    df['Produtividade'] = df['Producao bruta'] / df['Area']
    df['Mes_Colheita'] = df['Data de Colheita'].dt.month
    return df

# Carregar dados
df = load_data()

# Título do dashboard
st.title("Dashboard de Produção de Sementes")

# Filtros
selected_categorias = st.multiselect("Filtrar por Categoria", options=df['Categoria'].unique(), default=[])
selected_especies = st.multiselect("Filtrar por Espécie", options=df['Especie'].unique(), default=[])
selected_safras = st.multiselect("Filtrar por Safra", options=df['Safra'].unique(), default=[])
selected_uf = st.multiselect("Filtrar por Estado (UF)", options=df['UF'].unique(), default=[])
selected_cidades = st.multiselect("Filtrar por Cidade", options=df['Municipio'].unique(), default=[])

# Filtrar o DataFrame com base nos filtros selecionados
filtered_df = df.copy()
if selected_categorias:
    filtered_df = filtered_df[filtered_df['Categoria'].isin(selected_categorias)]
if selected_especies:
    filtered_df = filtered_df[filtered_df['Especie'].isin(selected_especies)]
if selected_safras:
    filtered_df = filtered_df[filtered_df['Safra'].isin(selected_safras)]
if selected_uf:
    filtered_df = filtered_df[filtered_df['UF'].isin(selected_uf)]
if selected_cidades:
    filtered_df = filtered_df[filtered_df['Municipio'].isin(selected_cidades)]

# Verificar se o DataFrame filtrado está vazio
if filtered_df.empty:
    st.write("Por favor, selecione os filtros para visualizar os gráficos.")
else:
    # Gráfico de sazonalidade das colheitas
    fig_sazonalidade = px.histogram(filtered_df, x='Mes_Colheita', color='Mes_Colheita', 
                                    title='Sazonalidade das Colheitas', 
                                    labels={'Mes_Colheita': 'Mês', 'count': 'Quantidade de Colheitas'},
                                    color_discrete_sequence=px.colors.sequential.Magma)
    st.plotly_chart(fig_sazonalidade)

    # Gráfico de produção por safra
    df_grouped = filtered_df.groupby('Safra')['Producao bruta'].sum().reset_index()
    fig_producao = px.line(df_grouped, x='Safra', y='Producao bruta', 
                           title='Tendência da Produção Agrícola ao Longo dos Anos',
                           labels={'Safra': 'Safra', 'Producao bruta': 'Produção Bruta (toneladas)'})
    st.plotly_chart(fig_producao)

    # Gráfico de impacto da categoria na produtividade média
    df_categoria = filtered_df.groupby('Categoria')['Produtividade'].mean().reset_index()
    fig_impacto = px.bar(df_categoria, x='Categoria', y='Produtividade', 
                         title='Impacto da Categoria na Produtividade Média',
                         labels={'Categoria': 'Categoria', 'Produtividade': 'Produtividade Média (ton/ha)'})
    st.plotly_chart(fig_impacto)