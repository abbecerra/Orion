# 🧠💼 ORION — Sistema de Inteligencia Competitiva IA

## 📌 Descripción
ORION es un agente inteligente basado en inteligencia artificial diseñado para analizar información empresarial y generar respuestas estratégicas a partir de un contexto definido.

El sistema simula el trabajo de una consultora estratégica, permitiendo identificar fortalezas, debilidades, riesgos competitivos y oportunidades de mejora mediante herramientas de consulta, razonamiento y generación de respuestas automáticas.

Este proyecto fue desarrollado como parte de una evaluación académica orientada al diseño de agentes funcionales con capacidades de memoria, planificación y orquestación.

## 🎯 Objetivo del proyecto
Desarrollar un agente inteligente capaz de apoyar procesos de análisis competitivo empresarial mediante inteligencia artificial, automatizando la consulta, interpretación y generación de recomendaciones estratégicas.

## ⚙️ Funcionamiento del sistema
El flujo de funcionamiento de ORION es el siguiente:

1. Carga información desde un archivo de contexto (`competidores.txt`)
2. Divide el contenido en fragmentos semánticos
3. Genera embeddings vectoriales del contenido
4. Almacena la información en una base vectorial FAISS
5. Recibe consultas del usuario
6. Recupera el contexto más relevante
7. Envía la información al modelo de lenguaje
8. Genera una respuesta estratégica basada en el contexto recuperado

## 🧠 Modelo utilizado
ORION utiliza un modelo de lenguaje ejecutado localmente mediante **Ollama**, integrado a través de **LangChain**.

Además, utiliza modelos **Sentence Transformers** para la generación de embeddings semánticos.

### Justificación
La elección de esta arquitectura responde a:

- Ejecución local sin dependencia de APIs externas
- Mayor reproducibilidad para evaluación académica
- Menor costo operativo
- Privacidad de la información procesada
- Facilidad de integración con herramientas de recuperación contextual

## 🧠 Memoria utilizada
ORION implementa memoria contextual mediante almacenamiento vectorial usando **FAISS**.

El contenido empresarial cargado es transformado en embeddings semánticos y almacenado en una base vectorial, permitiendo que el agente recupere información relevante durante las consultas.

### Tipos de memoria implementados

**Memoria de corto plazo**
- Contexto de consulta actual
- Recuperación dinámica de información relevante

**Memoria de largo plazo**
- Persistencia del conocimiento empresarial cargado en la base vectorial FAISS
- Reutilización del conocimiento durante múltiples consultas

## 📋 Planificación utilizada
ORION implementa un flujo secuencial planificado para resolver cada consulta.

### Secuencia de ejecución
1. Recepción de consulta del usuario
2. Recuperación del contexto relevante desde la memoria vectorial
3. Organización del contenido recuperado
4. Envío del contexto al modelo LLM
5. Generación de respuesta estratégica

Este enfoque permite secuenciar tareas de forma ordenada y reproducible.

## 🔄 Orquestación utilizada
La coordinación de los distintos componentes del sistema se realiza mediante **LangChain**, actuando como framework de orquestación.

LangChain permite integrar:

- Recuperación documental
- Base vectorial FAISS
- Modelos de embeddings
- Modelo LLM local
- Flujo completo de consulta y respuesta

Esto asegura una arquitectura modular y mantenible.

## 🏗️ Arquitectura del sistema

```text
Usuario
   ↓
main.py
   ↓
Carga archivo competidores.txt
   ↓
Fragmentación del contenido
   ↓
Generación de embeddings
   ↓
Almacenamiento en FAISS
   ↓
Recuperación de contexto relevante
   ↓
Modelo LLM (Ollama)
   ↓
Respuesta estratégica
```

## 🛠️ Tecnologías utilizadas
- Python
- LangChain
- Ollama
- FAISS
- Sentence Transformers
- Hugging Face Transformers

## 📂 Estructura del proyecto

```text
ORION/
│── main.py
│── competidores.txt
│── requirements.txt
│── README.md
```

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

### 5. Instalar Ollama
Descargar e instalar desde:

https://ollama.com

### 6. Descargar modelo utilizado
```bash
ollama pull llama3
```

### 7. Ejecutar el sistema
```bash
python main.py
```

## 💬 Ejemplos de consultas
El sistema permite consultas estratégicas como:

- ¿Qué debilidades presenta Empresa B?
- ¿Qué estrategia recomendarías para Empresa A?
- ¿Qué empresa presenta mayor riesgo competitivo?
- ¿Qué empresa compite principalmente por precio?
- ¿Qué oportunidades estratégicas observas en este mercado?

## 📊 Ejemplo de uso

### Consulta
```text
¿Qué empresa tiene mayor riesgo de perder mercado?
```

### Respuesta esperada
```text
Econotech presenta mayor riesgo debido a su fuerte dependencia del precio y baja diferenciación competitiva, lo que reduce su capacidad de sostener ventajas frente a competidores con mayor valor agregado.
```

## 📈 Posibles mejoras futuras
- Interfaz gráfica web
- Integración con fuentes de datos externas
- Soporte para múltiples documentos
- Incorporación de memoria persistente ampliada
- Mejoras en planificación autónoma del agente
- Integración con modelos LLM más avanzados

## 👤 Autor
**Abraham Becerra**


## 📌 Reproducibilidad
El proyecto incluye:

✅ Código fuente completo  
✅ Archivo `requirements.txt`  
✅ README con instrucciones de instalación  
✅ Dependencias documentadas  
✅ Uso de modelo local reproducible  

Esto permite que terceros puedan ejecutar el sistema fuera del entorno original.