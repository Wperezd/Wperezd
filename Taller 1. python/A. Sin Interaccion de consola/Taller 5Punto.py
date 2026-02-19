import numpy as np

# =====================================
# FUNCIONES DE ROTACION
# =====================================

def rotacion_x(angulo):
    rad = np.radians(angulo)
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(rad), -np.sin(rad)],
        [0, np.sin(rad),  np.cos(rad)]
    ])
    return Rx


def rotacion_y(angulo):
    rad = np.radians(angulo)
    Ry = np.array([
        [ np.cos(rad), 0, np.sin(rad)],
        [0, 1, 0],
        [-np.sin(rad), 0, np.cos(rad)]
    ])
    return Ry


def rotacion_z(angulo):
    rad = np.radians(angulo)
    Rz = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad),  np.cos(rad), 0],
        [0, 0, 1]
    ])
    return Rz


# =====================================
# LLAMAR FUNCIONES
# =====================================

ROTACION_X = rotacion_x(0)   # ROLL
ROTACION_Y = rotacion_y(0)   # PITCH
ROTACION_Z = rotacion_z(0)   # YAW

print("Rotacion en X:")
print(ROTACION_X)

print("\nRotacion en Y:")
print(ROTACION_Y)

print("\nRotacion en Z:")
print(ROTACION_Z)
