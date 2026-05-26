import customtkinter as ctk
import threading
from main import analizar_consulta

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class OrionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ORION v2")
        self.geometry("950x700")
        self.resizable(False, False)

        titulo = ctk.CTkLabel(
            self,
            text="🧠ORION v2🧠",
            font=("Segoe UI", 30, "bold")
        )
        titulo.pack(pady=(20, 5))

        subtitulo = ctk.CTkLabel(
            self,
            text="Consultoría Estratégica Inteligente",
            font=("Segoe UI", 14)
        )
        subtitulo.pack()

        self.input_box = ctk.CTkEntry(
            self,
            width=750,
            height=45,
            placeholder_text="Escribe tu consulta estratégica..."
        )
        self.input_box.pack(pady=20)

        botones = ctk.CTkFrame(self)
        botones.pack()

        self.btn_analizar = ctk.CTkButton(
            botones,
            text="Analizar",
            width=140,
            command=self.iniciar
        )
        self.btn_analizar.pack(side="left", padx=10)

        btn_limpiar = ctk.CTkButton(
            botones,
            text="Limpiar",
            width=140,
            command=self.limpiar
        )
        btn_limpiar.pack(side="left", padx=10)

        self.output = ctk.CTkTextbox(
            self,
            width=880,
            height=500,
            font=("Consolas", 13)
        )
        self.output.pack(pady=20)

    def limpiar(self):
        self.output.delete("1.0", "end")
        self.input_box.delete(0, "end")

    def iniciar(self):
        query = self.input_box.get().strip()

        if not query:
            return

        self.output.delete("1.0", "end")
        self.output.insert("end", "🧠 ORION analizando...\n")

        hilo = threading.Thread(
            target=self.ejecutar,
            args=(query,)
        )
        hilo.start()

    def ejecutar(self, query):
        try:
            resultado = analizar_consulta(query)

            self.output.delete("1.0", "end")
            self.output.insert("end", resultado)

        except Exception as e:
            self.output.delete("1.0", "end")
            self.output.insert("end", f"Error: {e}")


if __name__ == "__main__":
    app = OrionApp()
    app.mainloop()