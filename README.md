# 🧠💼 ORION v2 — Sistema Inteligente de Análisis Estratégico Empresarial

## 📌 Descripción
ORION v2 es un agente inteligente basado en inteligencia artificial diseñado para realizar análisis estratégicos empresariales y de mercado.

El sistema simula el comportamiento de una consultora estratégica empresarial, permitiendo evaluar organizaciones, identificar riesgos competitivos, analizar fortalezas y debilidades, comparar empresas reales y generar recomendaciones estratégicas fundamentadas.

La solución implementa una arquitectura híbrida basada en Retrieval-Augmented Generation (RAG), combinando recuperación de conocimiento interno, búsqueda web externa, memoria conversacional y generación de respuestas mediante modelos de lenguaje.

Además, el sistema incorpora una interfaz gráfica de escritorio, permitiendo una experiencia más profesional e intuitiva para el usuario.

---

## 🎯 Objetivo del proyecto
Desarrollar un agente inteligente organizacional capaz de apoyar procesos de análisis estratégico empresarial mediante inteligencia artificial, recuperación contextual, memoria conversacional y herramientas externas de consulta.

El proyecto busca aplicar conceptos de:

- agentes inteligentes
- planificación
- orquestación
- retrieval augmented generation (RAG)
- memoria contextual
- interfaces de usuario

---

## ⚙️ Funcionamiento del sistema
El flujo de funcionamiento de ORION v2 es el siguiente:

1. El usuario ingresa una consulta desde la interfaz gráfica
2. El sistema analiza el tipo de consulta
3. Determina dinámicamente qué fuente utilizar:
   - Base de conocimiento interna (FAISS)
   - Búsqueda web externa (DuckDuckGo)
4. Recupera el contexto relevante
5. Integra memoria conversacional cuando corresponde
6. Construye un prompt estratégico
7. Envía la consulta al modelo LLM
8. Genera una respuesta empresarial estructurada

---

## 🧠 Modelo utilizado
ORION v2 utiliza un modelo de lenguaje ejecutado localmente mediante **Ollama**, específicamente:

**Modelo principal:**
- Llama 3

Para generación de embeddings semánticos:

**Modelo de embeddings:**
- sentence-transformers/all-MiniLM-L6-v2

---

## 📌 Justificación técnica
La arquitectura fue seleccionada considerando:

- ejecución local sin depender de APIs pagadas
- mayor reproducibilidad académica
- privacidad de los datos
- flexibilidad para integrar múltiples herramientas
- bajo costo operativo
- facilidad de expansión futura

---

## 🧠 Memoria utilizada
ORION implementa memoria conversacional de corto plazo mediante:

**ConversationBufferMemory**

Esto permite:

- recordar interacciones anteriores
- mantener coherencia contextual
- generar respuestas más consistentes en consultas relacionadas

### Tipos de memoria

**Memoria de corto plazo**
- historial conversacional
- contexto reciente de interacción

**Memoria contextual**
- recuperación dinámica mediante FAISS

---

## 📋 Planificación implementada
ORION utiliza planificación condicional.

El sistema analiza la intención de la consulta y decide dinámicamente qué herramienta utilizar.

### Ejemplos
**Consulta interna**
```text
Analiza TechZone
```

→ usa FAISS

---

**Consulta externa**
```text
Compara Samsung con Apple
```

→ usa búsqueda web

---

Este enfoque permite optimizar:

- velocidad
- precisión
- uso eficiente del contexto

---

## 🔄 Orquestación del sistema
La orquestación del sistema se realiza mediante **LangChain**.

LangChain coordina:

- carga documental
- fragmentación de texto
- embeddings
- base vectorial FAISS
- memoria conversacional
- búsqueda externa
- construcción de prompts
- conexión con LLM

Esto permite una arquitectura modular, organizada y mantenible.

---

## 🏗️ Arquitectura del sistema

```text
Usuario
   ↓
Interfaz gráfica (CustomTkinter)
   ↓
Planificador de consulta
   ↓
¿Consulta interna o externa?
   ↓
┌───────────────┬───────────────┐
│               │               │
FAISS        DuckDuckGo Web Search
│               │
└───────────────┴───────────────┘
   ↓
Memoria conversacional
   ↓
Construcción de prompt
   ↓
Llama 3 (Ollama)
   ↓
Respuesta estratégica
```

---

## 🛠️ Tecnologías utilizadas
- Python
- LangChain
- LangChain Community
- FAISS
- Sentence Transformers
- Hugging Face
- Ollama
- Llama 3
- DuckDuckGo Search (DDGS)
- CustomTkinter

---

## 📂 Estructura del proyecto

```text
ORION/
│── main.py
│── app.py
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

---

### 2. Crear entorno virtual
```bash
python -m venv venv
```

---

### 3. Activar entorno virtual (Windows)
```bash
venv\Scripts\activate
```

---

### 4. Instalar dependencias
```bash
python -m pip install -r requirements.txt
```

---

### 5. Instalar Ollama
Descargar desde:

https://ollama.com

---

### 6. Descargar modelo
```bash
ollama pull llama3
```

---

### 7. Ejecutar aplicación
```bash
python app.py
```

---

## 💬 Ejemplos de uso

### Consultas internas
- Analiza TechZone
- ¿Qué riesgos presenta Econotech?
- Compara LuxPhone con TechZone

### Consultas externas
- Analiza Tesla
- Compara Samsung con Apple
- Analiza Amazon
- Evalúa Microsoft frente a Google

---

## 📊 Ejemplo de respuesta
```text
1. Diagnóstico general
2. Fortalezas
3. Debilidades
4. Riesgos competitivos
5. Recomendación estratégica
```

---

## 📈 Optimizaciones implementadas
El sistema incorpora mejoras para eficiencia:

- retrieval selectivo
- planificación condicional
- memoria contextual controlada
- separación entre consultas internas y externas
- control básico anti alucinación

---

## 🔮 Posibles mejoras futuras
- persistencia de memoria a largo plazo
- integración con APIs empresariales
- dashboards analíticos
- exportación PDF
- integración con bases SQL
- multiagentes especializados
- scoring cuantitativo avanzado

---

## 👤 Autor
**Abraham Becerra**


---

## 📌 Reproducibilidad
El proyecto incluye:

✅ código fuente completo  
✅ requirements con versiones  
✅ instrucciones de instalación  
✅ modelo documentado  
✅ ejecución local reproducible  
✅ interfaz gráfica funcional  

Esto permite que terceros puedan ejecutar el sistema fuera del entorno original.