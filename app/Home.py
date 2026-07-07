import streamlit as st

st.set_page_config(
    page_title="Proyecto Integrador — Minería de Datos 1",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 Proyecto Integrador")
st.subheader("Minería de Datos 1 — ITSE")
st.markdown("### *Análisis de Comportamiento y Reducción de Dimensionalidad en Usuarios de Streaming*")
st.markdown("---")

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown("### 📌 Contexto del Proyecto")
    st.markdown("""
    El objetivo de este proyecto es aplicar los fundamentos de **Minería de Datos** para construir un pipeline analítico reproducible, justificando metodológicamente 
    cada decisión mediante evidencia empírica sobre el comportamiento de usuarios en plataformas de streaming.
    """)
    
    st.markdown("### 🗺️ Hoja de Ruta del Análisis")
    st.info("**📁 Dataset:** Inspección inicial del dataset y proceso ETL de limpieza.")
    st.info("**📊 EDA:** Análisis Exploratorio de Datos enfocado en resolver preguntas de negocio.")
    st.info("**🔷 PCA:** Escalamiento de variables y Reducción de dimensionalidad.")
    st.info("**📝 Conclusiones:** Principales hallazgos, limitaciones y próximos pasos.")

with col2:
    with st.container(border=True):
        st.markdown("### 👤 Datos del Proyecto")
        
        st.markdown("**Integrante:**")
        st.write("• Pinto Villegas, Eduardo Joaquín")
        
        st.markdown("**Cursado:**")
        st.write("• **Comisión:** Nodo")
        st.write("• **Fecha:** Julio 2026")
        
        st.markdown("**Código Fuente:**")
        
        st.markdown("🔗 [Repositorio en GitHub](https://github.com/tu-usuario/tu-repositorio)")

st.markdown("---")

col_btn, _ = st.columns([1, 3])
with col_btn:
    st.page_link("pages/01_Dataset.py", label="Comenzar con el Dataset", icon="📁", use_container_width=True)

st.caption("Proyecto Integrador · Minería de Datos 1 · ITSE")