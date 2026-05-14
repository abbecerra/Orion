# 🧠💼 ORION — Sistema de Inteligencia Competitiva IA

## 📌 Descripción
ORION es un sistema basado en inteligencia artificial diseñado para analizar información empresarial y generar respuestas estratégicas a partir de un contexto definido. El objetivo del proyecto es simular el trabajo de una consultora estratégica, permitiendo evaluar fortalezas, debilidades, riesgos competitivos y posibles estrategias de mejora para distintas empresas.

El sistema implementa una arquitectura basada en Retrieval-Augmented Generation (RAG), utilizando recuperación contextual mediante embeddings y búsqueda vectorial.

---

## ⚙️ Funcionamiento del sistema

El flujo general del sistema funciona de la siguiente manera:

1. Carga información desde un archivo de conocimiento (`competidores.txt`)
2. Divide el contenido en fragmentos de texto
3. Genera embeddings (representaciones vectoriales del contenido)
4. Almacena los vectores en una base FAISS
5. Permite al usuario realizar consultas estratégicas
6. Recupera el contexto más relevante mediante similarity search
7. Construye un prompt estratégico
8. Envía la consulta al modelo de lenguaje
9. Genera una respuesta estructurada

---

## 🔄 Flujo del sistema

```text
┌─────────────┐
│   Usuario   │
└──────┬──────┘
       ↓
┌────────────────────┐
│ Consulta ingresada │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Búsqueda en FAISS  │
│ (similarity search)│
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Recuperación de    │
│ contexto relevante │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Construcción del   │
│ prompt estratégico │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│   Modelo LLM       │
│   (Ollama/Llama3)  │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Respuesta final    │
└────────────────────┘
```

---

## 🛠️ Tecnologías utilizadas

- Python
- LangChain
- Hugging Face Transformers
- Sentence Transformers
- FAISS
- Ollama
- Llama3

---

## 📂 Estructura del proyecto

```text
ORION/
│── main.py
│── competidores.txt
│── requirements.txt
│── README.md
```

---

## 🚀 Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone https://github.com/abbecerra/Orion.git
cd Orion
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual (Windows)

```bash
venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar programa

```bash
python main.py
```

---

## 💬 Ejemplos de consultas

- ¿Debilidades de Empresa B?
- ¿Qué estrategia recomendarías a Empresa A?
- ¿Qué empresa tiene mayor riesgo de perder mercado?
- ¿Qué empresa compite solo por precio?
- ¿Cuál empresa tiene mejor posicionamiento estratégico?

---

## 📊 Ejemplo de uso

**Consulta:**

```text
¿Qué empresa tiene mayor riesgo de perder mercado?
```

**Respuesta esperada:**

```text
Econotech presenta el mayor riesgo debido a su alta dependencia del precio, baja diferenciación y mala percepción de calidad.
```

---

## 🎯 Objetivo del proyecto

Desarrollar una herramienta capaz de automatizar el análisis competitivo empresarial utilizando inteligencia artificial y recuperación contextual.

---

## 📈 Posibles mejoras futuras

- Integración con herramientas web externas
- Uso de modelos más avanzados
- Implementación de memoria conversacional
- Interfaz gráfica para usuarios
- Soporte para documentos PDF o bases de datos empresariales

---

## 👤 Autor

**Abraham Becerra**

---

## 📌 Nota

Para ejecutar correctamente el proyecto es necesario:

- Tener Python instalado
- Instalar las dependencias desde `requirements.txt`
- Tener Ollama instalado localmente
- Descargar previamente el modelo `llama3`

Ejemplo:

```bash
ollama run llama3
```