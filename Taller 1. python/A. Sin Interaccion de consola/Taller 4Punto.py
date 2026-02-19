# Programa para calcular la resistencia de una PT100

# Coeficientes
A = 3.9080e-3
B = -5.8019e-7
C = -4.2735e-12

# Temperatura
T = 12  # grados Celsius

# Resistencia nominal
R0 = 100  # ohmios para PT100

# Calculo de la resistencia
if T >= 0:
    # Para temperaturas mayores o iguales a 0°C
    R = R0 * (1 + A*T + B*T**2)
else:
    # Para temperaturas menores a 0°C
    R = R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)

print("Temperatura:", T, "°C")
print("Resistencia PT100:", R, "ohmios")
