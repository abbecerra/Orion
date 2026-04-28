# 🧠💼 ORION — Inteligencia Estratégica de Mercado

ORION es un sistema de inteligencia competitiva basado en **RAG (Retrieval-Augmented Generation)** que analiza empresas y genera informes estratégicos tipo consultoría.

---

## 🚀 ¿Qué hace?

- Analiza empresas desde documentos locales
- Usa embeddings para recuperar información relevante
- Genera análisis estratégico con LLM local (Ollama)
- Entrega ranking de riesgo y recomendaciones

---

## 🏗️ Arquitectura

1. TextLoader → carga datos
2. RecursiveCharacterTextSplitter → divide texto
3. HuggingFaceEmbeddings → crea vectores
4. FAISS → base de datos vectorial
5. Ollama (Llama 3) → modelo de lenguaje
6. Prompt → genera informe estratégico

---

## 📂 Estructura

ORION/
│
├── main.py
├── competidores.txt
├── requirements.txt
└── README.md

---

## ⚙️ Instalación

pip install -r requirements.txt

ollama run llama3

---

## ▶️ Ejecución

python main.py

---

## 💬 Ejemplo

¿Qué empresa tiene mayor riesgo de perder mercado?

ORION responde con:
- Diagnóstico
- Análisis por empresa
- Ranking
- Conclusión

---

## 🧠 Objetivo

Demostrar uso de:
- IA generativa
- RAG
- LLM local
- Análisis estratégico

---

## 👨‍💻 Autor
Proyecto académico ORION — Inteligencia Artificial