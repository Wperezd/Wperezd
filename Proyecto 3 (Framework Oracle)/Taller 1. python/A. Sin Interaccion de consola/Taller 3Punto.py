import numpy as np

# Inicializar coordenadas rectangulares
X = 4
Y = 8
Z = 16

# ===============================
# CONVERSION A COORDENADAS CILINDRICAS
# ===============================

# r (radio en el plano XY)
r_cil = np.sqrt(X**2 + Y**2)

# theta en radianes (usar atan2 es mejor)
theta_cil_rad = np.arctan2(Y, X)

# theta en grados
theta_cil_deg = np.degrees(theta_cil_rad)

print("COORDENADAS CILINDRICAS:")
print("r =", r_cil)
print("theta (rad) =", theta_cil_rad)
print("theta (deg) =", theta_cil_deg)
print("z =", Z)


# ===============================
# CONVERSION A COORDENADAS ESFERICAS
# ===============================

# rho (distancia al origen)
rho = np.sqrt(X**2 + Y**2 + Z**2)

# theta (ángulo en el plano XY)
theta_esf_rad = np.arctan2(Y, X)
theta_esf_deg = np.degrees(theta_esf_rad)

# phi (ángulo respecto al eje Z)
phi_rad = np.arccos(Z / rho)
phi_deg = np.degrees(phi_rad)

print("\nCOORDENADAS ESFERICAS:")
print("rho =", rho)
print("theta (rad) =", theta_esf_rad)
print("theta (deg) =", theta_esf_deg)
print("phi (rad) =", phi_rad)
print("phi (deg) =", phi_deg)
