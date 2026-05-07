import os
import shutil
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageHandler:
    def __init__(self, carpeta_destino="backend/image", tamaño=(200, 200)):
        self.carpeta_destino = carpeta_destino
        self.tamaño = tamaño

        os.makedirs(self.carpeta_destino, exist_ok=True)

    def subir_imagen(self):
        """Abre selector y guarda imagen en carpeta destino"""
        ruta_origen = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif")]
        )

        if not ruta_origen:
            return None

        nombre = os.path.basename(ruta_origen)
        ruta_destino = os.path.join(self.carpeta_destino, nombre)

        shutil.copy(ruta_origen, ruta_destino)

        return ruta_destino

    def cargar_imagen(self, ruta):
        """Carga imagen lista para Tkinter Label"""
        img = Image.open(ruta)
        img = img.resize(self.tamaño)
        return ImageTk.PhotoImage(img)

    def image_defect(self):
        return self.cargar_imagen("backend/image/perfil_defecto.png")
