# Diccionario de tipos MIME
tipos_mime = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

# Solicitar el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo: ").strip()

# Obtener la extensión del archivo en minúsculas
extension = nombre_archivo.lower().rsplit('.', 1)[-1] if '.' in nombre_archivo else ''

# Determinar el tipo MIME
mime_type = tipos_mime.get('.' + extension, 'application/octet-stream')

# Mostrar el resultado
print(f"El tipo de archivo MIME es: {mime_type}")
