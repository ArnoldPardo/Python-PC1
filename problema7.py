# Solicitar al usuario que ingrese dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostrar el menú de opciones
print("\nSelecciona una opción:")
print("1. Sumar los dos números")
print("2. Restar el primer número menos el segundo")
print("3. Multiplicar los dos números")

# Leer la opción del usuario
opcion = input("Opción elegida: ")

# Realizar la operación correspondiente
if opcion == '1':
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
else:
    print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
