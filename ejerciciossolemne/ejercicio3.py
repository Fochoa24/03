# Desarrolle un algoritmo para convertir de metros a pies y pulgadas (1 metro igual a 39.37, 1pie = 12 pulgadas). Imprima el resultado por pantalla.


valor_de_1metro = 39.37
valor_de_1pie = 12
metros_a_converter = float(input("Digite la cantidad de metros que desea convertir: "))

# Conversión a piezas
piezas_convertidas = metros_a_converter * valor_de_1metro / valor_de_1pie 
print("\n{} metros son iguales a {} pie".format(metros_a_converter, round(piezas_convertidas, 2)))


