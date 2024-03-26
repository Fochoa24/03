print('Programa para calcular el peso promedio de un grupo de personas')

peso_niños = 0
num_niños = 0
peso_jovenes = 0
num_jovenes = 0
peso_adultos = 0
num_adultos = 0
peso_ancianos = 0
num_ancianos = 0

num_personas = int(input('Ingrese el numero de personas a evaluar: '))

for i in range(0, num_personas):
  edad = int(input(f'Ingrese la edad de la persona {i+1}: '))
  peso = int(input(f'Ingrese el peso de la persona {i+1}: '))
  if edad < 13:
    peso_niños += peso
    num_niños += 1
  elif edad < 30:
    peso_jovenes += peso
    num_jovenes += 1
  elif edad < 60:
    peso_adultos += peso
    num_adultos +=1
  else:
    peso_ancianos += peso
    num_ancianos += 1

if num_niños == 0:
  print('No ingreso niños')
else:
  print(f'El peso promedio de los niños es: {peso_niños/num_niños}')

if num_jovenes == 0:
  print('No ingreso jovenes')
else:
  print(f'El peso promedio de los jovenes es: {peso_jovenes/num_jovenes}')

if num_adultos == 0:
  print('No ingreso adultos')
else:
  print(f'El peso promedio de los adultos es: {peso_adultos/num_adultos}')

if num_ancianos == 0:
  print('No ingreso ancianos')
else:
  print(f'El peso promedio de los ancianos es: {peso_ancianos/num_ancianos}')


###################


print('Programa para contabilizar votos')

candidato_a = 0
candidato_b = 0
candidato_c = 0

num_votos = int(input('Ingrese el numero de votos: '))

while num_votos != 0:
  print('Seleccione uno de los siguentes candidatos: \n1. Candidato A \n2. Candidato B \n3. Candidato C')
  voto = int(input('Ingrese el voto: '))
  if voto == 1:
    candidato_a += 1
    num_votos -= 1
  elif voto == 2:
    candidato_b += 1
    num_votos -= 1
  elif voto == 3:
    candidato_c += 1
    num_votos -= 1
  else:
    print('Voto invalido')

print(f'El candidato A obtuvo {candidato_a} votos,\nEl candidato B obtuvo {candidato_b} votos,\nEl candidato C obtuvo {candidato_c} votos')


###################


print('Programa para calcular promedios de empleados')

trabajadores_1 = 0
sueldo_trabajadores_1 = 0
trabajadores_2 = 0
sueldo_trabajadores_2 = 0
trabajadores_3 = 0
sueldo_trabajadores_3 = 0

sueldo_1000 = 0
antiguedad_20_menos2000 = 0
antiguedad_15 = 0
mujeres_cat1_1500 = 0
cat3_1250a1700 = 0

num_empledos = int(input('Ingrese el numero de personas a evaluar: '))

for i in range(0, num_empleados):
  categoria = int(input(f'Ingrese la categoria del trabajador {i+1} (1,2,3): '))
  edad = int(input(f'Ingrese la edad de la persona {i+1}: '))
  sueldo = int(input(f'Ingrese el peso de la persona {i+1}: '))
  antiguedad = int(input(f'Ingrese la antiguedad de la persona {i+1}: '))
  genero = input(f'Ingrese el genero de la persona {i+1} (Masculino 1, Femenino 2): ')
  
  if categoria == 1:
    trabajadores_1 += 1
    num_trabajadores_1 += 1
  elif categoria == 2:
    trabajadores_2 += 1
    num_trabajadores_2 += 1
  elif categoria == 3:
    trabajadores_3 += 1
    num_trabajadores_3 += 1
  else:
    print('Empleado sin categoria')

if num_niños == 0:
  print('No ingreso niños')
else:
  print(f'El peso promedio de los niños es: {peso_niños/num_niños}')

if num_jovenes == 0:
  print('No ingreso jovenes')
else:
  print(f'El peso promedio de los jovenes es: {peso_jovenes/num_jovenes}')

if num_adultos == 0:
  print('No ingreso adultos')
else:
  print(f'El peso promedio de los adultos es: {peso_adultos/num_adultos}')

if num_ancianos == 0:
  print('No ingreso ancianos')
else:
  print(f'El peso promedio de los ancianos es: {peso_ancianos/num_ancianos}')


##############


print('Programa para calcular promedios de empleados')

trabajadores_1 = 0
sueldo_trabajadores_1 = 0

trabajadores_2 = 0
sueldo_trabajadores_2 = 0

trabajadores_3 = 0
sueldo_trabajadores_3 = 0
cat3_1250a1700 = 0

sueldo_1000 = 0

antiguedad_15 = 0
antiguedad_10_menos2000 = 0

mujeres_cat1_1500 = 0

num_empleados = int(input('Ingrese el numero de personas a evaluar: '))

for i in range(0, num_empleados):
  categoria = int(input(f'Ingrese la categoria del trabajador {i+1} (1,2,3): '))
  edad = int(input(f'Ingrese la edad de la persona {i+1}: '))
  sueldo = int(input(f'Ingrese el sueldo de la persona {i+1}: '))
  antiguedad = int(input(f'Ingrese la antiguedad de la persona {i+1}: '))
  genero = input(f'Ingrese el genero de la persona {i+1} (Femenino 1, Masculino 2): ')

  if categoria == 1:
    trabajadores_1 += 1
    sueldo_trabajadores_1 += sueldo
  elif categoria == 2:
    trabajadores_2 += 1
    sueldo_trabajadores_2 += sueldo
  elif categoria == 3:
    trabajadores_3 += 1
    sueldo_trabajadores_3 += sueldo
    if sueldo >= 1250 and sueldo <= 1700:
      cat3_1250a1700 += 1
  else:
    print('Empleado sin categoria')

  if sueldo > 1000:
    sueldo_1000 += 1
  if antiguedad  >= 10 and sueldo < 2000:
    antiguedad_10_menos2000 += 1
  if antiguedad > 15:
    antiguedad_15 += 1
  if genero == 1 and sueldo > 1500:
    mujeres_cat1_1500 += 1


if trabajadores_1 == 0:
  print('No ingreso trabajadores categoria 1')
else:
  print(f'El sueldo promedio de los empleados de categoria 1: {sueldo_trabajadores_1/trabajadores_1} y hay {trabajadores_1} de este tipo')

if trabajadores_2 == 0:
  print('No ingreso trabajadores categoria 2')
else:
  print(f'El sueldo promedio de los empleados de categoria 2: {sueldo_trabajadores_2/trabajadores_2} y hay {trabajadores_2} de este tipo')

if trabajadores_3 == 0:
  print('No ingreso trabajadores categoria 3')
else:
  print(f'El sueldo promedio de los empleados de categoria 3: {sueldo_trabajadores_3/trabajadores_3} y hay {trabajadores_3} de este tipo')
  print(f' Hay {cat3_1250a1700} empleados de categoria 3 que ganan entre 1250 y 1700')

print(f'Hay {sueldo_1000} empleados que ganan mas de 1000')
print(f'Hay {antiguedad_10_menos2000} empleados que tienen mas de 10 años de antiguedad y ganan menos de 2000')
print(f' Hay {antiguedad_15} empleados que tienen mas de 15 años de antiguedad')
print(f' Hay {mujeres_cat1_1500} mujeres que ganan mas de 1500 y estan en categoria 1')


###################

