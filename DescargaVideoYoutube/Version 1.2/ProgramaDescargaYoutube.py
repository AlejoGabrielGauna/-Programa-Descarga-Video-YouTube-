import os
import threading
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog
from tkinter.ttk import Progressbar, Style
import yt_dlp


def seleccionar_carpeta():
    """Permitir al usuario seleccionar la carpeta de destino."""
    carpeta = filedialog.askdirectory()
    if carpeta:
        carpeta_destino.set(carpeta)


def descargar_video():
    """Iniciar la descarga del video."""
    enlace = url_var.get()
    destino = carpeta_destino.get()

    if not enlace or not destino:
        estado_var.set("Por favor, ingresa un enlace válido y selecciona una carpeta.")
        return

    estado_var.set("Descargando...")
    progress_bar["value"] = 0  # Reiniciar barra de progreso

    # Deshabilitar el botón de descargar mientras trabaja
    boton_descargar.config(state="disabled")

    # Hacer la descarga en un hilo separado para no congelar la interfaz
    threading.Thread(target=procesar_descarga, args=(enlace, destino)).start()


def procesar_descarga(enlace, destino):
    """Realizar la descarga del video usando yt-dlp."""
    opciones = {
        "format": "best",
        "outtmpl": os.path.join(destino, "%(title)s.%(ext)s"),  # Ruta del archivo descargado
        "no_color": True,  # Desactiva los colores ANSI en la salida
        "progress_hooks": [actualizar_progreso],  # Vincular la barra de progreso
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([enlace])
        estado_var.set("¡Descarga completada!")
        mostrar_boton_aceptar()
    except Exception as e:
        estado_var.set(f"Error: {e}")
    finally:
        # Habilitar el botón de descargar después de completar
        boton_descargar.config(state="normal")


def actualizar_progreso(d):
    """Actualizar la barra de progreso en función del estado de la descarga."""
    if d["status"] == "downloading":
        porcentaje = d.get("_percent_str", "0.0").strip().replace("%", "")
        try:
            progress_bar["value"] = float(porcentaje)  # Actualizar la barra
            estado_var.set(f"Descargando: {porcentaje}%")
        except ValueError:
            estado_var.set("Error al interpretar el progreso.")
    elif d["status"] == "finished":
        progress_bar["value"] = 100


def mostrar_boton_aceptar():
    """Mostrar el botón de aceptar una vez finalizada la descarga."""
    boton_aceptar.pack(pady=10)


# Crear la ventana principal
ventana = Tk()
ventana.title("Descargador de YouTube")
ventana.geometry("500x300")
ventana.resizable(False, False)

# Centrar la ventana en la pantalla
ventana.eval("tk::PlaceWindow . center")

# Estilo
ventana.configure(bg="#f2f2f2")  # Fondo gris claro
ventana.option_add("*Font", "Helvetica 10")  # Tipografía similar a sans-serif
style = Style()
style.theme_use("clam")
style.configure("TProgressbar", troughcolor="#d9d9d9", background="#ff8c00", thickness=15)  # Barra naranja

# Variables
url_var = StringVar()
carpeta_destino = StringVar()
estado_var = StringVar()

# Widgets
Label(ventana, text="Enlace del video de YouTube:", bg="#f2f2f2").pack(pady=10)
Entry(ventana, textvariable=url_var, width=50).pack()

Label(ventana, text="Carpeta de destino:", bg="#f2f2f2").pack(pady=10)
Entry(ventana, textvariable=carpeta_destino, width=50, state="readonly").pack()
Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta).pack(pady=5)

boton_descargar = Button(ventana, text="Descargar", command=descargar_video)
boton_descargar.pack(pady=10)

progress_bar = Progressbar(ventana, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
progress_bar.pack(pady=10)

Label(ventana, textvariable=estado_var, bg="#f2f2f2").pack(pady=10)

# Botón Aceptar (invisible hasta que termine la descarga)
boton_aceptar = Button(ventana, text="Aceptar", command=ventana.destroy)

# Iniciar la aplicación
ventana.mainloop()
