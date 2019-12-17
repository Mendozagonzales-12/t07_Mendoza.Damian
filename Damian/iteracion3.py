texto="QSKQ"
import os
texto=str(os.sys.argv[1])

for frase in texto:
#Si es Q muestre revisado
    if(texto=="Q"):
        print("Revisado")
#Si es S muestre falta corregir
    if(texto=="S"):
        print("Falta corregir")
#Si es K muestre tiene error
    if(texto=="K"):
        print("Tiene error")
        #fin_if
    #fin_for
