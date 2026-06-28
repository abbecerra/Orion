import customtkinter as ctk
from tkinter import messagebox
import threading
from agent import ejecutar_orion

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("ORION Pricing AI")
app.geometry("950x850")
app.resizable(False, False)

# =====================
# HEADER
# =====================


titulo = ctk.CTkLabel(
    app,
    text="🧠 ORION PRICING AI",
    font=("Segoe UI", 32, "bold")
)

titulo.pack(pady=(20,5))

subtitulo = ctk.CTkLabel(
    app,
    text="Strategic Market Intelligence Platform",
    font=("Segoe UI", 14)
)

subtitulo.pack(pady=(0,20))

# =====================
# PANEL ENTRADA
# =====================

frame_inputs = ctk.CTkFrame(
    app,
    width=850,
    height=170
)

frame_inputs.pack(
    padx=20,
    pady=10
)

label_producto = ctk.CTkLabel(
    frame_inputs,
    text="📦 Producto",
    font=("Segoe UI",16,"bold")
)

label_producto.pack(pady=(20,5))

entry_producto = ctk.CTkEntry(
    frame_inputs,
    width=400
)

entry_producto.pack()

entry_producto.insert(
    0,
    "RTX 4060"
)

label_costo = ctk.CTkLabel(
    frame_inputs,
    text="💰 Costo adquisición",
    font=("Segoe UI",16,"bold")
)

label_costo.pack(pady=(15,5))

entry_costo = ctk.CTkEntry(
    frame_inputs,
    width=400
)

entry_costo.pack()

entry_costo.insert(
    0,
    "250000"
)

label_margen = ctk.CTkLabel(
    frame_inputs,
    text="📈 Margen objetivo (%)",
    font=("Segoe UI",16,"bold")
)

label_margen.pack(pady=(15,5))

entry_margen = ctk.CTkEntry(
    frame_inputs,
    width=400
)

entry_margen.pack()

entry_margen.insert(
    0,
    "25")

# =====================
# RESULTADOS
# =====================

frame_resultados = ctk.CTkFrame(
    app,
    width=900,
    height=350
)

frame_resultados.pack(
    pady=10,
    padx=20
)

resultado = ctk.CTkTextbox(
    frame_resultados,
    width=850,
    height=220,
    font=("Consolas",13)
)

resultado.pack(
    pady=15,
    padx=15
)

# =====================
# BOTON
# =====================

def analizar():

    boton.configure(
        state="disabled"
    )

    app.update()

    try:

        producto = entry_producto.get()

        costo = int(
            entry_costo.get()
        )

        margen = int(
            entry_margen.get()
        )

        # ==================================
        # PANTALLA DE CARGA
        # ==================================

        resultado.delete(
            "1.0",
            "end"
        )

        resultado.insert(
            "end",
            f"""

═══════════════════════════════════════════
            ORION AI
═══════════════════════════════════════════

📦 PRODUCTO

   {producto}

═══════════════════════════════════════════

🔍 ETAPA 1
   ✓ Validando producto

🔍 ETAPA 2
   ⏳ Consultando Google Shopping

🔍 ETAPA 3
   ⏳ Verificando mercado chileno

🔍 ETAPA 4
   ⏳ Eliminando outliers

🔍 ETAPA 5
   ⏳ Analizando competencia

🔍 ETAPA 6
   ⏳ Calculando estrategia comercial

🔍 ETAPA 7
   ⏳ Generando reporte

═══════════════════════════════════════════

Por favor espere...

═══════════════════════════════════════════

"""
        )

        # fuerza actualización visual
        app.update()

        # ==================================
        # EJECUTAR ORION
        # ==================================

        r = ejecutar_orion(
            producto,
            costo,
            margen
        )

        resultado.delete(
            "1.0",
            "end"
        )

        app.update()

        # ==================================
        # ERROR
        # ==================================

        if "error" in r:

            resultado.insert(
                "end",
                f"\n❌ {r['error']}"
            )

            boton.configure(
                state="normal"
            )

            return

        # ==================================
        # REPORTE
        # ==================================

        texto = f"""

═══════════════════════════════════════════
            REPORTE ORION
═══════════════════════════════════════════

📦 PRODUCTO
   {r['producto']}

═══════════════════════════════════════════

💰 ANÁLISIS DE MERCADO

   Precio mercado:
      ${r['precio_mercado']:,.0f}

   Precio mínimo rentable:
      ${r['precio_minimo']:,.0f}

   Precio recomendado:
      ${r['precio_recomendado']:,.0f}

═══════════════════════════════════════════

📈 ESTRATEGIA COMERCIAL

   Estrategia:
      {r['estrategia']}

   Utilidad esperada:
      ${r['utilidad']:,.0f}

    🧠 JUSTIFICACIÓN
   {r['justificacion']}

═══════════════════════════════════════════

🚚 LOGÍSTICA

   Tienda:
      {r['tienda']}

   Transporte:
      {r['envio']}

   Costo envío:
      ${r['costo_envio']:,.0f}

    🌎 MERCADO

   {r['mercado']}

═══════════════════════════════════════════

⚠ EVALUACIÓN DE RIESGO

   Riesgo:
      {r['riesgo']}

   Score:
      {r['score']}/100

═══════════════════════════════════════════

🖥 MÉTRICAS DEL SISTEMA

   Latencia:
      {r['latencia_total']} segundos

   Reporte PDF:
      ✓ Generado

═══════════════════════════════════════════

                ORION

═══════════════════════════════════════════
"""

        resultado.insert(
            "end",
            texto
        )

        boton.configure(
            state="normal"
        )

    except ValueError:

        boton.configure(
            state="normal"
        )

        messagebox.showerror(
            "Error",
            "Costo y margen deben ser números."
        )

    except Exception as e:

        boton.configure(
            state="normal"
        )

        messagebox.showerror(
            "Error",
            str(e)
        )


boton = ctk.CTkButton(
    app,
    text="🚀 ANALIZAR MERCADO",
    width=300,
    height=45,
    font=("Segoe UI",16,"bold"),
    command=lambda:
        threading.Thread(
            target=analizar,
            daemon=True
        ).start()
)

boton.pack(pady=15)
estado = ctk.CTkFrame(
    app,
    width=850,
    height=80
)

estado.pack(
    pady=10
)
texto_estado = """
🟢 Qwen3 Online
🟢 Pricing Engine
🟢 Memory System
🟢 Logger Active
🟢 Dashboard Active
🟢 PDF Reports
"""

label_estado = ctk.CTkLabel(
    estado,
    text=texto_estado,
    justify="left",
    font=("Segoe UI", 12)
)

label_estado.pack(
    pady=10
)
estadisticas = ctk.CTkFrame(
    app,
    width=850,
    height=70
)
app.mainloop()