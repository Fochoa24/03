print('Programa para calcular el descuentos')
monto = int(input('Ingrese el valor de la compra: '))
if monto < 500:
  descuento = 0
  print('No hay descuento disponible para su compra')
elif monto <1000:
  descuento = monto*0.08
  print('Tiene un descuento del 8%')
elif monto <7000:
  descuento = monto*0.11
  print('Tiene un descuento del 11%')
elif monto <15000:
  descuento = monto*0.18
  print('Tiene un descuento del 18%')
else:
  descuento = monto*0.25
  print('Tiene un descuento del 25%')

print('El costo final de su compra es:', monto-descuento)

