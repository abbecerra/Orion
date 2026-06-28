def generar_recomendaciones(datos):

    recomendaciones = []

    # LATENCIA
    if datos["latencia"] > 1:

        recomendaciones.append(
            "Optimizar la latencia mediante cache y reducción de consultas."
        )

    else:

        recomendaciones.append(
            "La latencia del sistema es adecuada."
        )

    # CPU
    if datos["cpu"] > 70:

        recomendaciones.append(
            "Se recomienda optimizar el consumo de CPU."
        )

    else:

        recomendaciones.append(
            "El uso de CPU es eficiente."
        )

    # RAM
    if datos["ram"] > 80:

        recomendaciones.append(
            "Se recomienda optimizar el uso de memoria."
        )

    else:

        recomendaciones.append(
            "El uso de memoria es estable."
        )

    # CUELLO DE BOTELLA
    recomendaciones.append(
        f"El principal cuello de botella corresponde a: "
        f"{datos['cuello_botella']}."
    )

    return recomendaciones