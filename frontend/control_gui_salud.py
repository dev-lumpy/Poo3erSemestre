import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────────
#  CLASE ABSTRACTA BASE
# ─────────────────────────────────────────────
class FormularioBase(ABC):
    """
    Clase abstracta base para todos los formularios del sistema.
    Define la interfaz común para recolectar y leer datos del usuario.
    """

    def __init__(self, parent: tk.Toplevel | tk.Tk, titulo: str):
        self.parent = parent
        self.titulo = titulo
        self._datos: dict = {}          # almacena los valores capturados
        self._widgets: dict = {}        # referencia a cada widget de entrada
        self._ventana: tk.Toplevel | None = None

    # ── Métodos que DEBEN implementarse ────────────────────────────────────
    @abstractmethod
    def construir_formulario(self, frame: tk.Frame) -> None:
        """Construye los widgets del formulario dentro del frame dado."""
        ...

    @abstractmethod
    def validar(self) -> bool:
        """Valida los campos del formulario. Retorna True si son correctos."""
        ...

    @abstractmethod
    def guardar(self) -> None:
        """Persiste o envía los datos recolectados al sistema."""
        ...

    # ── Métodos comunes heredados ────────────────────────────────────────
    def obtener_datos(self) -> dict:
        """Retorna un diccionario con todos los datos recolectados."""
        self._recolectar_datos()
        return dict(self._datos)

    def _recolectar_datos(self) -> None:
        """Lee el valor actual de cada widget registrado en _widgets."""
        for clave, widget in self._widgets.items():
            if isinstance(widget, (tk.Entry, ttk.Entry)):
                self._datos[clave] = widget.get().strip()
            elif isinstance(widget, tk.Text):
                self._datos[clave] = widget.get("1.0", tk.END).strip()
            elif isinstance(widget, ttk.Combobox):
                self._datos[clave] = widget.get()
            elif isinstance(widget, tk.StringVar):
                self._datos[clave] = widget.get()

    def abrir(self) -> None:
        """Abre la ventana del formulario."""
        self._ventana = tk.Toplevel(self.parent)
        self._configurar_ventana(self._ventana)
        self._construir_ui(self._ventana)

    def _configurar_ventana(self, ventana: tk.Toplevel) -> None:
        ventana.title(self.titulo)
        ventana.configure(bg="#1e3a5f")
        ventana.resizable(False, False)
        ventana.grab_set()

    def _construir_ui(self, ventana: tk.Toplevel) -> None:
        """Marco visual compartido por todos los formularios."""
        # Encabezado
        header = tk.Frame(ventana, bg="#1e3a5f", pady=15)
        header.pack(fill="x")
        tk.Label(
            header,
            text=f"📋  {self.titulo}",
            font=("Segoe UI", 14, "bold"),
            bg="#1e3a5f",
            fg="white",
        ).pack()
        tk.Label(
            header,
            text="Complete los datos del formulario",
            font=("Segoe UI", 9),
            bg="#1e3a5f",
            fg="#a0b8d0",
        ).pack()

        # Contenedor principal
        contenedor = tk.Frame(ventana, bg="#f0f4f8", padx=20, pady=20)
        contenedor.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Delegar construcción a la subclase
        self.construir_formulario(contenedor)

        # Botones comunes
        self._crear_botones(contenedor)

    def _crear_botones(self, parent: tk.Frame) -> None:
        frame_btns = tk.Frame(parent, bg="#f0f4f8", pady=10)
        frame_btns.pack(fill="x")

        btn_style = {
            "font": ("Segoe UI", 10, "bold"),
            "relief": "flat",
            "cursor": "hand2",
            "bd": 0,
            "padx": 20,
            "pady": 8,
        }

        tk.Button(
            frame_btns,
            text="💾  Guardar",
            bg="#2979c4",
            fg="white",
            activebackground="#1a5fa8",
            command=self._accion_guardar,
            **btn_style,
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            frame_btns,
            text="✖  Cancelar",
            bg="#e0e0e0",
            fg="#333",
            activebackground="#bdbdbd",
            command=lambda: self._ventana.destroy() if self._ventana else None,
            **btn_style,
        ).pack(side="left")

    def _accion_guardar(self) -> None:
        if self.validar():
            self._recolectar_datos()
            self.guardar()


# ─────────────────────────────────────────────
#  FORMULARIO CONTROL DE SALUD
# ─────────────────────────────────────────────
class FormularioControlSalud(FormularioBase):
    """
    Formulario de Control de Salud que hereda de FormularioBase..
    Recolecta: identificación, fecha, talla, peso y lista de observaciones.
    """

    # Paleta (igual al sistema existente)
    COLOR_BG_CARD   = "#3ab0e8"   # azul claro de las tarjetas
    COLOR_ENTRY_BG  = "#5cb85c"   # verde de los Entry
    COLOR_ENTRY_FG  = "white"
    COLOR_BTN_ADD   = "#5cb85c"
    COLOR_BTN_DEL   = "#e05252"
    COLOR_FRAME_OBS = "#3ab0e8"   # frame de observaciones
    COLOR_LABEL     = "white"

    def __init__(self, parent):
        super().__init__(parent, "Registro de Control de Salud")
        self._observaciones: list[str] = []   # lista interna de observaciones
        self._obs_entries:   list[tk.Entry] = []
        self._obs_frame_inner: tk.Frame | None = None

    # ── Implementación abstracta ─────────────────────────────────────────
    def construir_formulario(self, frame: tk.Frame) -> None:
        """Construye la tarjeta de datos personales + frame de observaciones."""
        # ── Tarjeta superior (datos básicos) ─────────────────────────────
        card_datos = tk.Frame(frame, bg=self.COLOR_BG_CARD, bd=0,
                              relief="flat", padx=16, pady=12)
        card_datos.pack(fill="x", pady=(0, 10))
        card_datos.configure(highlightthickness=0)

        # Agregar esquinas redondeadas simuladas con un poco de padding
        self._campo(card_datos, "Identificación:", "identificacion", row=0)
        self._campo(card_datos, "Fecha:",          "fecha",          row=1,
                    default=datetime.today().strftime("%d/%m/%Y"))
        self._campo_talla(card_datos, row=2)
        self._campo(card_datos, "Peso:",           "peso",           row=3)

        # ── Frame de observaciones ───────────────────────────────────────
        frame_obs = tk.LabelFrame(
            frame,
            text=" Observaciones ",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLOR_FRAME_OBS,
            fg="white",
            padx=8, pady=8,
            bd=2, relief="groove",
        )
        frame_obs.pack(fill="both", expand=True)

        # Botón "+"
        tk.Button(
            frame_obs,
            text=" + Agregar observación",
            bg=self.COLOR_BTN_ADD,
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            bd=0, padx=10, pady=4,
            command=self._agregar_obs,
        ).pack(anchor="w", pady=(0, 6))

        # Canvas + scrollbar para la lista de entries
        canvas = tk.Canvas(frame_obs, bg=self.COLOR_FRAME_OBS,
                           highlightthickness=0, height=130)
        scrollbar = ttk.Scrollbar(frame_obs, orient="vertical",
                                  command=canvas.yview)
        self._obs_frame_inner = tk.Frame(canvas, bg=self.COLOR_FRAME_OBS)

        self._obs_frame_inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.create_window((0, 0), window=self._obs_frame_inner, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Agregar 3 observaciones de ejemplo
        for _ in range(3):
            self._agregar_obs()

    def validar(self) -> bool:
        datos = {}
        for clave, widget in self._widgets.items():
            val = widget.get().strip() if isinstance(widget, tk.Entry) else widget.get()
            datos[clave] = val

        if not datos.get("identificacion"):
            self._mostrar_error("El campo Identificación es obligatorio.")
            return False
        if not datos.get("fecha"):
            self._mostrar_error("El campo Fecha es obligatorio.")
            return False
        return True

    def guardar(self) -> None:
        datos = self.obtener_datos()
        # Aquí se conectaría con la capa de persistencia del sistema
        print("=" * 50)
        print("DATOS RECOLECTADOS – Control de Salud")
        for k, v in datos.items():
            print(f"  {k:20}: {v}")
        print("=" * 50)
        if self._ventana:
            self._ventana.destroy()

    # ── Lectura pública (para el sistema externo) ─────────────────────────
    def obtener_datos(self) -> dict:
        """Retorna todos los datos + lista de observaciones."""
        super()._recolectar_datos()
        # Agregar observaciones como lista y como texto plano
        obs = [e.get().strip() for e in self._obs_entries if e.get().strip()]
        self._datos["observaciones"]      = obs
        self._datos["observaciones_texto"] = "\n".join(obs)
        return dict(self._datos)

    # ── Helpers privados ──────────────────────────────────────────────────
    def _campo(self, parent, label_text, key, row, default=""):
        """Crea una fila label + entry y la registra en _widgets."""
        tk.Label(
            parent, text=label_text,
            font=("Segoe UI", 10), bg=self.COLOR_BG_CARD, fg=self.COLOR_LABEL,
        ).grid(row=row, column=0, sticky="w", pady=4, padx=(0, 12))

        entry = tk.Entry(
            parent,
            bg=self.COLOR_ENTRY_BG, fg=self.COLOR_ENTRY_FG,
            insertbackground="white",
            font=("Segoe UI", 10), relief="flat",
            width=24,
        )
        entry.grid(row=row, column=1, sticky="ew", pady=4)
        if default:
            entry.insert(0, default)
        self._widgets[key] = entry
        parent.columnconfigure(1, weight=1)

    def _campo_talla(self, parent, row):
        """Fila especial Talla con spinner N emblemático."""
        tk.Label(
            parent, text="Talla:",
            font=("Segoe UI", 10), bg=self.COLOR_BG_CARD, fg=self.COLOR_LABEL,
        ).grid(row=row, column=0, sticky="w", pady=4, padx=(0, 12))

        sub = tk.Frame(parent, bg=self.COLOR_BG_CARD)
        sub.grid(row=row, column=1, sticky="ew", pady=4)

        # Icono N (simulado)
        tk.Label(sub, text="✦", bg="#2979c4", fg="white",
                 font=("Segoe UI", 9, "bold"), padx=3).pack(side="left")

        entry = tk.Entry(
            sub,
            bg=self.COLOR_ENTRY_BG, fg=self.COLOR_ENTRY_FG,
            insertbackground="white",
            font=("Segoe UI", 10), relief="flat", width=20,
        )
        entry.pack(side="left", fill="x", expand=True, padx=(4, 0))
        self._widgets["talla"] = entry

    def _agregar_obs(self):
        """Agrega un nuevo Entry de observación a la lista."""
        fila = tk.Frame(self._obs_frame_inner, bg=self.COLOR_FRAME_OBS)
        fila.pack(fill="x", pady=2)

        entry = tk.Entry(
            fila,
            bg=self.COLOR_ENTRY_BG, fg=self.COLOR_ENTRY_FG,
            insertbackground="white",
            font=("Segoe UI", 9), relief="flat",
        )
        entry.pack(side="left", fill="x", expand=True)
        self._obs_entries.append(entry)

        # Botón eliminar fila
        tk.Button(
            fila,
            text="✖", bg=self.COLOR_BTN_DEL, fg="white",
            font=("Segoe UI", 8, "bold"), relief="flat",
            cursor="hand2", bd=0, padx=6,
            command=lambda f=fila, e=entry: self._eliminar_obs(f, e),
        ).pack(side="left", padx=(4, 0))

    def _eliminar_obs(self, fila: tk.Frame, entry: tk.Entry):
        if entry in self._obs_entries:
            self._obs_entries.remove(entry)
        fila.destroy()

    @staticmethod
    def _mostrar_error(msg: str):
        import tkinter.messagebox as mb
        mb.showerror("Error de validación", msg)


class AbstraccionFormularioControlSalud(FormularioControlSalud):
    """
    Clase que hereda de FormularioControlSalud para especializar 
    la salida de datos y añadir lógica de procesamiento.
    """

    def __init__(self, parent):
        # Inicializamos la clase padre (FormularioControlSalud)
        super().__init__(parent)
        self.titulo = "Resumen Especializado de Salud"

    def obtener_metricas_fisicas(self) -> dict:
        """
        Extrae específicamente los campos numéricos para cálculos.
        """
        datos = self.obtener_datos()
        return {
            "talla": datos.get("talla", "0"),
            "peso": datos.get("peso", "0")
        }

    def obtener_solo_observaciones(self) -> list:
        """
        Retorna exclusivamente la lista de strings de las observaciones.
        """
        return [e.get().strip() for e in self._obs_entries if e.get().strip()]

    def guardar(self) -> None:
        """
        Sobrescribe el método guardar para, por ejemplo, 
        formatear la salida antes de cerrar.
        """
        if not self.validar():
            return

        datos = self.obtener_datos()
        
        # Lógica personalizada de guardado
        print(f"--- PROCESANDO REGISTRO DE: {datos['identificacion']} ---")
        print(f"Fecha: {datos['fecha']}")
        print(f"Cantidad de observaciones: {len(datos['observaciones'])}")
        
        # Aquí podrías llamar a una base de datos o un servicio externo
        super().guardar()