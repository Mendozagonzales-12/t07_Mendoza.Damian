#PROGRAMA QUE PIDA UN NUMERO PARA MOSTRAR LA TABLA DE MULTIPLICAR
numero=0
import os

numero=int(os.sys.argv[1])

for i in  [numero]:
#SI EL NUMERO ES 0 MUESTRA LA MULTIPLICACION DE 0*0=0
    if(numero==0):
        print(f"{numero} * {numero} = {numero ** 2}")
#SI EL NUMERO ES 1 MUESTRA LA MULTIPLICACION DE 1*1=1
    if(numero==1):
        print(f"{numero} * {numero} = {numero ** 2}")
#SI EL NUMERO ES 2 MUESTRA LA MULTIPLICACION DE 2*2=4
    if(numero==2):
        print(f"{numero} * {numero} = {numero ** 2}")
    #fin_if
    print("Final del if")
#fin_for
print("Final del for")
