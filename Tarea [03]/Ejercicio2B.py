import math

# Definir variables
n = 1
pi = math.pi
precision = 10 ** (-10)
x = 1
max_iterations = 10000  # Límite de iteraciones

# Calculamos la serie hasta cumplir la precisión requerida
while True:
    suma = 0  # Reiniciamos la suma a 0

    for i in range(1, n + 1):
        termino = ((-1) ** (i + 1) * x ** (2 * i - 1)) / (2 * i - 1)
        suma += termino

    # Calculamos P_n
    P_n = 4 * suma

    # Calculamos la diferencia con pi
    diferencia = abs(P_n - pi)

    # Comparamos
    if diferencia < precision:
        break

    # Incrementar n en 1
    n += 1

    # Verificar si el número de iteraciones ha alcanzado el límite
    if n > max_iterations:
        print("El número de iteraciones ha alcanzado el límite máximo sin converger.")
        break

# Resultado
print("Número de términos requeridos:", n)