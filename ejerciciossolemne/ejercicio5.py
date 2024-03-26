# Calcular el total que una persona debe pagar en una cauchera, si el precio de cada caucho es de 800$ si se compran menos de 5 cauchos y 700$ si se compran 5 o más

print("Calculadora de caucho")

caucho = 800
caucho50 = 700
precio_caja = int(input("Ingrese el precio por cada caucho: "))
unidades = int(input("Cuantas unidades desea comprar?: "))
total = (caucho * precio_caja)
if total > 1500 :
    print ("El monto a pagar es de: ", total - 200 )
else:
    print ("El monto a pagar es de: ", total)
    

