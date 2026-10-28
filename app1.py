import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Dashboard de Análisis de Datos", page_icon="📊", layout="wide"
)

st.title("📊 Demostración de Streamlit: Análisis de Datos")
st.markdown(
    "Esta aplicación interactiva muestra gráficos dinámicos y métricas usando Pandas, NumPy y Streamlit."
)

# Sidebar para controles
st.sidebar.header("Parámetros de Configuración")
num_puntos = st.sidebar.slider(
    "Cantidad de datos sintéticos", 50, 1000, 200, step=50
)
ruido = st.sidebar.slider("Nivel de ruido", 0.1, 5.0, 1.0)

# Generación de datos de ejemplo
np.random.seed(42)
df = pd.DataFrame(
    {
        "x": np.linspace(0, 10, num_puntos),
        "y": np.sin(np.linspace(0, 10, num_puntos))
        + np.random.normal(0, ruido, num_puntos),
        "categoria": np.random.choice(["Grupo A", "Grupo B", "Grupo C"], num_puntos),
    }
)

# Métricas principales
col1, col2, col3 = st.columns(3)
col1.metric("Total Registros", len(df))
col2.metric("Promedio Eje Y", f"{df['y'].mean():.2f}")
col3.metric("Desviación Estándar", f"{df['y'].std():.2f}")

st.divider()

# Gráficos
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Gráfico de Líneas (Tendencia)")
    st.line_chart(df.set_index("x")["y"])

with col_g2:
    st.subheader("Gráfico de Dispersión")
    st.scatter_chart(df, x="x", y="y", color="categoria")

# Tabla de datos interactiva
with st.expander("Ver dataset completo"):
    st.dataframe(df, use_container_width=True)