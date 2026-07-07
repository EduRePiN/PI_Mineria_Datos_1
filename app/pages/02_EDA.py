import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="EDA — Minería de Datos 1",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("---")

# 📥 Carga del dataset limpio procesado
@st.cache_data
def cargar_datos_limpios():
    return pd.read_json('../data/processed/streaming_users_clean.json')

try:
    df = cargar_datos_limpios()
except Exception as e:
    st.error("No se pudo cargar el dataset limpio. Asegurate de que el archivo 'streaming_users_clean.json' exista en 'data/processed/'.")
    st.stop()

# Configuración estética global
sns.set_theme(style="whitegrid")


# ==============================================================================
# 1. VISUALIZACIONES UNIVARIADAS
# ==============================================================================
st.header("1. Visualizaciones Univariadas")

# Gráfico 1 
st.subheader("Gráfico 1: Distribución de la Edad de los Usuarios")
    
fig1, ax = plt.subplots(figsize=(10, 4))
sns.histplot(df['age'], bins=20, kde=True, color='skyblue', ax=ax)
ax.set_title('Distribución de Edad de los Usuarios', fontsize=14, fontweight='bold')
ax.set_xlabel('Edad (Años)', fontsize=12)
ax.set_ylabel('Cantidad de Usuarios', fontsize=12)
st.pyplot(fig1)
    
with st.container(border=True):
    st.markdown("**🧐 Pregunta:** ¿Cómo se distribuye la edad en la plataforma?")
    st.markdown("**💡 Interpretación Obligatoria:**")
    st.write("""
    Los usuarios se concentran principalmente entre 25-45 años, 
    con un pico en el rango 30-35 años. La distribución muestra un ligero sesgo hacia la derecha, 
    indicando predominio de adultos jóvenes pero con presencia de usuarios de todas las edades.
    """)

st.markdown("---")

# Gráfico 2
st.subheader("Gráfico 2: Preferencia de Género Favorito")

fig2, ax2 = plt.subplots(figsize=(10, 5))
orden_generos = df['favorite_genre'].value_counts().index
sns.countplot(
    data=df, 
    y='favorite_genre', 
    order=orden_generos, 
    hue='favorite_genre', 
    palette='viridis', 
    legend=False,
    ax=ax2
)
ax.set_title('Distribución de Usuarios por Género Favorito', fontsize=14, fontweight='bold')
ax.set_xlabel('Cantidad de Usuarios', fontsize=12)
ax.set_ylabel('Género Favorito', fontsize=12)
st.pyplot(fig2)

with st.container(border=True):
    st.markdown("**🧐 Pregunta:** ¿Cuáles son los géneros más elegidos por los usuarios y qué relevancia tiene el grupo que decidió no especificar su preferencia?")
    st.markdown("**💡 Interpretación Obligatoria:**")
    st.write("""
    No hay un género claramente dominante; Comedia lidera con ventaja mínima sobre el resto. Las preferencias están muy equilibradas entre todos los géneros. El bajo porcentaje de "No especificado" (3%) confirma que la mayoría declaró su género favorito.
    """)

st.markdown("---")

# ==============================================================================
# 2. VISUALIZACIONES BIVARIADAS
# ==============================================================================
st.header("2. Visualizaciones Bivariadas")

# Gráfico 3
st.subheader("Gráfico 3: Consumo Mensual de Minutos según el Plan de Suscripción")

fig3, ax3 = plt.subplots(figsize=(10, 6))

# Calculamos las medianas por plan y las ordenamos de menor a mayor
orden_planes = df.groupby('subscription_plan')['monthly_watch_time_mins'].median().sort_values().index

sns.boxplot(
    data=df, 
    x='subscription_plan', 
    y='monthly_watch_time_mins', 
    order=orden_planes,
    hue='subscription_plan', 
    palette='Set2', 
    legend=False,
    ax=ax3
)

ax3.set_title('Consumo Mensual de Minutos según el Plan de Suscripción', fontsize=14, fontweight='bold')
ax3.set_xlabel('Plan de Suscripción', fontsize=12)
ax3.set_ylabel('Minutos de Reproducción Mensual', fontsize=12)

plt.tight_layout()
st.pyplot(fig3)

with st.container(border=True):
    st.markdown("**🧐 Pregunta:** ¿Los usuarios del plan Premium realmente consumen más minutos mensuales de contenido que los usuarios de planes inferiores?")
    st.markdown("**💡 Interpretación Obligatoria:**")
    st.write("""
    Se observa una tendencia clara: a mayor plan (Básico → Estándar → Premium), mayor mediana de consumo mensual. Aunque hay solapamiento entre planes, Premium presenta los valores más altos. Todos los planes muestran outliers, evidenciando usuarios con consumo excepcional.
    """)

st.markdown("---")

# Gráfico 4
st.subheader("Gráfico 4: Tickets de Soporte Técnico según el País")

fig4, ax4 = plt.subplots(figsize=(11, 6))

# Ordenamos los géneros por la mediana de minutos de mayor a menor
orden_generos_mins = df.groupby('favorite_genre')['monthly_watch_time_mins'].median().sort_values(ascending=False).index

sns.boxplot(
    data=df,
    y='favorite_genre',
    x='monthly_watch_time_mins',
    order=orden_generos_mins,
    hue='favorite_genre',
    palette='Set3',
    legend=False,
    ax=ax4
)

ax4.set_title('Distribución de Consumo Mensual (Minutos) por Género Favorito', fontsize=14, fontweight='bold')
ax4.set_xlabel('Minutos de Reproducción Mensual', fontsize=12)
ax4.set_ylabel('Género Favorito', fontsize=12)

plt.tight_layout()
st.pyplot(fig4)

with st.container(border=True):
    st.markdown("**🧐 Pregunta:** ¿El género de contenido favorito de los usuarios influye en la cantidad de tiempo que pasan en la plataforma?")
    st.markdown("**💡 Interpretación Obligatoria:**")
    st.write("""
    Los géneros favoritos no influyen en el tiempo de reproducción; todos presentan medianas similares (~700-800 min) y dispersión comparable. Se observan outliers en todas las categorías con consumos superiores a 2,500 minutos, evidenciando usuarios muy activos sin importar su género preferido.
    """)

st.markdown("---")

# ==============================================================================
# 3. VISUALIZACIÓN MULTIVARIADA
# ==============================================================================
st.header("3. Visualización Multivariada")

st.subheader("Gráfico 5: Promedio de Tickets de Soporte por País y Plan de Suscripción")
fig5, ax5 = plt.subplots(figsize=(14, 6))

sns.barplot(
    data=df,
    x='country',
    y='customer_support_tickets',
    hue='subscription_plan',
    palette='Accent',
    errorbar=None,
    ax=ax5
)

ax5.set_title('Promedio de Tickets de Soporte por País y Plan de Suscripción', fontsize=14, fontweight='bold')
ax5.set_xlabel('País', fontsize=12)
ax5.set_ylabel('Promedio de Tickets Enviados', fontsize=12)
ax5.legend(title='Plan de Suscripción')
ax5.set_xticklabels(ax.get_xticklabels(), rotation=15)

plt.tight_layout()
st.pyplot(fig5)

with st.container(border=True):
    st.markdown("**🧐 Pregunta:** ¿Cómo se distribuyen las quejas a soporte técnico según el plan del usuario en cada país?")
    st.markdown("**💡 Interpretación Obligatoria:**")
    st.write("""
    La relación entre tickets de soporte y plan de suscripción cambia según el país. En Perú y Chile, Premium tiene más tickets; en Brasil y México, Premium tiene menos; en Argentina, Estándar lidera. Las diferencias son moderadas pero evidencian patrones regionales distintos.
    """)

# Botón de enlace para avanzar de página de forma nativa
st.markdown("---")
col_btn, _ = st.columns([1, 3])
with col_btn:
    st.page_link("pages/03_PCA.py", label="Ir al Análisis de Componentes Principales (PCA)", icon="🔷", use_container_width=True)

st.caption("Proyecto Integrador · Minería de Datos 1 · ITSE")