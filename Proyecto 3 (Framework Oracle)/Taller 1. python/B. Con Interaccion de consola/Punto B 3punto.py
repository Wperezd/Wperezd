import math

print("CALCULADORA DE VOLUMENES")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Seleccione el sólido (1-4): "))

if opcion == 1:
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = area_base * altura
    print(f"El volumen del prisma es: {volumen}")

elif opcion == 2:
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = (area_base * altura) / 3
    print(f"El volumen de la pirámide es: {volumen}")

elif opcion == 3:
    R = float(input("Ingrese el radio mayor (R): "))
    r = float(input("Ingrese el radio menor (r): "))
    altura = float(input("Ingrese la altura: "))
    volumen = (math.pi * altura / 3) * (R**2 + r**2 + R*r)
    print(f"El volumen del cono truncado es: {volumen}")

elif opcion == 4:
    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))
    volumen = math.pi * radio**2 * altura
    print(f"El volumen del cilindro es: {volumen}")

else:
    print("Opción no válida")