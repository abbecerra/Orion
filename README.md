# 🧠 ORION

# Sistema Inteligente de Apoyo a Decisiones Comerciales

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![SERPAPI](https://img.shields.io/badge/SERPAPI-Inteligencia%20de%20Mercado-red)
![CustomTkinter](https://img.shields.io/badge/Interfaz-CustomTkinter-green)
![Streamlit](https://img.shields.io/badge/Monitoreo-Streamlit-orange)
![Estado](https://img.shields.io/badge/Estado-Operativo-success)

### Plataforma Inteligente para el Análisis Estratégico de Mercado y Gestión Comercial

**Autor:** Abraham Becerra Muñoz
**Carrera:** Ingeniería en Informática
**Institución:** Duoc UC
**Asignatura:** Ingeniería de Soluciones de Software con Inteligencia Artificial

</div>

---

# 📌 Introducción

ORION es un sistema inteligente diseñado para apoyar la toma de decisiones comerciales mediante el análisis automatizado de mercados, evaluación de riesgos y generación de estrategias comerciales.

La plataforma integra múltiples componentes de inteligencia artificial, recuperación de información, análisis estadístico y sistemas de observabilidad para proporcionar recomendaciones basadas en datos reales del mercado.

El sistema fue desarrollado utilizando una arquitectura modular basada en agentes especializados, permitiendo una alta escalabilidad, mantenibilidad y resiliencia.

---

# 🎯 Objetivos del Proyecto

## Objetivo General

Desarrollar un sistema inteligente capaz de automatizar procesos de análisis comercial y recomendación estratégica mediante el uso de técnicas de inteligencia artificial y análisis de mercado.

## Objetivos Específicos

* Automatizar el análisis de precios de mercado.
* Incorporar inteligencia comercial basada en datos reales.
* Evaluar riesgos comerciales automáticamente.
* Implementar mecanismos de recuperación ante errores.
* Generar reportes ejecutivos automatizados.
* Implementar sistemas de observabilidad y monitoreo.
* Facilitar la toma de decisiones comerciales.

---

# 🏗 Arquitectura del Sistema

ORION implementa una arquitectura basada en agentes especializados y separación de responsabilidades.

```text
                     USUARIO
                         │
                         ▼
                ┌────────────────┐
                │ Interfaz ORION │
                └────────┬───────┘
                         │
                         ▼
                ┌────────────────┐
                │ Agente ORION   │
                └────────┬───────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Motor de        Motor de Estrategia   Motor de
 Mercado             Comercial          Riesgo
        │                │                │
        └──────────┬─────┴─────┬──────────┘
                   ▼           ▼
              Memoria      Observabilidad
                   │
                   ▼
             Generador PDF
```

---

# 🤖 Sistema Multiagente

La plataforma implementa una arquitectura basada en agentes especializados.

| Agente                | Responsabilidad          |
| --------------------- | ------------------------ |
| Agente Principal      | Coordinación general     |
| Planificador          | Selección de acciones    |
| Motor de Mercado      | Obtención de información |
| Motor Comercial       | Cálculo estratégico      |
| Motor de Riesgo       | Evaluación comercial     |
| Sistema de Memoria    | Persistencia             |
| Sistema de Registro   | Observabilidad           |
| Generador de Reportes | Documentación            |

---

# ⚙ Flujo Operacional

```text
Usuario ingresa producto
            │
            ▼
Validación de datos
            │
            ▼
Corrección automática
            │
            ▼
Consulta de mercado
            │
            ▼
Filtrado inteligente
            │
            ▼
Eliminación de valores atípicos
            │
            ▼
Análisis competitivo
            │
            ▼
Cálculo de estrategia
            │
            ▼
Evaluación de riesgo
            │
            ▼
Generación de reporte
            │
            ▼
Persistencia y monitoreo
```

---

# 🔎 Sistema de Inteligencia de Mercado

ORION obtiene información comercial utilizando Google Shopping mediante SERPAPI.

Para maximizar la recuperación de información, el sistema implementa múltiples estrategias de búsqueda:

```text
Producto + Chile
Producto
Producto + precio
Producto + GPU
Producto + graphics card
```

Además, el sistema incorpora:

* Corrección automática de nombres.
* Recuperación ante búsquedas vacías.
* Bases referenciales.
* Validación de resultados.
* Filtrado inteligente.

---

# 📊 Eliminación de Valores Atípicos

ORION implementa el algoritmo estadístico IQR (Interquartile Range) para eliminar precios anómalos.

```text
Q1 = Percentil 25
Q3 = Percentil 75

IQR = Q3 − Q1

Mínimo = Q1 − 1.5(IQR)
Máximo = Q3 + 1.5(IQR)
```

Este mecanismo permite eliminar:

* Productos incorrectos.
* Equipos armados.
* Combos comerciales.
* Accesorios.
* Precios anómalos.
* Resultados erróneos.

---

# 💰 Motor de Estrategias Comerciales

El sistema calcula automáticamente:

```text
Costo Total
=
Costo de Compra + Costo de Envío
```

```text
Precio Mínimo
=
Costo Total × Margen Objetivo
```

El sistema implementa tres estrategias comerciales.

## Estrategia Competitiva

Aplicada cuando el precio calculado es significativamente inferior al mercado.

Objetivo:

* Maximizar competitividad.

---

## Estrategia de Mercado

Aplicada cuando el precio calculado es similar al mercado.

Objetivo:

* Mantener equilibrio comercial.

---

## Estrategia de Supervivencia

Aplicada cuando el costo supera el precio promedio del mercado.

Objetivo:

* Garantizar rentabilidad mínima.

---

# ⚠ Sistema de Evaluación de Riesgo

ORION evalúa múltiples variables comerciales:

* Competencia.
* Rentabilidad.
* Margen.
* Factibilidad comercial.
* Condiciones del mercado.

La clasificación del riesgo se realiza mediante puntajes.

| Puntaje  | Riesgo |
| -------- | ------ |
| 80 - 100 | Bajo   |
| 60 - 79  | Medio  |
| 0 - 59   | Alto   |

---

# 💾 Sistema de Memoria

El sistema mantiene persistencia local de información para permitir:

* Historial de consultas.
* Recuperación de información.
* Auditoría.
* Trazabilidad.

Archivos utilizados:

```text
data/
    memory.json
```

---

# 📈 Sistema de Observabilidad y Monitoreo

ORION incorpora mecanismos de observabilidad para supervisar el comportamiento del sistema.

La plataforma registra:

* Consultas realizadas.
* Latencia.
* Errores.
* Rendimiento.
* Operaciones ejecutadas.

Archivos utilizados:

```text
logs/
    orion_logs.csv
```

---

# 📊 Panel de Monitoreo

El sistema incorpora un panel de monitoreo desarrollado mediante Streamlit.

El panel permite visualizar:

* Historial de consultas.
* Latencias.
* Rendimiento del sistema.
* Errores.
* Métricas operacionales.

### Ejecución del panel:

```bash
streamlit run dashboard.py
```

---

# 📄 Generación Automática de Reportes

ORION genera automáticamente reportes ejecutivos con:

* Información del producto.
* Precio de mercado.
* Estrategia comercial.
* Evaluación de riesgo.
* Justificación.
* Métricas operacionales.

Los reportes son almacenados en:

```text
reports/
```

---

# 🛡 Validaciones Implementadas

## Validaciones de entrada

* Producto vacío.
* Costos negativos.
* Márgenes negativos.
* Márgenes excesivos.

## Validaciones comerciales

* Productos inexistentes.
* Productos imposibles.
* Resultados anómalos.
* Productos incorrectos.

## Validaciones estadísticas

* Eliminación de valores atípicos.
* Validación de competencia.
* Filtrado de ruido.

---

# 🔄 Recuperación Ante Errores

ORION implementa mecanismos de resiliencia mediante:

* Búsquedas alternativas.
* Corrección automática.
* Bases referenciales.
* Recuperación de consultas.
* Manejo de excepciones.
* Registro de errores.

---

# 🖥 Interfaz Principal

La interfaz principal fue desarrollada utilizando CustomTkinter.

Características:

* Tema oscuro.
* Interfaz amigable.
* Procesamiento asíncrono.
* Indicadores de estado.
* Manejo de errores.
* Visualización de resultados.

### Ejecución:

```bash
python app.py
```

---

# 📚 Tecnologías Utilizadas

| Tecnología    | Función                   |
| ------------- | ------------------------- |
| Python 3.11   | Desarrollo principal      |
| CustomTkinter | Interfaz gráfica          |
| Streamlit     | Monitoreo                 |
| SERPAPI       | Inteligencia de mercado   |
| ReportLab     | Reportes                  |
| JSON          | Persistencia              |
| CSV           | Observabilidad            |
| Threading     | Procesamiento concurrente |
| Git           | Control de versiones      |
| GitHub        | Repositorio               |

---

# 📂 Estructura del Proyecto

```text
ORION/

├── assets/
├── data/
├── logs/
├── reports/

├── agent.py
├── app.py
├── dashboard.py
├── logger.py
├── market_search.py
├── memory.py
├── planner.py
├── recommendations.py
├── report_generator.py
├── tools.py

├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Instalación

```bash
git clone https://github.com/abbecerra/Orion

cd Orion

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

# ▶ Ejecución

## Interfaz principal

```bash
python app.py
```

## Panel de monitoreo

```bash
streamlit run dashboard.py
```

---

# 🧪 Casos de Prueba

Ejemplos de productos utilizados:

```text
RTX 4060
RTX 5070
RTX 4090
GTX 1650
Ryzen 9800X3D
Ryzen 7600
iPhone 17
Samsung Galaxy S26
PlayStation 5 Pro
```

---

# 📈 Funcionalidades Implementadas

✅ Arquitectura multiagente
✅ Inteligencia de mercado
✅ Estrategias comerciales
✅ Evaluación de riesgo
✅ Eliminación de valores atípicos
✅ Recuperación automática
✅ Persistencia
✅ Observabilidad
✅ Panel de monitoreo
✅ Reportes automáticos
✅ Manejo de errores
✅ Validaciones avanzadas

---

# 🔮 Trabajo Futuro

* Incorporación de aprendizaje automático.
* Predicción de precios.
* Integración con bases de datos.
* Servicios web.
* API REST.
* Analítica avanzada.

---

# 👨‍💻 Autor

**Abraham Becerra Muñoz**

Ingeniería en Informática
Duoc UC

---

# 📜 Licencia

Proyecto desarrollado con fines académicos para la asignatura:

**Ingeniería de Soluciones de Software con Inteligencia Artificial**
