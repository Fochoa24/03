# Dado tres números: Determinar si la suma de cualquier pareja de ellos es igual
# al tercer número. Si se cumple esta condición escribir “iguales” y en caso contrario
# escribir “distinto”

v = 0
x = 0
w = 0

v = int(input("Ingrese el primer numero: "))
w = int(input("Ingrese el segundo numero: "))
x = int(input("Ingrese el tercer numero: "))
if (v + w == x) or (v + x == w):
    print("iguales")
else:
    print("impares")