print('Programa para calcular el peso promedio de un grupo de personas')

peso_niños = 0
num_niños = 0
peso_jovenes = 0
num_jovenes = 0
pesos_adultos = 0
num_adultos = 0
peso_anciano = 0
num_ancianos = 0

num_personas = int(input('Ingreseel numero de personas a evaluar: '))

for i in range(0, num_personas):
    edad = int(input(f'Ingrese la edad de la persona {i+1}: '))
    peso = int(input(f'Ingrese el peso de la persona {i+1} (en kg.): '))
    if edad <= 12: # Niño o menor de 12 años.
        peso_niños += peso
        num_niños += 1
    elif 13 <= edad <= 18:
        peso_jovenes += peso
        num_jovenes += 1
    else: # Mayor de 18 años.
        pesos_adultos +=  peso
        num_adultos += 1

promedio_peso_niños  = peso_niños / num_niños
promedio_peso_jovenes = peso_jovenes / num_jovenes
peso_promedio_adultos = pesos_adultos / num_adultos

# Se asume que los ancianos son mayores de 65 años.
edad_anciano = 65
peso_anciano = peso_anciano + ((num_personas - num_adultos) * peso_promedio_adultos) / (edad_anciano - 18)

print('\nPeso promedio de las  niñas/os menores de 12 años: ', round(promedio_peso_niños, 2), 'kg')
print('Peso promedio de las jóvenes/os entre 13 y 18 años: ', round(promedio_peso_jovenes, 2) ,'kg')
print('Peso promedio de las adultas/os mayores de 18 años: ', round(peso_promedio_adultos, 2), 'kg')
print('Pso promedio de la tercera edad: ', round(peso_anciano, 2), 'kg')

