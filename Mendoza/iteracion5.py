#Programa que pida dos numeros
#Declaracion
num1,num2=0,0
import os

#Input
num1=int(os.sys.argv[1])
num2=int(os.sys.argv[2])

for i in [num1 and num2]:
#Muestre en pantalla si el primero es mayor
    if(num1>num2):
        print("El primer numero",num1," es mayor que ",num2)
#si el numero 2>numero 1, indicarlo en pantalla
    if(num2>num1):
        print("Numero ",num2," Es mayor que ",num1)
#si los dos numeros pedidos son iguales mostrar en patalla
    if(num1==num2):
        print("Numero ",num1," Es igual que ",num2)
    #if_fin
#fin_for
