#Programa que pida una frase
texto=""
import os
texto=str(os.sys.argv[1])

for frase in texto:
#Si es # muestre auxilio
    if(frase=="#"):
        print("Auxilio")
#Si es $ muestre necesito ayuda
    if(frase=="$"):
        print("Necesito ayuda")
#Si es O muestre hablame urgente
    if(frase=="O"):
        print("Hablame urgente")
    #fin_if
#fin_for
