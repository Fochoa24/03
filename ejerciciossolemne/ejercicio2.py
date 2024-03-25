# Dado tres numeros: Determinar si la suma de cualquier pareja de ellos es igual al tercer numero. Si se cumple esta condicion escribr "iguales" y en caso contrario escribir "distinto"

numero1 =   8
numero2 =  45
numero3 = 123

# Operadores de asignación: +=, -=, *=, /=, %=

print("Numero 1 antes del incremento en uno: ", numero1)
numero1 += 1 # Es lo mismo que escribir numero1 = numero1 + 1
print("Numero 1 después del incremento en uno: ", numero1)

print("\n")

print("Numero 2 antes de la resta con 7: ", numero2)
numero2 -= 7 # Es lo mismo que escribir numero2 = numero2 -  7
print("Numero 2 después de la resta con 7: ", numero2)

print("\n")

resultado_multiplicacion = numero1 * numero3
print(f"La multiplicación de {numero1} y {numero3} es: {resultado_multiplicacion}")

division = numero2 / numero1
print(f"\nEl cociente de la división entre {numero2} y {numero1} es: {division}")
resto = numero2 % numero1
print(f"\nEl resto de la division entre {numero2} y {numero1}")



