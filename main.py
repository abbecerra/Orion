from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = TextLoader("competidores.txt", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_documents(docs)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(docs, embeddings)


llm = Ollama(model="llama3")

print("\n🧠💼 ORION — CONSULTORÍA ESTRATÉGICA DE MERCADO\n")


def build_prompt(query, context):
    return f"""
Eres ORION, una consultora estratégica senior.

Debes evaluar empresas con lógica consistente y cuantificable.

CONTEXTO:
{context}

CONSULTA:
{query}

REGLAS OBLIGATORIAS:
- Evalúa cada empresa con puntaje de riesgo de 0 a 100
- 0 = sin riesgo / 100 = riesgo extremo
- Usa estos factores:
  • dependencia de precio
  • diferenciación
  • accesibilidad de mercado

RESPONDE EN FORMATO:

1. 📊 Diagnóstico del mercado

2. 🏢 Evaluación por empresa:
   - A: score de riesgo + explicación breve
   - B: score de riesgo + explicación breve
   - C: score de riesgo + explicación breve

3. ⚖️ Ranking de riesgo (ordenado por score)

4. ⚠️ Justificación basada en scores

5. 🚀 Conclusión final (1 sola empresa)
"""


while True:
    query = input("\nConsulta (o 'salir'): ")

    if query.lower() == "salir":
        break

    
    docs_found = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs_found])

    
    prompt = build_prompt(query, context)

  
    response = llm.invoke(prompt)

    print("\n📊 INFORME CONSULTORA ORION:\n")
    print(response)
    print("\n" + "-" * 60)