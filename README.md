# 🧠💼 ORION — Sistema de Inteligencia Competitiva IA

## 📌 Descripción
ORION es un sistema basado en inteligencia artificial que analiza información de empresas y genera respuestas estratégicas a partir de un contexto definido. Su objetivo es simular el trabajo de una consultora, permitiendo evaluar fortalezas, debilidades, riesgos y estrategias recomendadas.

## ⚙️ Funcionamiento del sistema
El sistema trabaja de la siguiente manera:
1. Carga información desde un archivo (`competidores.txt`)
2. Divide el texto en fragmentos
3. Genera embeddings (representaciones vectoriales)
4. Almacena la información en FAISS
5. Permite realizar consultas
6. Responde usando IA en base al contexto

## 🛠️ Tecnologías utilizadas
- Python
- LangChain
- Transformers (Hugging Face)
- FAISS
- Sentence-Transformers

## 📂 Estructura del proyecto
ORION/
│── main.py
│── competidores.txt
│── requirements.txt
│── README.md

## 🚀 Instalación y ejecución
1. Clonar repositorio
   git clone https://github.com/abbecerra/Orion.git
   cd Orion

2. Crear entorno virtual
   python -m venv venv

3. Activar entorno (Windows)
   venv\Scripts\activate

4. Instalar dependencias
   pip install -r requirements.txt

5. Ejecutar programa
   python main.py

## 💬 Ejemplos de consultas
- ¿Debilidades de Empresa B?
- ¿Qué estrategia recomendarías a Empresa A?
- ¿Qué empresa tiene mayor riesgo de perder mercado?
- ¿Qué empresa compite solo por precio?

## 📊 Ejemplo de uso
Consulta:
¿Qué empresa tiene mayor riesgo de perder mercado?

Respuesta esperada:
Econotech presenta el mayor riesgo debido a su dependencia del precio y baja diferenciación en calidad.

## 🎯 Objetivo del proyecto
Desarrollar una herramienta que automatice el análisis competitivo de empresas utilizando inteligencia artificial.

## 📈 Posibles mejoras
- Integración con modelos más avanzados
- Uso de APIs externas
- Interfaz gráfica
- Incorporación de más datos empresariales

## 👤 Autor
Abraham Becerra

## 📌 Nota
Para ejecutar correctamente el proyecto, es necesario instalar las dependencias indicadas en requirements.txt.