# 📊 Proyecto Integrador - Minería de Datos 1

## Análisis de Comportamiento y Reducción de Dimensionalidad en Usuarios de Streaming

---

## 📌 Información General

| | |
|---|---|
| **Institución** | Instituto Tecnológico de Santiago del Estero |
| **Materia** | Minería de Datos 1 |
| **Fecha** | Julio 2026 |
| **Integrante** | Pinto Villegas, Eduardo Joaquín |

---

# 🎯 Objetivo del Proyecto

El objetivo de este proyecto es aplicar los fundamentos de **Minería de Datos** para construir un pipeline analítico reproducible, justificando metodológicamente cada decisión mediante evidencia empírica.

Durante el desarrollo se implementan las siguientes etapas:

- Inspección inicial del dataset.
- Proceso ETL de limpieza y preparación de datos.
- Análisis Exploratorio de Datos (EDA).
- Escalamiento de variables.
- Reducción de dimensionalidad mediante **PCA**.
- Desarrollo de una aplicación interactiva en **Streamlit** para comunicar los resultados.

---

# 📂 Dataset

El dataset original se encuentra en:

```
data/raw/streaming_users_dirty.json
```

### Características

- **Registros iniciales:** 8.160 usuarios
- **Variables:** 8
- **Formato:** JSON

Las variables analizadas incluyen:

| Variable | Descripción |
| :--- | :--- |
| `user_id` | Identificador único de usuario |
| `age` | Edad del usuario |
| `subscription_plan` | Plan contratado |
| `monthly_watch_time_mins` | Minutos vistos mensuales |
| `country` | País de residencia |
| `favorite_genre` | Género cinematográfico favorito |
| `last_login_date` | Última fecha de inicio de sesión |
| `customer_support_tickets` | Reclamos realizados |

El conjunto de datos presentaba duplicados, valores faltantes, errores de formato y registros inconsistentes, los cuales fueron corregidos durante el proceso ETL.

---

# 📁 Estructura del Proyecto

```text
PI_Mineria_Datos_1/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
│
├── reports/
│   └── informe_final.pdf
│
└── logs/
    └── pipeline_log.csv
```

---

# 🧹 Preparación y Calidad de Datos

El proceso completo se encuentra documentado en:

```
notebooks/02_calidad_y_limpieza.ipynb
```

### Principales tareas realizadas

- Eliminación de **128 registros duplicados**.
- Corrección de fechas inválidas.
- Imputación de valores faltantes.
- Tratamiento de outliers mediante **clipping (3 × IQR)**.
- Corrección de edades imposibles.
- Exportación del dataset limpio.

### Resultado

| Métrica | Valor |
|---------|-------|
| Registros iniciales | 8.160 |
| Registros finales | 7.633 |
| Retención de datos | **93.54 %** |

---

# 📈 Análisis Exploratorio (EDA)

El análisis exploratorio se desarrolló en:

```
notebooks/03_eda.ipynb
```

Entre los principales hallazgos se destacan:

- La mayor parte de los usuarios tiene entre **25 y 45 años**.
- Las preferencias por género cinematográfico son bastante equilibradas.
- Los usuarios Premium consumen significativamente más minutos de contenido.
- Existen diferencias regionales en la cantidad de tickets de soporte técnico.

---

# 📉 Reducción de Dimensionalidad (PCA)

El análisis fue realizado en:

```
notebooks/04_pca.ipynb
```

Previo al PCA se aplicó un **escalamiento estándar (Z-Score)**.

### Varianza explicada

| Componente | Varianza |
|------------|----------|
| PC1 | 33.79 % |
| PC2 | 33.12 % |
| PC3 | 33.09 % |

El análisis permitió identificar tres perfiles principales de usuarios:

- **PC1:** Actividad general del usuario.
- **PC2:** Usuarios jóvenes con mayor interacción con soporte.
- **PC3:** Usuarios con alto consumo y baja utilización del soporte técnico.

---

# 🌐 Aplicación Interactiva

El proyecto incluye una aplicación desarrollada en **Streamlit** que permite explorar los resultados del análisis mediante visualizaciones interactivas.

### Incluye

- Exploración del dataset.
- EDA interactivo.
- Visualización de PCA.
- Conclusiones del proyecto.

🔗 **Aplicación:**

> [*(Enlace de Streamlit Cloud.)*](https://pimineriadatos1-3hg93urnsydbmbrxjpbn8l.streamlit.app/)

---

# ▶️ Ejecución Local

Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/PI_Mineria_Datos_1.git
```

Ingresar al proyecto

```bash
cd PI_Mineria_Datos_1
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación

```bash
streamlit run app/Home.py
```

---

# ✅ Conclusiones

El proyecto permitió construir un pipeline analítico completo y reproducible para el análisis de usuarios de una plataforma de streaming.

Entre los principales resultados se destacan:

- Se obtuvo un dataset limpio con una retención del **93.54 %** de los registros.
- Los usuarios Premium presentan el mayor nivel de consumo.
- El comportamiento del soporte técnico varía entre países.
- El PCA permitió identificar tres perfiles representativos de usuarios sin perder interpretabilidad.
- El trabajo constituye una base sólida para futuros modelos de **Clustering**, predicción de **Churn**.

---

## 🛠️ Tecnologías utilizadas

- Python
- NumPy
- Matplotlib
- Pandas
- Scikit-Learn
- Streamlit