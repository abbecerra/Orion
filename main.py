from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.memory import ConversationBufferMemory
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ddgs import DDGS
import warnings

warnings.filterwarnings("ignore")

print("\n🧠 ORION v2 🧠 \n")

try:
    loader = TextLoader("competidores.txt", encoding="utf-8")
    docs = loader.load()
except Exception as e:
    raise Exception(f"Error cargando competidores.txt: {e}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_documents(docs)

try:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)

except Exception as e:
    raise Exception(f"Error creando FAISS: {e}")

try:
    llm = Ollama(model="llama3")
except Exception as e:
    raise Exception(f"Error iniciando Llama3: {e}")

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=False
)


def buscar_web(query):
    try:
        with DDGS() as ddgs:
            resultados = ddgs.text(query, max_results=3)

            textos = []

            for r in resultados:
                titulo = r.get("title", "")
                body = r.get("body", "")

                if titulo or body:
                    textos.append(f"{titulo}: {body}")

            return "\n".join(textos)

    except:
        return ""


def requiere_web(query):
    keywords = [
        "samsung",
        "apple",
        "tesla",
        "amazon",
        "google",
        "microsoft",
        "meta",
        "netflix",
        "mercado",
        "industria",
        "competencia",
        "empresa real"
    ]

    q = query.lower()

    return any(word in q for word in keywords)


def obtener_contexto(query):
    if requiere_web(query):
        contexto_web = buscar_web(query)

        return f"""
CONTEXTO WEB:
{contexto_web}
"""

    docs_found = db.similarity_search(query, k=3)

    contexto_local = "\n".join(
        [doc.page_content for doc in docs_found]
    )

    return contexto_local


def build_prompt(query, context, history, web_mode=False):
    if web_mode:
        return f"""
Eres ORION v2, consultora estratégica empresarial senior.

REGLAS:
- Usa SOLO contexto web.
- No inventes.
- Si falta evidencia responde:
"No tengo suficiente información para responder con precisión."

CONTEXTO:
{context}

CONSULTA:
{query}

RESPONDE:
1. Diagnóstico
2. Fortalezas
3. Debilidades
4. Riesgos
5. Recomendación
"""

    return f"""
Eres ORION v2, consultora estratégica empresarial senior.

REGLAS:
- Usa SOLO el contexto.
- No inventes información.

HISTORIAL:
{history}

CONTEXTO:
{context}

CONSULTA:
{query}

RESPONDE:
1. Diagnóstico
2. Evaluación
3. Ranking
4. Recomendación
"""


def analizar_consulta(query):
    query = query.strip()

    if not query:
        return "Consulta vacía."

    web_mode = requiere_web(query)

    if web_mode:
        history = ""
    else:
        history = memory.load_memory_variables({}).get(
            "chat_history",
            ""
        )

    context = obtener_contexto(query)

    if not context.strip():
        return "No se encontró contexto suficiente."

    prompt = build_prompt(
        query,
        context,
        history,
        web_mode
    )

    response = llm.invoke(prompt)

    if not web_mode:
        memory.save_context(
            {"input": query},
            {"output": response}
        )

    return response