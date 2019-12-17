texto="QSKQ"
import os
texto=str(os.sys.argv[1])

for frase in texto:
#Si es Q muestre revisado
    if(frase=="Q"):
        print("Revisado")
#Si es S muestre falta corregir
    if(frase=="S"):
        print("Falta corregir")
#Si es K muestre tiene error
    if(frase=="K"):
        print("Tiene error")
        #fin_if
    #fin_for
