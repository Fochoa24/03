# Promedio de notas hasta n

print ("Programa para calcular el promedio de N notas")

i=0
n = int(input("Cuantas notas desea ingresar? "))
sumaNotas = 0

while i<n :
   nota = float(input("Ingrese la "+ str(i+1) +"° nota: "))
   sumaNotas += nota
   i+=1
promedio = sumaNotas/n
print("\nEl promedio de las", n, "notas es: ", promedio)

   