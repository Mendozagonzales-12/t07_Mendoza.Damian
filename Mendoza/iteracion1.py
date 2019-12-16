#Programa que pida una palabra
palabra=""
import os

palabra=str(os.sys.argv[1])

for i in [palabra]:
#SI LA PALABRA ES HOLA MUESTRE ¿COMO ESTAS?
    if(palabra=="HOLA"):
        print("¿COMO ESTAS?")
#SI LA PALABRA ES DIME MUESTRE ¿QUE PASO?
    if(palabra=="DIME"):
        print("¿QUE PASO?")
#SI LA PALABRA ES CHAU MUESTRE HASTA LUEGO
    if(palabra=="CHAU"):
        print("HASTA LUEGO")
    #fin_if
#fin_for
