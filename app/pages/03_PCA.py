import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(
    page_title="PCA — Minería de Datos 1",
    page_icon="🔷",
    layout="wide"
)

st.title("🔷 Análisis de Componentes Principales (PCA)")
st.markdown("---")

# 📥 Carga del dataset limpio
@st.cache_data
def cargar_datos_clean():
    return pd.read_json('../data/processed/streaming_users_clean.json')

try:
    df = cargar_datos_clean()
except Exception as e:
    st.error("No se pudo cargar el dataset limpio. Asegurate de que el archivo 'streaming_users_clean.json' exista en 'data/processed/'.")
    st.stop()


# ==============================================================================
# 1. CONFIGURACIÓN Y ESCALAMIENTO
# ==============================================================================
st.header("1. Configuración del Modelo y Escalamiento")

col_conf1, col_conf2 = st.columns([2, 1], gap="large")

with col_conf1:
    st.markdown("""
    **Propósito del Análisis:** Reducir las dimensiones de comportamiento de los usuarios para identificar si existen **"perfiles sintéticos"** que sinteticen su actividad general dentro de la plataforma de streaming.
    
    **Variables Numéricas Seleccionadas:** Para el modelado numérico se aislaron las 3 variables cuantitativas continuas y discretas de comportamiento:
    * `age` (Edad del usuario)
    * `monthly_watch_time_mins` (Minutos de reproducción mensuales)
    * `customer_support_tickets` (Cantidad de reclamos de soporte técnico)
    """)

with col_conf2:
    with st.container(border=True):
        st.markdown("##### ⚙️ Preprocesamiento")
        st.markdown("**Escalamiento Aplicado:** `StandardScaler` (Z-score)")
        st.write("Es un paso crítico dado que las variables poseen escalas drásticamente diferentes (los minutos van de 0 a 2700, mientras que los tickets varían entre 0 y 5). Sin este escalamiento, los minutos dominarían artificialmente la varianza.")

# Ejecución del Pipeline matemático de PCA en tiempo real para la app
features = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Armamos un DF de loadings para las explicaciones
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3'], index=features)


# ==============================================================================
# 2. VARIANZA EXPLICADA Y VISUALIZACIONES (MÁXIMO 2)
# ==============================================================================
st.markdown("---")
st.header("2. Varianza Explicada y Gráficos")

# Gráfico 1: Scree Plot
st.subheader("Gráfico 1: Scree Plot (Varianza Explicada)")

# Varianza explicada
var_explicada = pca.explained_variance_ratio_
var_acumulada = np.cumsum(var_explicada)

# Crear resumen_pca
resumen_pca = pd.DataFrame({
    "Componente": [f'PC{i+1}' for i in range(3)],
    "Varianza explicada (%)": np.round(var_explicada * 100, 2),
    "Varianza acumulada (%)": np.round(var_acumulada * 100, 2)
})

# Creamos la figura
fig1, ax1 = plt.subplots(figsize=(8, 5))

# 1. Dibujamos las barras para la varianza de cada PC
bars = ax1.bar(resumen_pca["Componente"], resumen_pca["Varianza explicada (%)"], 
               color="skyblue", alpha=0.8, label="Varianza Individual")

# 2. Dibujamos la línea del acumulado
ax1.plot(resumen_pca["Componente"], resumen_pca["Varianza acumulada (%)"], 
         color="orange", marker="o", linewidth=2, label="Varianza Acumulada")

# Agregamos los números arriba de las barras
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
             f"{height:.1f}%", ha="center", va="bottom", fontsize=10)

# Configuraciones estéticas
ax1.set_title("Análisis de Varianza Explicada por Componente (PCA)", fontsize=13, pad=15)
ax1.set_ylabel("Porcentaje (%)")
ax1.set_ylim(0, 110)
ax1.grid(axis="y", linestyle="--", alpha=0.5)
ax1.legend(loc="upper left")

plt.tight_layout()
st.pyplot(fig1)

# Métrica adicional
st.metric(label="📊 Varianza Acumulada (PC1 + PC2)", value=f"{var_acumulada[1]*100:.2f}%")
st.markdown("---")

# Gráfico 2: Heatmap de Loadings
st.subheader("Gráfico 2: Matriz de Cargas (Loadings Heatmap)")

# 1. Creamos un DataFrame con las cargas (componentes de PCA)
loadings = pd.DataFrame(
    pca.components_.T, 
    columns=[f'PC{i+1}' for i in range(3)], 
    index=['age', 'monthly_watch_time_mins', 'customer_support_tickets']
)

# 2. Armamos el Heatmap
fig2, ax2 = plt.subplots(figsize=(7, 5))
sns.heatmap(loadings, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, cbar=True, ax=ax2)

# Estética del gráfico
ax2.set_title('Interpretación de Componentes: Peso de cada Variable (Loadings)', fontsize=12, pad=15)
ax2.set_ylabel('Variables Originales')
ax2.set_xlabel('Componentes Principales')

plt.tight_layout()
st.pyplot(fig2)

# ==============================================================================
# 3. INTERPRETACIÓN DE LOS COMPONENTES
# ==============================================================================
st.markdown("---")
st.header("3. Interpretación de los Componentes Principales")

tab_pc1, tab_pc2, tab_pc3 = st.tabs(["🔷 PC1: Actividad General", "🔷 PC2: Fricción Técnica", "🔷 PC3: Consumo Intensivo"])

with tab_pc1:
    st.markdown(f"### **PC1 — Actividad General (Explica el {var_explicada[0]*100:.2f}%)**")
    st.write("""
    Este primer componente presenta cargas positivas moderadas y estables en todas las variables analizadas por igual: 
    edad, minutos de reproducción y tickets enviados. 
    
    **Interpretación:** Representa un eje de **volumen o nivel de actividad general** del usuario dentro del ecosistema de la plataforma. 
    A mayor valor en este componente, mayor es la presencia integral del usuario, sin distinguir un comportamiento en particular, 
    reflejando simplemente la antigüedad o escala de interacción.
    """)

with tab_pc2:
    st.markdown(f"### **PC2 — Fricción Técnica / Perfil Joven Demandante (Explica el {var_explicada[1]*100:.2f}%)**")
    st.write("""
    Este componente se caracteriza por tener una carga fuertemente positiva en la variable `customer_support_tickets` y una relación marcadamente inversa (negativa) con respecto a la edad (`age`).
    
    **Interpretación:** Describe un contraste generacional claro. Identifica un perfil de **usuarios relativamente jóvenes que presentan una alta tasa de fricción operativa** o interacción recurrente con el soporte técnico de la plataforma, contrapuesto a usuarios de mayor edad con menor actividad de reclamos.
    """)

with tab_pc3:
    st.markdown(f"### **PC3 — Consumo Intensivo Silencioso (Explica el {var_explicada[2]*100:.2f}%)**")
    st.write("""
    El tercer componente está fuertemente asociado de manera positiva al tiempo mensual de visualización (`monthly_watch_time_mins`), relacionándose de forma negativa con la edad y con los tickets de soporte.
    
    **Interpretación:** Puede interpretarse claramente como un segmento de **usuarios jóvenes de consumo intensivo**. Son perfiles con altos niveles de permanencia devorando contenidos en la pantalla, pero que registran muy baja o nula interacción con el servicio de soporte técnico (consumidores pesados pero independientes).
    """)


# Botón final para ir a las Conclusiones
st.markdown("---")
col_btn, _ = st.columns([1, 3])
with col_btn:
    st.page_link("pages/04_Conclusiones.py", label="Ir a las Conclusiones Finales", icon="📝", use_container_width=True)

st.caption("Proyecto Integrador · Minería de Datos 1 · ITSE")