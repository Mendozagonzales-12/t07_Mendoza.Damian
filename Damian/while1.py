#Programa que muestre si la operacion es ineficiente
#Declaracion
precio_venta=0.0
precio_compra=0.0

#Input
precio_compra_invalida=(precio_compra<100 or precio_compra>200)
precio_venta_invalida=(precio_venta<50 or precio_venta<100)

while(precio_compra_invalida):
    precio_compra=float(input("ingrese el precio de compra del producto:"))
    precio_compra_invalida=(precio_compra<100 or precio_compra>200)
#fin_while

while(precio_venta_invalida):
    precio_venta=float(input("ingrese el precio de venta del producto:"))
    precio_venta_invalida=(precio_venta<50 or precio_venta>100)
#fin_while

print("Operacion ineficiente")
