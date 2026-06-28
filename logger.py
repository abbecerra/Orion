import csv
import os
from datetime import datetime
import psutil


LOG_FILE = "logs/orion_logs.csv"


def iniciar_logs():

    os.makedirs("logs", exist_ok=True)

    with open(
        LOG_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow([
            "timestamp",
            "consulta",
            "herramienta",
            "latencia",
            "cpu",
            "ram",
            "precision",
            "error"
        ])


def registrar_evento(
    consulta,
    herramienta,
    latencia,
    precision=100,
    error=False
):

    herramientas_validas = [
        "buscar_precio",
        "buscar_envios",
        "calcular_precio",
        "analizar_riesgo",
        "generar_reporte"
    ]

    if herramienta not in herramientas_validas:
        herramienta = "desconocida"

    cpu = psutil.cpu_percent()

    ram = round(
        psutil.virtual_memory().percent,
        2
    )

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow([
            datetime.now(),
            consulta,
            herramienta,
            max(
                round(latencia,3),
                0.001
            ),
            cpu,
            ram,
            precision,
            error
        ])


def obtener_metricas():

    datos = []

    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as archivo:

        reader = csv.DictReader(archivo)

        for fila in reader:
            datos.append(fila)

    return datos