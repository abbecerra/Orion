from serpapi import GoogleSearch

SERP_API_KEY = "ee3a20ee04fdf040e05e1fb2d7bd0a0d1b374d027a1f407491e6ab598afb2f9d"

TIENDAS_CHILENAS = [

    "PC Factory",
    "Pcfactory",
    "SP Digital",
    "Winpy",
    "Mercado Libre",
    "MercadoLibre",
    "Paris",
    "Paris.cl",
    "Falabella",
    "Ripley",
    "Ripley.com",
    "Lancenter",
    "Abcdin",
    "Hites",
    "Entel",
    "Claro",
    "Samsung",
    "Lider",
    "lider.cl",
    "mybox",
    "MyShop",
    "Pc Express",
    "NotebooksYa",
    "MegaBytes",
    "CompuElite",
    "Xtreme",
    "Centrale",
    "Tienda MegaBytes"
]

PRODUCTOS_IMPOSIBLES = [

    "rtx 9999",
    "rtx 8888",
    "iphone 20",
    "iphone 30",
    "playstation 12",
    "ryzen 15000x3d"
]
CORRECCIONES = {

    # GTX confundidas con RTX
    "rtx 1650": "gtx 1650",
    "rtx 1660": "gtx 1660",
    "rtx 1660 ti": "gtx 1660 ti",
    "rtx 1660 super": "gtx 1660 super",

    # errores comunes
    "rtx1650": "gtx 1650",
    "rtx1660": "gtx 1660",
    "rtx1660ti": "gtx 1660 ti",
    "rtx1660super": "gtx 1660 super",
}

BASE_REFERENCIAL = {
    
    # =====================================
    # NVIDIA RTX 30
    # =====================================

    "rtx 3050": 249990,
    "rtx 3060": 329990,
    "rtx 3060 ti": 399990,
    "rtx 3070": 549990,
    "rtx 3070 ti": 649990,
    "rtx 3080": 799990,
    "rtx 3080 ti": 999990,
    "rtx 3090": 1699990,
    "rtx 3090 ti": 1999990,

    # =====================================
    # NVIDIA RTX 40
    # =====================================

    "rtx 4060": 479990,
    "rtx 4060 ti": 649990,
    "rtx 4070": 799990,
    "rtx 4070 super": 949990,
    "rtx 4070 ti": 1099990,
    "rtx 4070 ti super": 1249990,
    "rtx 4080": 1699990,
    "rtx 4080 super": 1899990,
    "rtx 4090": 2499990,

    # =====================================
    # NVIDIA RTX 50
    # =====================================

    "rtx 5060": 449990,
    "rtx 5060 ti": 599990,
    "rtx 5070": 879995,
    "rtx 5070 ti": 1099990,
    "rtx 5080": 1699990,
    "rtx 5090": 2999990,

    # =====================================
    # AMD RX 6000
    # =====================================

    "rx 6600": 249990,
    "rx 6650 xt": 329990,
    "rx 6700 xt": 449990,
    "rx 6750 xt": 499990,
    "rx 6800 xt": 699990,
    "rx 6900 xt": 899990,
    "rx 6950 xt": 999990,

    # =====================================
    # AMD RX 7000
    # =====================================

    "rx 7600": 329990,
    "rx 7700 xt": 549990,
    "rx 7800 xt": 699990,
    "rx 7900 gre": 849990,
    "rx 7900 xt": 1099990,
    "rx 7900 xtx": 1499990,

    # =====================================
    # AMD RX 9000
    # =====================================

    "rx 9060": 499990,
    "rx 9070": 799990,
    "rx 9070 xt": 999990,

    # =====================================
    # AMD RYZEN
    # =====================================

    "ryzen 5600": 119990,
    "ryzen 5700x": 189990,
    "ryzen 5800x3d": 329990,

    "ryzen 7600": 229990,
    "ryzen 7700x": 349990,
    "ryzen 7800x3d": 499990,
    "ryzen 7900x": 549990,
    "ryzen 7950x": 749990,

    "ryzen 9600x": 329990,
    "ryzen 9700x": 449990,
    "ryzen 9800x3d": 590990,
    "ryzen 9900x": 699990,
    "ryzen 9950x": 899990,

    # =====================================
    # INTEL
    # =====================================

    "i5 12400f": 149990,
    "i5 13400f": 189990,
    "i5 14600k": 329990,

    "i7 13700k": 449990,
    "i7 14700k": 499990,

    "i9 13900k": 699990,
    "i9 14900k": 799990,

    "ultra 7 265k": 549990,
    "ultra 9 285k": 899990,

    # =====================================
    # APPLE
    # =====================================

    "iphone 15": 899990,
    "iphone 15 plus": 1099990,
    "iphone 15 pro": 1299990,
    "iphone 15 pro max": 1499990,

    "iphone 16": 999990,
    "iphone 16 plus": 1199990,
    "iphone 16 pro": 1399990,
    "iphone 16 pro max": 1699990,

    "iphone 17": 1299990,
    "iphone 17 pro": 1599990,
    "iphone 17 pro max": 1899990,

    # =====================================
    # SAMSUNG
    # =====================================

    "samsung galaxy s24": 799990,
    "samsung galaxy s24 plus": 1099990,
    "samsung galaxy s24 ultra": 1399990,

    "samsung galaxy s25": 999990,
    "samsung galaxy s25 plus": 1199990,
    "samsung galaxy s25 ultra": 1499990,

    "samsung galaxy s26": 1099990,
    "samsung galaxy s26 plus": 1299990,
    "samsung galaxy s26 ultra": 1599990,

    # =====================================
    # XIAOMI
    # =====================================

    "xiaomi 14": 799990,
    "xiaomi 14 ultra": 1199990,
    "xiaomi 15": 899990,
    "xiaomi 15 ultra": 1399990,

    "redmi note 14": 249990,
    "redmi note 14 pro": 399990,
    "redmi note 14 pro plus": 499990,

    # =====================================
    # MOTOROLA
    # =====================================

    "motorola edge 50": 499990,
    "motorola edge 50 pro": 699990,
    "motorola razr 50": 899990,
    "moto g85": 299990,
    "moto g75": 249990,

    # =====================================
    # HONOR
    # =====================================

    "honor magic 6 pro": 999990,
    "honor magic 7 pro": 1199990,
    "honor 200 pro": 699990,

    # =====================================
    # HUAWEI
    # =====================================

    "huawei pura 70": 899990,
    "huawei pura 70 pro": 1199990,
    "huawei mate 70": 1099990,

    # =====================================
    # OPPO
    # =====================================

    "oppo find x8": 999990,
    "oppo reno 13": 499990,

    # =====================================
    # VIVO
    # =====================================

    "vivo x200": 1099990,
    "vivo v50": 599990,

    # =====================================
    # CONSOLAS
    # =====================================

    "playstation 5": 599990,
    "playstation 5 pro": 999990,
    "xbox series x": 649990,
    "nintendo switch 2": 599990,
}

BASURA = [

    "pc gamer",
    "gaming pc",
    "desktop",
    "workstation",
    "notebook",
    "laptop",
    "ultrabook",
    "bundle",
    "kit",
    "combo",
    "pack",
    "set",
    "armado",
    "computador",
    "torre",
    "incluye",

    # nuevos
    "setup",
    "cpu",
    "gabinete",
    "pc completa",
    "monitor",
    "mouse",
    "teclado",
    "accesorio",
    "repuesto"
]



def normalizar(texto):

    texto = texto.lower()

    for x in [
        " ",
        "-",
        "_",
        ".",
        ",",
        "/",
        "(",
        ")"
    ]:

        texto = texto.replace(
            x,
            ""
        )

    return texto


def limpiar_outliers(lista):

    if len(lista) < 4:
        return lista

    lista = sorted(lista)

    q1 = lista[len(lista)//4]
    q3 = lista[(len(lista)*3)//4]

    iqr = q3 - q1

    minimo = q1 - (1.5 * iqr)
    maximo = q3 + (1.5 * iqr)

    return [

        x

        for x in lista

        if minimo <= x <= maximo
    ]


def calcular_mediana(lista):

    lista = limpiar_outliers(
        lista
    )

    if not lista:
        return None

    lista.sort()

    n = len(lista)

    if n % 2 == 0:

        return int(

            (
                lista[n//2-1]
                +
                lista[n//2]
            ) / 2
        )

    return lista[n//2]


def coincide_producto(
    producto,
    titulo
):

    producto = producto.lower()
    titulo = titulo.lower()

    # =====================
    # GPUs NVIDIA
    # =====================

    # =====================
# GPUs NVIDIA
# =====================

    if (
        "rtx" in producto
        or
        "gtx" in producto
    ):

        import re

        numero = re.findall(
            r"\d+",
            producto
        )

        if not numero:
            return False

        numero = numero[0]

        # debe existir GTX o RTX
        if (
            "rtx" not in titulo
            and
            "gtx" not in titulo
        ):
            return False

        # debe existir el modelo
        if numero not in titulo:
            return False

        basura = [

            "pc gamer",
            "gaming pc",
            "desktop",
            "workstation",
            "notebook",
            "laptop",
            "bundle",
            "kit",
            "combo",
            "setup",
            "gabinete",
            "cpu"
        ]

        if any(
            x in titulo
            for x in basura
        ):
            return False

        return True

    # =====================
    # RYZEN
    # =====================

    if "ryzen" in producto:

        numeros = []

        for p in producto.split():

            if any(c.isdigit() for c in p):
                numeros.append(
                    p.lower()
                )

        if "ryzen" not in titulo:
            return False

        for n in numeros:

            if n not in titulo:
                return False

        return True

    # =====================
    # IPHONE
    # =====================

    if "iphone" in producto:

        numero = None

        for p in producto.split():

            if p.isdigit():
                numero = p

        if numero is None:
            return False

        return (
            "iphone" in titulo
            and
            numero in titulo
        )

    # =====================
    # SAMSUNG
    # =====================

    if (
        "galaxy" in producto
        or
        "samsung" in producto
    ):

        palabras = producto.split()

        encontrados = 0

        for p in palabras:

            if p in titulo:
                encontrados += 1

        return (
            encontrados >=
            len(palabras)-1
        )

    # =====================
    # GENERICO
    # =====================

    producto_n = normalizar(
        producto
    )

    titulo_n = normalizar(
        titulo
    )

    if producto_n in titulo_n:
        return True

    palabras = producto.split()

    encontrados = 0

    for p in palabras:

        if p in titulo:
            encontrados += 1

    return (
        encontrados >=
        max(
            1,
            len(palabras)-1
        )
    )

def fallback_orion(producto):

    producto_n = (
        producto
        .lower()
        .strip()
    )

    if producto_n in BASE_REFERENCIAL:

        return {
            "precio_mercado":
                BASE_REFERENCIAL[
                    producto_n
                ],
            "tienda":
                "Base Referencial ORION",
            "competencia":
                "alta"
        }

    return None

def buscar_producto_real(
    producto
):
    producto = CORRECCIONES.get(
        producto.lower(),
        producto
    )
    print(
    "CORREGIDO:",
    producto
)

    try:

        if (
            producto
            .lower()
            in
            PRODUCTOS_IMPOSIBLES
        ):
            return None

                # =====================
        # BUSQUEDA MULTIPLE
        # =====================

        consultas = [

            f"{producto} Chile",
            producto,
            f"{producto} precio",
            f"{producto} graphics card",
            f"{producto} gpu"
        ]

        shopping = []

        for consulta in consultas:

            print(
                "BUSCANDO:",
                consulta
            )

            search = GoogleSearch({

                "engine":
                    "google_shopping",

                "q":
                    consulta,

                "hl":
                    "es",

                "gl":
                    "cl",

                "api_key":
                    SERP_API_KEY
            })

            resultados = (
                search.get_dict()
            )

            shopping = (
                resultados.get(
                    "shopping_results",
                    []
                )
            )

            if shopping:

                print(
                    "ENCONTRADO:",
                    consulta
                )

                break
    
        shopping = (
            resultados.get(
                "shopping_results",
                []
            )
        )
        print(resultados.keys())
        print(resultados)
        print("\n====================")
        print("PRODUCTO:", producto)
        print("====================")

        for item in shopping:

            print(
                item.get("source",""),
                "|",
                item.get("title",""),
                "|",
                item.get("extracted_price")
            )
        if not shopping:

            producto_n = (
                producto
                .lower()
                .strip()
            )

            if producto_n in BASE_REFERENCIAL:

                return {

                    "precio_mercado":
                        BASE_REFERENCIAL[
                            producto_n
                        ],

                    "tienda":
                        "Base Referencial ORION",

                    "competencia":
                        "alta"
                }

            return None

        precios_chile = []
        tienda_chile = None

        precios_global = []

        for item in shopping:

            titulo = item.get(
                "title",
                ""
            )

            tienda = item.get(
                "source",
                ""
            )

            precio = item.get(
                "extracted_price"
            )

            # validar producto
            if not coincide_producto(
                producto,
                titulo
            ):
                continue

            # eliminar basura
            if any(
                x in titulo.lower()
                for x in BASURA
            ):
                continue

            if precio is None:
                continue

            try:

                precio = int(
                    float(precio)
                )

            except:

                continue

            # filtros generales
            if precio < 50000:
                continue

            if precio > 10000000:
                continue

            # filtros CPU
            if (
                "ryzen"
                in
                producto.lower()
            ):

                if precio > 1500000:
                    continue

            # filtros GPU
            if (
                "rtx"
                in
                producto.lower()
            ):

                if precio > 2500000:
                    continue

            # filtros smartphones
            if any(
                x in producto.lower()
                for x in [
                    "iphone",
                    "galaxy",
                    "samsung"
                ]
            ):

                if precio > 3000000:
                    continue

            precios_global.append(
                precio
            )

            es_chile = any(

                x.lower()
                in
                tienda.lower()

                for x in
                TIENDAS_CHILENAS
            )

            if es_chile:

                precios_chile.append(
                    precio
                )

                if tienda_chile is None:

                    tienda_chile = (
                        tienda
                    )

        # sin resultados
        # =====================
# SIN RESULTADOS VALIDOS
# =====================

        if (
            not precios_chile
            and
            not precios_global
        ):

            producto_n = (
                producto
                .lower()
                .strip()
            )

            # FALLBACK ORION
            if producto_n in BASE_REFERENCIAL:

                precio = BASE_REFERENCIAL[
                    producto_n
                ]

                # limitar GPUs absurdamente caras
                if "rtx" in producto_n:

                    precio = min(
                        precio,
                        1999990
                    )

                return {

                    "precio_mercado":
                        precio,

                    "tienda":
                        "Base Referencial ORION",

                    "competencia":
                        "alta"
                }

            return None

        # prioridad chile
        if precios_chile:

            return {

                "precio_mercado":
                    calcular_mediana(
                        precios_chile
                    ),

                "tienda":
                    tienda_chile,

                "competencia":
                    "alta"
            }

        # fallback global
        return {

            "precio_mercado":
                calcular_mediana(
                    precios_global
                ),

            "tienda":
                "Referencia Global",

            "competencia":
                "alta"
        }

    except Exception as e:

        print(
            "SERPAPI ERROR:",
            e
        )

        return None