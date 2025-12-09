import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da página ---
st.set_page_config(
    page_title="Dashboard de Filmes",
    page_icon="🎬",
    layout="wide"
)

# --- Carregamento dos dados ---
@st.cache_data
def carregar_dados():
    df = pd.read_csv("movies.csv")
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["year"] = df["release_date"].dt.year
    return df

df = carregar_dados()

# --- Barra Lateral ---
st.sidebar.header("Filtros")

# Filtro: Ano
anos = sorted(df["year"].dropna().unique())
anos_selecionados = st.sidebar.multiselect(
    "Ano de lançamento",
    anos,
    default=anos
)

# Filtro: Nota mínima
nota_minima = st.sidebar.slider(
    "Nota mínima (vote_average)",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)

# --- Filtragem ---
df_filtrado = df[
    (df["year"].isin(anos_selecionados)) &
    (df["vote_average"] >= nota_minima)
]

# --- Título ---
st.title("🎬 Dashboard Simples de Análise de Filmes")
st.markdown("Explore popularidade, notas e tendências de filmes com base no arquivo **movies.csv**.")

# --- Métricas ---
st.subheader("Métricas Gerais")

if not df_filtrado.empty:
    media_nota = df_filtrado["vote_average"].mean()
    total_filmes = df_filtrado.shape[0]
    filme_mais_popular = df_filtrado.loc[df_filtrado["popularity"].idxmax(), "title"]
else:
    media_nota = total_filmes = 0
    filme_mais_popular = "-"

col1, col2, col3 = st.columns(3)
col1.metric("Nota média", f"{media_nota:.2f}")
col2.metric("Total de filmes", total_filmes)
col3.metric("Mais popular", filme_mais_popular)

st.markdown("---")

# --- Gráfico de popularidade ---
st.subheader("Popularidade dos Filmes")

if not df_filtrado.empty:
    grafico = px.scatter(
        df_filtrado,
        x="release_date",
        y="popularity",
        size="vote_count",
        color="vote_average",
        hover_name="title",
        title="Popularidade ao longo do tempo",
        labels={"release_date": "Data", "popularity": "Popularidade"}
    )
    st.plotly_chart(grafico, use_container_width=True)
else:
    st.warning("Nenhum dado para exibir no gráfico.")

# --- Tabela ---
st.subheader("Tabela de Filmes")
st.dataframe(df_filtrado)
