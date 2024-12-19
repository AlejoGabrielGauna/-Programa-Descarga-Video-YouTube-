import yt_dlp

link = input("Coloca el link del video aqui: ").strip()

# Configurar opciones de descarga
opciones = {
    "format": "best",  # Selecciona la mejor calidad disponible
    "outtmpl": "Video_Descargado.%(ext)s",  # Guardar como Video_Descargado.mp4
}

# Descargar el video
try:
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([link])
        print("Descarga terminada!!")
except Exception as e:
    print(f"Ocurrió un error: {e}")
