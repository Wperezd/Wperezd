import numpy as np

PRESION_CILINDRO = 5          # bar
DIAMETRO_BASTAGO = 4.2        # mm
DIAMETRO_EMBOLO = 22          # mm

# CONVERSIONES

P = PRESION_CILINDRO * 1e5          # bar → Pascales
D_bastago = DIAMETRO_BASTAGO * 1e-3  # mm → metros
D_embolo = DIAMETRO_EMBOLO * 1e-3    # mm → metros

# FUERZA DE AVANCE

area_avance = (np.pi * D_embolo**2) / 4
FUERZA_AVANCE = P * area_avance

# FUERZA DE RETROCESO

area_retroceso = (np.pi * (D_embolo**2 - D_bastago**2)) / 4
FUERZA_RETROCESO = P * area_retroceso

# RESULTADOS

print("FUERZA DE AVANCE:", FUERZA_AVANCE, "N")
print("FUERZA DE RETROCESO:", FUERZA_RETROCESO, "N")
