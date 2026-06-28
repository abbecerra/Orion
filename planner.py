def planificar(
    consulta
):

    consulta = (
        consulta
        .lower()
    )

    # =====================
    # BUSCAR PRECIOS
    # =====================

    if any(

        palabra in consulta

        for palabra in [

            "precio",
            "buscar",
            "producto",
            "mercado",
            "valor"
        ]
    ):

        return (
            "buscar_precio"
        )

    # =====================
    # ENVÍOS
    # =====================

    if any(

        palabra in consulta

        for palabra in [

            "envio",
            "envíos",
            "transporte",
            "logistica"
        ]
    ):

        return (
            "buscar_envios"
        )

    # =====================
    # CÁLCULO
    # =====================

    if any(

        palabra in consulta

        for palabra in [

            "calcular",
            "precio_final",
            "rentabilidad",
            "margen"
        ]
    ):

        return (
            "calcular_precio"
        )

    # =====================
    # RIESGO
    # =====================

    if any(

        palabra in consulta

        for palabra in [

            "riesgo",
            "competencia",
            "score"
        ]
    ):

        return (
            "analizar_riesgo"
        )

    # =====================
    # DEFAULT
    # =====================

    return (
        "buscar_precio"
    )