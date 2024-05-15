from PIL import Image, ImageFilter, ImageOps
import os

# Ruta de las carpetas que contienen las imágenes
bien = r'C:/Users/jimen/Desktop/Tyre dataset/Tyre dataset/Good'
mal = r'C:/Users/jimen/Desktop/Tyre dataset/Tyre dataset/Defective'
carpeta_destino_bien = r'C:/Users/jimen/Desktop/Tyre dataset/Tyre dataset/DatosModelo/BuenEstado'
carpeta_destino_mal = r'C:/Users/jimen/Desktop/Tyre dataset/Tyre dataset/DatosModelo/MalEstado'


# Función para aplicar modificaciones a una imagen
def modificaciones(imagen, clase, nuevo_ancho, nuevo_alto):
    imagen_gris = imagen.convert('L') # Convertir a escala de grises
    imagen_redimensionada = imagen_gris.resize((nuevo_ancho, nuevo_alto)) # Redimensionar
    imagen_filtrada = imagen_redimensionada.filter(ImageFilter.MedianFilter()) # Aplicar filtrado de mediana
    imagen_ecualizada = ImageOps.equalize(imagen_filtrada) # Ecualizar histograma
    # Determinar carpeta de destino
    if clase == 'bien':
        carpeta_destino = carpeta_destino_bien
    elif clase == 'mal':
        carpeta_destino = carpeta_destino_mal
    # Guardar la imagen modificada
    nombre_archivo = os.path.basename(imagen.filename)
    ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
    imagen_ecualizada.save(ruta_destino)

# Procesar imágenes de la carpeta "bien"
for archivo in os.listdir(bien):
    ruta_imagen = os.path.join(bien, archivo)
    imagen = Image.open(ruta_imagen)
    modificaciones(imagen, 'bien', 256, 256)

# Procesar imágenes de la carpeta "mal"
for archivo in os.listdir(mal):
    ruta_imagen = os.path.join(mal, archivo)
    imagen = Image.open(ruta_imagen)
    modificaciones(imagen, 'mal', 256, 256)
