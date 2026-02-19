# Taller 1
# Programa que suma, resta, multiplica (producto punto,
# producto cruz y elemento a elemento) y divide dos vectores

import numpy as np

# Inicializar vectores
a1 = np.array([2, 3, 4])
a2 = np.array([1, 4, 7])

# SUMA DE LOS VECTORES
suma_vectores = a1 + a2
print("SUMA:", suma_vectores)

# RESTA DE LOS VECTORES
resta_vectores = a1 - a2
print("RESTA:", resta_vectores)

# MULTIPLICACION DE LOS VECTORES
multiplica_vectores = a1 * a2
print("MULTIPLICACION:", multiplica_vectores)

# PRODUCTO PUNTO
producto_punto = np.dot(a1, a2)
print("PRODUCTO PUNTO:", producto_punto)

# PRODUCTO CRUZ
producto_cruz = np.cross(a1, a2)
print("PRODUCTO CRUZ:", producto_cruz)

# DIVISION ELEMENTO A ELEMENTO
division_vectores = a1 / a2
print("DIVISION:", division_vectores)


