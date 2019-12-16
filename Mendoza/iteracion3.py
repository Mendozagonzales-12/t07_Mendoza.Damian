#PROGRAMA QUE PIDA UNA LETRA Y FORME UNA PALABRA AL FINAL
letra=""
import os

letra=str(os.sys.argv[1])

for i in [letra]:
#SI LA LETRA ES T MUESTRE DAME UNA T
    if(letra=="T"):
        print(f"Dame una {letra}")
#SI LA LETRA ES I MUESTRE DAME UNA I
    if(letra=="I"):
        print(f"Dame una {letra}")
#SI LA LETRA ES A MUESTRE DAME UNA A Y AL FINAL MUESTRE PALABRA COMPLETA
    if(letra=="A"):
        print(f"Dame una {letra}")
        print("¡TIA!")
    #fin_if
#FIN_FOR
