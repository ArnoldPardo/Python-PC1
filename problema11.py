# Lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Eliminar duplicados manteniendo el orden
lista_procesada = []
for item in lista_original:
    if item not in lista_procesada:
        lista_procesada.append(item)

# Mostrar la lista procesada
print("Lista procesada:", lista_procesada)
