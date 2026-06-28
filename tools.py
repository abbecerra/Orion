from market_search import buscar_producto_real
PRODUCTOS = {

    "RTX 4060": {
        "precio_mercado": 349990,
        "tienda": "PC Factory",
        "competencia": "alta"
    },

    "RTX 4070": {
        "precio_mercado": 599990,
        "tienda": "SP Digital",
        "competencia": "media"
    },

    "Ryzen 7 7800X3D": {
        "precio_mercado": 429990,
        "tienda": "PC Factory",
        "competencia": "alta"
    },

    "iPhone 16": {
        "precio_mercado": 999990,
        "tienda": "MercadoLibre Chile",
        "competencia": "media"
    }
}


ENVIOS = {

    "Chilexpress": 6900,
    "Starken": 5200,
    "Blue Express": 4500
}

def buscar_precio(producto):

    producto = producto.strip()

    # =====================
    # MERCADO CHILENO
    # =====================

    if producto in PRODUCTOS:

        datos = PRODUCTOS[
            producto
        ]

        datos["mercado"] = (
            "Chile"
        )

        return datos

    # =====================
    # MERCADO GLOBAL
    # =====================

    datos = buscar_producto_real(
        producto
    )

    if datos:

        datos["mercado"] = (
            "Global"
        )

        return datos

    return None


def buscar_envios():

    return ENVIOS


def calcular_precio(
    costo_compra,
    costo_envio,
    margen,
    precio_mercado
):
    # ==================================
    # VALIDAR COSTO REALISTA
    # ==================================

    ratio = (
        costo_compra /
        precio_mercado
    )

    # si el costo es absurdamente bajo
    if ratio < 0.25:

        costo_compra = int(
            precio_mercado * 0.60
        )

    # si el costo supera el mercado
    elif ratio > 1:

        costo_compra = int(
            precio_mercado * 0.90
        )
    costo_total = (
        costo_compra +
        costo_envio
    )

    precio_minimo = int(
        costo_total *
        (1 + margen/100)
    )

    porcentaje = (
        precio_minimo /
        precio_mercado
    )

    # podemos competir cómodamente
    if porcentaje <= 0.85:

        estrategia = "Competitivo"

        precio_recomendado = int(
            precio_mercado * 0.95
        )

    # estamos cerca del mercado
    elif porcentaje <= 1:

        estrategia = "Mercado"

        precio_recomendado = int(
            precio_mercado * 0.98
        )

    # nuestro costo ya supera el mercado
    else:

        estrategia = "Supervivencia"

        precio_recomendado = precio_minimo

    utilidad = (
        precio_recomendado -
        costo_total
    )

    return {

        "precio_minimo":
            precio_minimo,

        "precio_recomendado":
            precio_recomendado,

        "utilidad":
            utilidad,

        "estrategia":
            estrategia
    }


def analizar_riesgo(
    competencia,
    margen
):

    score = 0

    if competencia == "alta":
        score += 60

    elif competencia == "media":
        score += 40

    else:
        score += 20

    if margen < 20:
        score += 30

    elif margen < 30:
        score += 15

    if score >= 80:
        nivel = "ALTO"

    elif score >= 50:
        nivel = "MEDIO"

    else:
        nivel = "BAJO"

    return {

        "score":
            score,

        "riesgo":
            nivel
    }
def justificar_precio(

    precio_mercado,
    precio_minimo,
    precio_recomendado,
    estrategia

):

    if estrategia == "Competitivo":

        return (
            "Se utilizó una estrategia "
            "competitiva debido a que "
            "el mercado presenta "
            "un amplio margen "
            "respecto al costo."
        )

    if estrategia == "Mercado":

        return (
            "Se utilizó una estrategia "
            "de mercado para mantener "
            "competitividad y "
            "rentabilidad."
        )

    return (
        "Se utilizó una estrategia "
        "de supervivencia para "
        "asegurar la rentabilidad "
        "mínima."
    )    