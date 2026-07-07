import streamlit as st

st.set_page_config(
    page_title="Conclusiones — Minería de Datos 1",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Conclusiones Finales")
st.markdown("---")

# ==============================================================================
# Hallazgos Principales
# ==============================================================================
st.markdown("### 🏆 Hallazgos Principales")
with st.container(border=True):
    st.markdown("""
    * **El Plan Comercial manda:** El EDA y el PCA confirmaron que el nivel de suscripción (Premium vs Básico) es el principal motor del tiempo de consumo mensual, superando a la afinidad de género.
    * **Efectividad del Pipeline:** La segmentación del tratamiento de nulos (MAR y MCAR) y el clipping de outliers estabilizaron las variables numéricas, reteniendo un sólido **93.54%** de los datos originales.
    * **Perfiles Sintéticos Claros:** Mediante el PCA logramos identificar tres tipos de usuarios puros: el *Activo General* (PC1), el *Joven con Fricción Técnica* (PC2) y el *Consumidor Intensivo Silencioso* (PC3).
    """)

st.markdown("---")

# ==============================================================================
# Limitaciones del Estudio
# ==============================================================================
st.markdown("### ⚠️ Limitaciones del Estudio")
with st.container(border=True):
    st.markdown("""
    * **Datos Corruptos de Origen:** La presencia de registros imposibles (como edades de 150 años o 99.999 minutos vistos) evidencia fallas severas en el sistema de carga o captura de datos crudos.
    * **Pocas Variables Numéricas:** Contar con solo 3 variables cuantitativas limitó el potencial de varianza explicada del PCA en los primeros componentes.
    * **Falta de Historial:** Al ser un corte estático, no se puede analizar la evolución temporal del comportamiento del usuario (churn o abandono de plataforma).
    """)

st.markdown("---")

# ==============================================================================
# Próximos Pasos
# ==============================================================================
st.markdown("### 🚀 Próximos Pasos")
with st.container(border=True):
    st.markdown("""
    * **Modelado Predictivo:** Utilizar los componentes sintéticos obtenidos en el PCA para entrenar modelos de Clustering (K-Means) o Clasificación para predecir fugas (*churn*).
    * **Ingeniería de Características:** Cruzar los datos actuales con variables de engagement real (dispositivos usados, clics, interacciones por hora).
    * **Auditoría de Logs:** Elevar al equipo de ingeniería una propuesta de validación en frontend para evitar la carga de valores negativos o incoherentes en la base de datos.
    """)

st.markdown("---")

# Botón final de cierre del Proyecto Integrador
st.success("🎉 ¡Muchas gracias por leer mi trabajo!")

# Enlace de regreso a la Home
col_btn, _ = st.columns([1, 3])
with col_btn:
    st.page_link("Home.py", label="Volver al Inicio (Home)", icon="🏠", use_container_width=True)

st.caption("Proyecto Integrador · Minería de Datos 1 · ITSE")