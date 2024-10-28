import math

# Definir variables
n = 1
suma = 0
pi = 0
precision = 10 ** (-3)
pi_anterior = 0


while True:
    # Calculamos el término 1
    termino1 = 1
    for i in range(n):
        termino1 *= 1 + (1 / 5) ** 2

    termino1 = 4 / termino1

    # Calculamos el término 2
    termino2 = 1
    for i in range(n):
        termino2 *= 1 + (1 / 239) ** 2

    termino2 = 4 / termino2

    # Sumamos ambos términos
    pi += ((-1) ** (n + 1)) * (termino1 - termino2)

    # Diferencia absoluta entre el valor de pi y pi calculado en la iteración
    if abs(math.pi - pi) < precision:

        break

    # Actualizar pi_anterior para la siguiente iteración
    pi_anterior = pi


    n += 1

# Resultado
print("Número de términos necesarios:", n)