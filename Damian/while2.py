#Programa que muestre si el cliente se encuentra en riesgo
#Declaracion
deuda_bcp=0
deuda_bvva=0

#Input
deuda_bcp_invalida=(deuda_bcp<10000 or deuda_bcp>50000)
deuda_bvva_invalida=(deuda_bvva<80000 or deuda_bvva>100000)

while(deuda_bcp_invalida):
    deuda_bcp=int(input("ingrese la deuda bcp del cliente:"))
    deuda_bcp_invalida=(deuda_bcp<10000 or deuda_bcp>50000)
#fin_while

while(deuda_bvva_invalida):
    deuda_bvva=int(input("Ingrese deuda bbva del cliente:"))
    deuda_bvva_invalida=(deuda_bvva<80000 or deuda_bvva>100000)
#fin_while
print("Cliente en rojo")
