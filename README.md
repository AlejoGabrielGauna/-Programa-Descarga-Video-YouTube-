# -Programa-Descarga-Video-YouTube-
Proyecto de Python, implementando las [yt-dlp | Tkinter | FFmpeg] para desarrollar una aplicacion de descarga de video YouTube.


# Descargador de YouTube

## Versión 0.1
### Descripción
Esta versión inicial permite la descarga de videos desde YouTube utilizando la biblioteca **yt-dlp** en Python. 

### Características:
- Descarga de videos en la mejor calidad disponible.
- Archivo descargado con nombre fijo: `Video_Descargado.mp4`.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Versión 0.2
### Descripción
Se implementa una interfaz gráfica de usuario (GUI) básica utilizando **Tkinter**, simplificando el uso de la aplicación para usuarios no técnicos.

### Características:
- Entrada de enlace de video y selección de carpeta de destino desde la GUI.
- Botón de descarga que inicia la operación.
- Barra de progreso para mostrar el avance de la descarga.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Versión 0.3
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

## Versión 0.4
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

Lista de Librerias usadas en las diferentes versiones:
--Versión 0.1
  >yt-dlp: Utilizada para manejar la descarga de videos de YouTube.
--Versión 0.2
  >yt-dlp: Sigue siendo la biblioteca principal para las descargas.
  >Tkinter: Utilizada para crear la interfaz gráfica básica, permitiendo al usuario ingresar enlaces y seleccionar carpetas.
--Versión 0.3
  >yt-dlp: Continua siendo utilizada para la funcionalidad de descarga.
  >Tkinter: Mejorada con estilos adicionales y funcionalidades como:
  >Barra de progreso para mostrar el avance de la descarga.
  >Centrado automático de la ventana.
  >Mejoras visuales en colores y estilos de botones.
--Versión 0.4
  >yt-dlp: Extendida para soportar la descarga de solo audio.
  >Tkinter: Ampliada para:
  >Soporte de interfaz personalizable con colores oscuros y texto blanco.
  >Nuevo botón "Aceptar" que aparece al completar la descarga.
  >FFmpeg (integrado con yt-dlp): Para convertir el audio descargado a formato MP3 con calidad específica.


