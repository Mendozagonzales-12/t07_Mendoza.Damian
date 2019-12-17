#Programa que pida una letra
letra=""
import os
letra=str(os.sys.argv[1])

for palabra in letra:
#Si es A muestre aprobado
    if(palabra=="A"):
        print("Aprobado")
#Si es B muestre regular
    if(palabra=="B"):
        print("Regular")
#Si es C muestre desaprobado
    if(palabra=="C"):
        print("Desaprobado")
    #fin_if
#fin_for

