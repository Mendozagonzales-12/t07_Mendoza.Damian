#Programa que pregunte al usuario su renta anual
#muestre por pantalla si la renta>=10000 y renta<20000 entonces su tipo de impositivo es 5
#Declaracion
renta=0.0

#Input
renta_invalida=(renta<10000 or renta>=20000)

while(renta_invalida):
    renta=float(input("Ingrese su renta anual:"))
    renta_invalida=(renta<10000 or renta>=20000)
#Fin_While
print("TU TIPO IMPOSITIVO ES DEL 15%")
