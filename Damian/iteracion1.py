#Programa que pida una frase
texto=""
import os
texto=str(os.sys.argv[1])

for frase in texto:
#Si es # muestre auxilio
    if(texto=="#"):
        print("Auxilio")
#Si es $ muestre necesito ayuda
    if(texto=="$"):
        print("Necesito ayuda")
#Si es O muestre hablame urgente
    if(texto=="O"):
        print("Hablame urgente")
    #fin_if
#fin_for
