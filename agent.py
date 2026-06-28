import time

from planner import planificar
from report_generator import generar_reporte
from tools import (
    buscar_precio,
    buscar_envios,
    calcular_precio,
    analizar_riesgo,
    justificar_precio
)

from logger import registrar_evento
from memory import guardar_memoria


def ejecutar_orion(
    
    producto,
    costo_compra,
    margen
):

    inicio_total = time.time()

    try:

        # ==================================
        # VALIDACIONES
        # ==================================
        if costo_compra <= 0:
            return {
                "error":
                "El costo debe ser mayor a cero"
            }

        if margen < 0:
            return {
                "error":
                "El margen no puede ser negativo"
            }

        if margen > 300:
            return {
                "error":
                "El margen excede el límite permitido"
            }
        if not producto or len(producto.strip()) == 0:
            return {
                "error":
                "Debe ingresar un producto."
            }

        if costo_compra <= 0:

            return {
                "error":
                "El costo debe ser mayor a cero"
            }

        if margen < 0:

            return {
                "error":
                "El margen no puede ser negativo"
            }

        if margen > 300:

            return {
                "error":
                "El margen excede el límite permitido"
            }

        producto = producto.strip()

        # ==================================
        # PLANIFICACIÓN
        # ==================================

        decision = planificar(
            f"Busca el precio de {producto}"
        )

        # ==================================
        # BUSCAR PRODUCTO
        # ==================================

        inicio = time.time()

        datos_producto = buscar_precio(
            producto
        )

        registrar_evento(
            producto,
            "buscar_precio",
            time.time() - inicio,
            95,
            False
        )

        if datos_producto is None:

            registrar_evento(
                producto,
                "buscar_precio",
                0,
                0,
                True
            )

            return {
                "error":
                f"El producto '{producto}' no se encuentra en la base de datos."
            }

        # ==================================
        # BUSCAR ENVÍOS
        # ==================================

        inicio = time.time()

        envios = buscar_envios()

        registrar_evento(
            producto,
            "buscar_envios",
            time.time() - inicio,
            100,
            False
        )

        envio_recomendado = min(
            envios,
            key=envios.get
        )

        costo_envio = envios[
            envio_recomendado
        ]

        # ==================================
        # CALCULAR PRECIO
        # ==================================

        inicio = time.time()

        precio = calcular_precio(
            costo_compra,
            costo_envio,
            margen,
            datos_producto[
                "precio_mercado"
            ]
        )
        justificacion = justificar_precio(

            datos_producto[
                "precio_mercado"
            ],

            precio[
                "precio_minimo"
            ],

            precio[
                "precio_recomendado"
            ],

            precio[
                "estrategia"
            ]
        )
        registrar_evento(
            producto,
            "calcular_precio",
            time.time() - inicio,
            100,
            False
        )

        # ==================================
        # ANALIZAR RIESGO
        # ==================================

        inicio = time.time()

        riesgo = analizar_riesgo(
            datos_producto[
                "competencia"
            ],
            margen
        )

        registrar_evento(
            producto,
            "analizar_riesgo",
            time.time() - inicio,
            95,
            False
        )

        # ==================================
        # RESPUESTA FINAL
        # ==================================

        respuesta = {

            "producto":
                producto,

            "precio_mercado":
                datos_producto[
                    "precio_mercado"
                ],

            "precio_minimo":
                precio[
                    "precio_minimo"
                ],

            "precio_recomendado":
                precio[
                    "precio_recomendado"
                ],

            "estrategia":
                precio[
                    "estrategia"
                ],

            "utilidad":
                precio[
                    "utilidad"
                ],

            "tienda":
                datos_producto[
                    "tienda"
                ],
            "mercado":
                datos_producto.get(
                        "mercado",
                        "Chile"
                ),
            "envio":
                envio_recomendado,

            "costo_envio":
                costo_envio,

            "riesgo":
                riesgo[
                    "riesgo"
                ],

            "score":
                riesgo[
                    "score"
                ],
            "justificacion":
               justificacion,
            
            "latencia_total":
                round(
                    time.time()
                    - inicio_total,
                    2
                )
        }
        archivo = generar_reporte(
            respuesta
        )

        respuesta[
            "reporte"
        ] = archivo
        guardar_memoria(
            producto,
            str(respuesta)
        )

        return respuesta

    except Exception as e:

        registrar_evento(
            producto,
            "generar_reporte",
            0,
            0,
            True
        )

        return {
            "error":
            f"Error interno ORION: {str(e)}"
        }