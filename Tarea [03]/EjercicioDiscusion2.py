import math


a = float(input("Ingrese el coeficiente a de la ecuación cuadrática: "))
b = float(input("Ingrese el coeficiente b de la ecuación cuadrática: "))
c = float(input("Ingrese el coeficiente c de la ecuación cuadrática: "))
discriminante = b**2 - 4 * a * c
x1 = 0
x2 = 0

#  Calculamos el discriminante de la ecuación cuadrática
discriminante = b**2 - 4 * a * c


if discriminante >= 0:
    #  Calculamos x1 y x2
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    # Paso 4.2: Imprimir los valores de x1 y x2
    print("Las raíces de la ecuación cuadrática son:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    # Calculamos x1 y x2 utilizando la fórmula de los complejos
    x1_real = -b / (2 * a)
    x1_imaginaria = abs(discriminante) / (2 * a)
    x2_real = -b / (2 * a)
    x2_imaginaria = -abs(discriminante) / (2 * a)
    # Resultado
    print("Las raíces conjugadas complejas de la ecuación cuadrática son:")
    print("x1 =", x1_real, "+ i *", x1_imaginaria)
    print("x2 =", x2_real, "- i *", x2_imaginaria)