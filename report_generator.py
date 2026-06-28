from datetime import datetime
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generar_reporte(resultado):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    fecha = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    archivo = (
        f"reports/reporte_{fecha}.pdf"
    )

    doc = SimpleDocTemplate(
        archivo
    )

    estilos = getSampleStyleSheet()

    contenido = []

    contenido.append(
        Paragraph(
            "<font size='20'><b>ORION Pricing AI</b></font>",
            estilos["Title"]
        )
    )

    contenido.append(
        Spacer(1,20)
    )

    contenido.append(
        Paragraph(
            f"<b>Fecha:</b> {datetime.now()}",
            estilos["Normal"]
        )
    )

    contenido.append(
        Spacer(1,10)
    )

    datos = [

        ("Producto", resultado["producto"]),
        ("Precio mercado", f"${resultado['precio_mercado']:,}"),
        ("Precio mínimo", f"${resultado['precio_minimo']:,}"),
        ("Precio recomendado", f"${resultado['precio_recomendado']:,}"),
        ("Estrategia", resultado["estrategia"]),
        ("Utilidad", f"${resultado['utilidad']:,}"),
        ("Tienda", resultado["tienda"]),
        ("Empresa envío", resultado["envio"]),
        ("Costo envío", f"${resultado['costo_envio']:,}"),
        ("Riesgo", resultado["riesgo"]),
        ("Score", resultado["score"]),
        ("Latencia", f"{resultado['latencia_total']} s")
    ]

    for nombre, valor in datos:

        contenido.append(
            Paragraph(
                f"<b>{nombre}:</b> {valor}",
                estilos["Normal"]
            )
        )

        contenido.append(
            Spacer(1,8)
        )

    contenido.append(
        Spacer(1,20)
    )

    contenido.append(
        Paragraph(
            "Reporte generado automáticamente por ORION Pricing AI.",
            estilos["Italic"]
        )
    )

    doc.build(
        contenido
    )

    return archivo