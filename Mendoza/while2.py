#Programa Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
#Si se compran tres camisas o más se aplica un descuento del 20%
#sobre el total de la compra
#Declaracion
nc=0
costo,des,pt,pc=0.0,0.0,0.0,0.0


#Input
pc=float(input("Ingrese el precio de las camisas:"))
nc_invalido=(nc<3)

while(nc_invalido):
    nc=int(input("Ingrese la cantidad de camisas que desea el cliente:"))
    nc_invalido=(nc<3)
    costo=nc*pc
    des=costo*0.20
    pt=costo-des
#fin_while
print("El costo de las camisas es:",costo)
print("El descuento es:",des)
print("El costo total a pagar es",pt)

