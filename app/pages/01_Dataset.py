import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset — Minería de Datos 1",
    page_icon="📁",
    layout="wide"
)

st.title("📁 Inspección y Calidad del Dataset")
st.markdown("---")

# 1. DESCRIPCIÓN GENERAL
st.header("1. Descripción General")
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("""
    El dataset bajo estudio contiene registros de comportamiento pertenecientes a usuarios de una plataforma de streaming. 
    Originalmente, la matriz de datos contaba con **8.160 filas y 8 columnas**, recopilando tanto perfiles demográficos como métricas de consumo y soporte técnico.
    """)
    
    # Diccionario de Variables pedido por consigna
    st.markdown("#### **Diccionario de Variables**")
    diccionario = {
        "Variable": ["user_id", "age", "subscription_plan", "monthly_watch_time_mins", "country", "favorite_genre", "last_login_date", "customer_support_tickets"],
        "Tipo Original": ["int64", "int64", "str (object)", "float64", "str (object)", "str (object)", "str (object)", "int64"],
        "Descripción": [
            "Identificador único del usuario.",
            "Edad del usuario.",
            "Plan contratado por el cliente.",
            "Minutos de reproducción mensuales consumidos.",
            "País de residencia del usuario.",
            "Género cinematográfico preferido.",
            "Última fecha registrada de inicio de sesión.",
            "Cantidad de reclamos de soporte técnico realizados."
        ]
    }
    st.table(pd.DataFrame(diccionario))

with col2:
    with st.container(border=True):
        st.markdown("### 📊 Dimensiones del Pipeline")
        st.metric(label="Registros Iniciales (Dirty)", value="8.160")
        st.metric(label="Registros Finales (Clean)", value="7.633", delta="-527 filas")
        st.metric(label="Tasa de Retención Total", value="93.54%")


# 2. RESUMEN BREVE DE CALIDAD
st.markdown("---")
st.header("2. Resumen de Calidad de los Datos")

st.markdown("""
Durante la etapa de auditoría inicial, se detectaron severas anomalías en los datos crudos que requirieron intervención metodológica:
* **Valores Faltantes (Nulos):** Se identificaron nulos distribuidos en tres variables críticas: `last_login_date` (3.92%), `favorite_genre` (2.94%) y `monthly_watch_time_mins` (2.37%).
* **Registros Duplicados:** Se detectaron 128 filas idénticas en el sistema que introducían sesgo por doble conteo.
* **Outliers e Inconsistencias Extremas:** Valores imposibles para el negocio como edades negativas (-5) o seniles (150 años), minutos de reproducción corruptos (99.999 minutos, superando la cantidad de minutos de un mes completo) y ráfagas artificiales de tickets de soporte técnico (150 reclamos).
""")

# Tabla resumen del Log ETL
st.markdown("#### **Historial de Auditoría (Log de Cambios ETL)**")
log_etl = {
    "Paso": [0, 1, 2, 3, 4, 5],
    "Descripción": [
        "Dataset original", 
        "Eliminación de duplicados", 
        "Normalización Categoricas", 
        "Limpieza de fechas y filtrado de periodo 2018-2025", 
        "Imputación de faltantes en género y tiempo mensual", 
        "Tratamiento de outliers"
    ],
    "Filas Resultantes": [8160, 8032, 8032, 7633, 7633, 7633],
    "Nulos Totales": [753, 753, 753, 418, 0, 0],
    "Retención (%)": ["100.00%", "98.43%", "98.43%", "93.54%", "93.54%", "93.54%"]
}
st.dataframe(pd.DataFrame(log_etl), use_container_width=True)


# 3. TRANSFORMACIONES PRINCIPALES
st.markdown("---")
st.header("3. Transformaciones Principales Aplicadas")

tab1, tab2, tab3 = st.tabs(["Estandarización", "Imputación Inteligente", "Saneamiento de Outliers"])

with tab1:
    st.markdown("""
    * **Normalización Textual:** Se unificaron las variables categóricas (`subscription_plan`, `country`, `favorite_genre`) pasándolas a minúsculas, removiendo espacios en blanco (`.str.strip()`) y mapeando abreviaturas o errores de tipeo (ej: unificación de *'arg'* a *'argentina'*, o *'basic'* a *'básico'*).
    * **Casting Cronológico:** La variable `last_login_date` se convirtió a tipo fecha (`datetime64`), removiendo registros corruptos o fuera del rango lógico del negocio (período 2018-2025).
    """)

with tab2:
    st.markdown("""
    Se analizaron los mecanismos de pérdida para no sesgar las distribuciones:
    * **Mecanismo MCAR (Completamente al azar):** Para los nulos de `favorite_genre` (~3% parejo en todos los países), se asignó la etiqueta **'No especificado'** para mantener la neutralidad del perfil.
    * **Mecanismo MAR (Al azar condicionado):** Para `monthly_watch_time_mins`, la falta estaba correlacionada con el tipo de suscripción (los Premium tenían 9.68% de faltantes). Se imputó utilizando la **mediana agrupada por plan**, garantizando valores realistas acordes al segmento de consumo.
    """)

with tab3:
    st.markdown("""
    Para no perder filas valiosas, los valores atípicos se trataron mediante técnicas estadísticas de **Imputación** y **Suavizado (Clipping)**:
    * **Edad:** Los 94 perfiles con edades imposibles se reemplazaron por la mediana de edad de su respectivo plan.
    * **Métricas de Consumo y Soporte:** Se aplicó un *clipping* matemático basado en el Rango Intercuartílico ($3.0 \times \text{IQR}$). Los valores negativos o artificialmente altos se toparon en **2762.4 minutos** de reproducción y un máximo de **4.0 tickets** de soporte, estabilizando la varianza sin eliminar usuarios.
    """)


# 4. VISTA PREVIA SIMPLE
st.markdown("---")
st.header("4. Vista Previa del Dataset Limpio")

# Carga del dataset procesado final
df_procesado = pd.read_json('../data/processed/streaming_users_clean.json')
df_clean_preview = pd.DataFrame(df_procesado)

st.dataframe(df_clean_preview, use_container_width=True)
st.success("✨ El dataset se encuentra listo, balanceado y libre de nulos para las etapas de EDA y reducción dimensional.")

# Botón para ir al EDA
st.markdown("---")
col_btn, _ = st.columns([1, 3])
with col_btn:
    st.page_link("pages/02_EDA.py", label="Ir al Análisis Exploratorio (EDA)", icon="📊", use_container_width=True)

st.caption("Proyecto Integrador · Minería de Datos 1 · ITSE")