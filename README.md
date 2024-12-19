# -Programa-Descarga-Video-YouTube-
Proyecto de Python, implementando las [yt-dlp | Tkinter | FFmpeg] para desarrollar una aplicacion de descarga de video YouTube.


# Descargador de YouTube

## Versión 1.0
### Descripción
Esta versión inicial permite la descarga de videos desde YouTube utilizando la biblioteca **yt-dlp** en Python. 

### Características:
- Descarga de videos en la mejor calidad disponible.
- Archivo descargado con nombre fijo: `Video_Descargado.mp4`.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Versión 1.1
### Descripción
Se implementa una interfaz gráfica de usuario (GUI) básica utilizando **Tkinter**, simplificando el uso de la aplicación para usuarios no técnicos.

### Características:
- Entrada de enlace de video y selección de carpeta de destino desde la GUI.
- Botón de descarga que inicia la operación.
- Barra de progreso para mostrar el avance de la descarga.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Versión 1.2
### Descripción
La interfaz se mejora con nuevas funcionalidades y ajustes de diseño.

### Características:
- Centrado automático de la ventana en la pantalla.
- Mejoras visuales:
  - Fondo gris claro.
  - Barra de progreso en color naranja.
  - Estilo más atractivo y consistente en botones y textos.
- Mensajes claros para informar sobre el estado de la descarga.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Versión 1.3
### Descripción
Se introducen opciones adicionales y ajustes para una experiencia más completa y funcional.

### Características:
- Descarga de solo audio en formato MP3 con calidad de 192 kbps.
- Configuración para convertir automáticamente el audio descargado usando **FFmpeg**.
- Personalización de la interfaz con colores similares al fondo de este chat:
  - Fondo gris oscuro.
  - Texto blanco.
- Botón "Aceptar" que aparece al finalizar la descarga y permite cerrar la aplicación.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Lista de Librerias usadas en las diferentes versiones:
- Versión 1.0
  - yt-dlp: Utilizada para manejar la descarga de videos de YouTube.
- Versión 1.1
  - yt-dlp: Sigue siendo la biblioteca principal para las descargas.
  - Tkinter: Utilizada para crear la interfaz gráfica básica, permitiendo al usuario ingresar enlaces y seleccionar carpetas.
- Versión 1.2
  - yt-dlp: Continua siendo utilizada para la funcionalidad de descarga.
  - Tkinter: Mejorada con estilos adicionales y funcionalidades como:
  - Barra de progreso para mostrar el avance de la descarga.
  - Centrado automático de la ventana.
  - Mejoras visuales en colores y estilos de botones.
- Versión 1.3
  - yt-dlp: Extendida para soportar la descarga de solo audio.
  - Tkinter: Ampliada para:
  - Soporte de interfaz personalizable con colores oscuros y texto blanco.
  - Nuevo botón "Aceptar" que aparece al completar la descarga.
  - FFmpeg (integrado con yt-dlp): Para convertir el audio descargado a formato MP3 con calidad específica.
 
_________________________________________________________________________________________________________________________________________________________________________


-YouTube-Video-Download-Program-
Python project, implementing [yt-dlp | Tkinter | FFmpeg] to develop a YouTube video download application.

YouTube Downloader
Version 1.0
Description
This initial version allows downloading videos from YouTube using the yt-dlp library in Python.

Features:
- Download videos in the best available quality.
- Downloaded file with a fixed name: Video_Descargado.mp4.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Version 1.1
Description
A basic graphical user interface (GUI) is implemented using Tkinter, simplifying the application for non-technical users.

Features:
- Video link input and destination folder selection through the GUI.
- Download button to start the operation.
- Progress bar to display download progress.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Version 1.2
Description
The interface is enhanced with new functionalities and design adjustments.

Features:
- Automatic centering of the window on the screen.
- Visual improvements:
  - Light gray background.
  - Progress bar in orange color.
  - More attractive and consistent style for buttons and text.
- Clear messages to inform about the download status.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Version 1.3
Description
Additional options and adjustments are introduced for a more complete and functional experience.

Features:
- Audio-only download in MP3 format with 192 kbps quality.
- Configuration to automatically convert the downloaded audio using FFmpeg.
- Interface customization with colors similar to the background of this chat:
  - Dark gray background.
  - White text.
- "Accept" button that appears when the download is completed, allowing the application to close.

List of Libraries used in different versions:
- Version 1.0
  - yt-dlp: Used to handle YouTube video downloads.

- Version 1.1
  - yt-dlp: Remains the main library for downloads.
  - Tkinter: Used to create the basic graphical user interface, allowing users to enter links and select folders.

- Version 1.2
  - yt-dlp: Still used for download functionality.
  - Tkinter: Enhanced with additional styles and functionalities such as:
    - Progress bar to display download progress.
    - Automatic centering of the window.
    - Visual improvements in colors and button styles.

- Version 1.3
  - yt-dlp: Extended to support audio-only downloads.
  - Tkinter: Expanded to include:
    - Support for a customizable interface with dark colors and white text.
    - New "Accept" button that appears upon download completion.
  - FFmpeg (integrated with yt-dlp): To convert the downloaded audio into MP3 format with specific quality.




