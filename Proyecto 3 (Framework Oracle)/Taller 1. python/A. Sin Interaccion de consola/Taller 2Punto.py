import numpy as np

# Inicializar matrices
b1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

b2 = np.array([[7, 4, 1],
               [8, 5, 2],
               [9, 6, 3]])

# SUMA DE LAS MATRICES
suma_matrices = b1 + b2
print("SUMA:")
print(suma_matrices)

# RESTA DE LAS MATRICES
resta_matrices = b1 - b2
print("\nRESTA:")
print(resta_matrices)

# MULTIPLICACION MATRICIAL (producto matricial real)
producto_matricial = np.matmul(b1, b2)
print("\nMULTIPLICACION:")
print(producto_matricial)

# PRODUCTO PUNTO (elemento a elemento y luego suma total)
producto_punto = np.sum(b1 * b2)
print("\nPRODUCTO PUNTO:", producto_punto)

# PRODUCTO CRUZ (por filas, como en MATLAB)
producto_cruz = np.cross(b1, b2)
print("\nPRODUCTO CRUZ:")
print(producto_cruz)

# DIVISION ELEMENTO A ELEMENTO
division_matrices = b1 / b2
print("\nDIVISION ELEMENTO A ELEMENTO:")
print(division_matrices)
