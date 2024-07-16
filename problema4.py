# Solicitar un entero positivo al usuario
N = int(input("Introduce un entero positivo: "))


if N > 0:
    # Calcular la suma de los primeros N enteros
    suma = (N * (N + 1)) // 2  
    # Mostrar el resultado
    print(f"La suma de los enteros desde 1 hasta {N} es: {suma}")
else:
    print("Por favor, introduce un entero positivo.")
