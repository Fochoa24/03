lista = ["Felipe Ochoa", "Estudiante de programacion", True, 1.68]
print(lista[0]) # Imprime el primer elemento de la lista (nombre)
print(lista[-1]) # Imprime el ultimo elemento de la lista (altura)
print(lista[1]) # Imprime el segundo elemento de la lista (Profesión)
# print(lista[4]) # Error: Indice fuera del rango de la lista

# Tupla = que una lista, solamente usas () en vez [] y no se pueden modificar!!

tupla = ("Felipe Ochoa", "Estudiante de programacion", True, 1.86)

# Creando un conjunto (set)

conjunto = {"perro","gato","cocodrillo"} # Elementos desordenados que pueden cambiar.
# No podemos acceder a un indice al hacer print.
# En un conjunto no puede haber datos duplicados!
print(conjunto)
# print(conjunto[3]) -> no puede acceder al elemnto

#Creando un diccionario

diccionario = {
    "Nombre": "Felipe Ochoa",
    "Edad" : 20,
    "Sexo" : "Masculino",
    "Hobby" : "Programación"
}   

print(diccionario["Nombre"]) # Accediendo a los valores por su clave.
print(diccionario.get("Edad")) # Devuelve el valor asociado con esa clave. Si no existe devuelve None.
print(diccionario.keys()) # Devuelve las claves del diccionario

