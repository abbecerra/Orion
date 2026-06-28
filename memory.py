import json
import os


MEMORY_FILE = "data/memory.json"


def iniciar_memoria():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                [],
                archivo,
                ensure_ascii=False,
                indent=4
            )


def guardar_memoria(
    consulta,
    respuesta
):

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as archivo:

        memoria = json.load(archivo)

    memoria.append({
        "consulta": consulta,
        "respuesta": respuesta
    })

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            memoria,
            archivo,
            ensure_ascii=False,
            indent=4
        )


def obtener_memoria():

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as archivo:

        return json.load(archivo)