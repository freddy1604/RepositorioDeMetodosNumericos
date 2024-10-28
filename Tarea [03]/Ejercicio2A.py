# Definir variables
n = 1
suma = 0
x = 1
pi = 3.14159265358979323846  # Valor de pi

# Definir la precisión requerida
precision = 1e-3


while True:
    # Calculamos la serie
    for i in range(1, n+1):
        termino = ((-1) ** (i + 1)) * (x ** (2 * i - 1)) / (2 * i - 1)
        suma += termino

    # Calculamos P_n
    P_n = 4 * suma

    # Calculamos la diferencia con pi
    diferencia = abs(P_n - pi)

    # Comparamos
    if diferencia < precision:
        break  # Salir del bucle si se cumple la precisión

    # Incrementamos n y reiniciamos la suma para la siguiente iteración
    n += 1
    suma = 0

# Resultado
print("Número de términos necesarios:", n)