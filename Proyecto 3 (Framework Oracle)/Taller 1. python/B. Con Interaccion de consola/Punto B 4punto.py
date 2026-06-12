seleccion = """
Escriba la opcion de los siguientes robots:
(1) Robot Cartesiano
(2) Robot Cilindrico
(3) Robot Esferico
Digite aqui su opcion: 
"""

t = int(input(seleccion))

if t == 1:
    robot = ("El Robot Cartesiano es un robot tipo PPP, que tiene tres "
             "movimientos lineales y perpendiculares entre sí, "
             "Tiene 3 articulaciones en los tres ejes cartesianos X, Y y Z.")

elif t == 2:
    robot = ("El Robot Cilindrico es un robot tipo RPP, "
             "Tiene 3 articulaciones una articulación rotacional y dos prismáticas.")

elif t == 3:
    robot = ("El Robot Esferico es un robot tipo RRP, "
             "Tiene 3 articulaciones dos articulaciones rotacionales y una prismática.")

else:
    robot = "Vuelva a ejecutar el programa y escoja alguna de las 3 opciones."

print(robot)