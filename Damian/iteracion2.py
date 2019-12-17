#Programa que pida una letra
letra=""
import os
letra=str(os.sys.argv[1])

for palabra in letra:
#Si es A muestre aprobado
    if(letra=="A"):
        print("Aprobado")
#Si es B muestre regular
    if(letra=="B"):
        print("Regular")
#Si es C muestre desaprobado
    if(letra=="C"):
        print("Desaprobado")
    #fin_if
#fin_for

