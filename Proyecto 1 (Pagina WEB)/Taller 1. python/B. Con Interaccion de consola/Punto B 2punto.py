import random

# Pedir datos al usuario
m = int(input("Introduzca el rango minimo: "))
p = int(input("Introduzca el rango maximo: "))
a = int(input("Introduzca la cantidad de numeros a calcular aleatoriamente: "))

# Generar números aleatorios en el rango [m, p]
X = [random.randint(m, p) for _ in range(a)]

# Mostrar resultados
print("El Numero de numeros calculados es:")
print(X)