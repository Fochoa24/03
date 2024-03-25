# Estructuras repetitivas: Permite la ejecucion repetida de un conjunto de instrucciones un numero determinado de veces.

# for i in range(1,5):

#  i=0
# while(i<n):
# i += 1 

# Declarar la primera variable igual a 0, siempre que se vayan a acumular, luego establecer el rango (1,10) 
#x1 = 0
#for i in range(1,11):
   # n = int(input("Ingrese la nota: "))
  #  x1 = x1 + n
 #   pg = x1/10
#print("El promedio general es", pg)



# Leer 8 numerosnaturalesy determine si es par e impar y cuantos pares e impares hay
x2 = 0
x3 = 0
for n in range(0,8):
    # Usar variables "contador"
    v = int(input("Digite un numero natural:"))
    if v%2==0:
        print ("Es par")
        x2+=1
    else:
        print ("Es impar")
        x3+=1
print("\nHay", x2,"numeros pares\ny", x3,"numeros impares.")
    