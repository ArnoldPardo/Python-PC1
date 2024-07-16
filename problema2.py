# Solicitar el costo de la comida
costo_comida = float(input("¿Cuál fue el costo de su comida en el restaurante? $"))

# Solicitar el porcentaje de propina
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar? "))

# Calcular la cantidad de propina
propina = (costo_comida * porcentaje_propina) / 100

# Mostrar el resultado
print(f"La cantidad de propina a dejar es: ${propina:.2f}")
