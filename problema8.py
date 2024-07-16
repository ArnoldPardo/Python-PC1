# Solicitar al usuario que ingrese la hora
hora_input = input("Introduce la hora en formato 24 horas (HH:MM): ")

# Separar horas y minutos
hora, minuto = map(int, hora_input.split(':'))

# Comprobar la hora para desayuno, almuerzo y cena
if (hora == 7 and 0 <= minuto <= 59) or (hora == 8 and minuto == 0):
    print("Es hora del desayuno.")
elif (hora == 12 and 0 <= minuto <= 59) or (hora == 13 and minuto == 0):
    print("Es hora del almuerzo.")
elif (hora == 18 and 0 <= minuto <= 59) or (hora == 19 and minuto == 0):
    print("Es hora de la cena.")
else:
    print("No es hora de comer.")
