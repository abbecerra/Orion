# 🧠 ORION AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green)
![SERPAPI](https://img.shields.io/badge/Market-SERPAPI-red)
![PDF](https://img.shields.io/badge/Reports-PDF-orange)
![Status](https://img.shields.io/badge/Status-Production-success)

### Plataforma Inteligente de Análisis Estratégico de Precios

**Autor:** Abraham Becerra Muñoz
**Carrera:** Ingeniería en Informática
**Institución:** Duoc UC
**Asignatura:** Ingeniería de Soluciones de Software con Inteligencia Artificial

</div>

---

# 📌 Descripción del Proyecto

ORION AI es una plataforma inteligente orientada a la automatización de procesos de análisis comercial y pricing estratégico.

El sistema integra múltiples componentes de inteligencia artificial, análisis estadístico y recuperación de información de mercado para generar recomendaciones comerciales automáticas basadas en datos reales.

La plataforma permite:

* Obtener precios reales desde internet.
* Analizar competencia.
* Determinar estrategias comerciales.
* Calcular precios recomendados.
* Evaluar riesgos comerciales.
* Generar reportes ejecutivos.
* Mantener historial y memoria de análisis.

---

# 🎯 Objetivos

## Objetivo General

Desarrollar una plataforma inteligente capaz de asistir procesos de pricing mediante técnicas de inteligencia artificial y análisis de mercado automatizado.

## Objetivos Específicos

* Automatizar el análisis de precios.
* Reducir errores humanos.
* Incorporar inteligencia comercial.
* Implementar validaciones automáticas.
* Generar recomendaciones de pricing.
* Evaluar riesgo de mercado.
* Producir reportes ejecutivos.

---

# 🧠 Arquitectura del Sistema

```text
                     USUARIO
                         │
                         ▼
                ┌────────────────┐
                │ ORION GUI      │
                └────────┬───────┘
                         │
                         ▼
                ┌────────────────┐
                │ AGENTE ORION   │
                └────────┬───────┘
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 Market Search     Pricing Engine     Risk Engine
       │                 │                 │
       └──────────┬──────┴──────┬──────────┘
                  ▼             ▼
               Memory         Logger
                  │
                  ▼
            PDF Generator
```

---

# ⚙ Flujo Operacional

```text
Usuario ingresa producto
            │
            ▼
Validación de entrada
            │
            ▼
Corrección automática
            │
            ▼
Búsqueda Google Shopping
            │
            ▼
Filtrado inteligente
            │
            ▼
Eliminación de outliers
            │
            ▼
Análisis de mercado
            │
            ▼
Estrategia comercial
            │
            ▼
Evaluación de riesgo
            │
            ▼
Generación PDF
            │
            ▼
Persistencia
```

---

# 🤖 Sistema Multiagente

ORION implementa una arquitectura basada en agentes especializados.

| Agente         | Función                 |
| -------------- | ----------------------- |
| Planner        | Planificación           |
| Market Search  | Inteligencia de mercado |
| Pricing Engine | Optimización de precios |
| Risk Engine    | Evaluación de riesgo    |
| Memory Agent   | Persistencia            |
| Logger Agent   | Observabilidad          |
| Report Agent   | Reportería              |

---

# 🔍 Sistema de Inteligencia de Mercado

ORION utiliza Google Shopping mediante SERPAPI.

### Estrategias de búsqueda:

```text
Producto + Chile
Producto
Producto + precio
Producto + gpu
Producto + graphics card
```

### Recuperación automática:

* Corrección RTX ↔ GTX.
* Fallback de mercado.
* Base referencial.
* Filtrado estadístico.
* Recuperación ante errores.

---

# 📊 Eliminación de Outliers

ORION implementa el algoritmo estadístico IQR.

```text
Q1 = Percentil 25
Q3 = Percentil 75

IQR = Q3 − Q1

Mínimo = Q1 − 1.5(IQR)
Máximo = Q3 + 1.5(IQR)
```

Este método elimina:

* Productos erróneos.
* Equipos armados.
* Bundles.
* Precios anómalos.
* Resultados irreales.

---

# 💰 Motor de Pricing

El sistema calcula:

```text
Costo total
=
Costo compra + envío
```

```text
Precio mínimo rentable
=
Costo total × margen objetivo
```

### Estrategias implementadas

#### Competitivo

```text
Precio mínimo ≤ 85% mercado
```

Objetivo:

* Maximizar competitividad.

---

#### Mercado

```text
Precio mínimo ≈ mercado
```

Objetivo:

* Mantener equilibrio.

---

#### Supervivencia

```text
Costo > mercado
```

Objetivo:

* Mantener rentabilidad mínima.

---

# ⚠ Sistema de Riesgo

Variables evaluadas:

* Competencia.
* Rentabilidad.
* Margen.
* Factibilidad.

Clasificación:

| Score  | Riesgo |
| ------ | ------ |
| 80-100 | Bajo   |
| 60-79  | Medio  |
| 0-59   | Alto   |

---

# 🛡 Validaciones Implementadas

### Producto

* Productos imposibles.
* Correcciones automáticas.
* Coincidencia inteligente.

### Mercado

* Eliminación de ruido.
* Filtrado de notebooks.
* Filtrado de PC gamer.
* Filtrado de bundles.

### Usuario

* Costos negativos.
* Márgenes inválidos.
* Valores extremos.

---

# 💾 Persistencia

```text
data/
    memory.json

logs/
    orion_logs.csv

reports/
    reportes PDF
```

---

# 📄 Reportes

ORION genera automáticamente:

* Reporte comercial.
* Estrategia aplicada.
* Evaluación de riesgo.
* Justificación.
* Métricas de rendimiento.
* Reporte PDF.

---

# 🖥 Interfaz Gráfica

Desarrollada utilizando:

```text
CustomTkinter
```

Características:

* Tema oscuro.
* Indicadores de estado.
* Procesamiento asíncrono.
* Manejo de errores.
* Reportes interactivos.

---

# 📚 Tecnologías Utilizadas

| Tecnología    | Uso                 |
| ------------- | ------------------- |
| Python 3.11   | Backend             |
| CustomTkinter | GUI                 |
| SERPAPI       | Market Intelligence |
| ReportLab     | PDF                 |
| JSON          | Persistencia        |
| CSV           | Logging             |
| Threading     | Paralelismo         |

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

python app.py
```

---

# 🧪 Casos de Prueba

```text
RTX 4060
RTX 5070
RTX 4090
GTX 1650
Ryzen 9800X3D
iPhone 17
Samsung Galaxy S26
PlayStation 5 Pro
```

---

# 📈 Características Implementadas

✅ Multi-Agent System
✅ Strategic Pricing
✅ Market Intelligence
✅ SERPAPI Integration
✅ Statistical Filtering
✅ Outlier Detection
✅ Risk Analysis
✅ Memory System
✅ Logger System
✅ Dashboard
✅ PDF Reports
✅ Recovery System
✅ Reference Database
✅ Error Handling
✅ Persistence Layer

---

# 🔮 Mejoras Futuras

* Machine Learning Predictivo.
* Forecasting de precios.
* Integración ERP.
* Base de datos SQL.
* API REST.
* Dashboard web.
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
