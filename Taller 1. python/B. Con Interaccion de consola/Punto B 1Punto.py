# Programa para calcular la potencia eléctrica

# Pedir datos al usuario
voltaje = float(input("Ingrese el valor del voltaje (V): "))
corriente = float(input("Ingrese el valor de la corriente (A): "))

# Calcular la potencia
potencia = voltaje * corriente

# Mostrar resultado
print("La potencia consumida es:", potencia, "Watts")