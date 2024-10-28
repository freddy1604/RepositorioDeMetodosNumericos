# Definir variables
n = int(input("Ingrese el número de elementos en las sumas: "))

#Inicializacion
suma_total = 0
multiplicacion_total = 0

for i in range(1, n + 1):
    # Realizar la multiplicación a_i * b_i
    a_i = int(input("Ingrese el valor de a_" + str(i) + ": "))
    b_i = int(input("Ingrese el valor de b_" + str(i) + ": "))
    multiplicacion = a_i * b_i

    # Sumamos el resultado de la multiplicación al total acumulado
    suma_total += multiplicacion

    # Sumamos el resultado de la multiplicación a la suma acumulada
    multiplicacion_total += multiplicacion

    multiplicacion_total += 1
    suma_total += 1

# Resultado
print("Número total de sumas realizadas:", suma_total)
print("Número total de multiplicaciones realizadas:", multiplicacion_total)