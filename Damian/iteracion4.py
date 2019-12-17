texto="EBRE"
import os
texto=str(os.sys.argv[1])

for letra in texto:
#Si es R muestre cliente en riesgo
    if(texto=="R"):
        print("Cliente en riesgo")
#Si es B muestre buen cliente
    if(texto=="B"):
        print("Buen cliente")
#Si es E muestre excelente cliente
    if(texto=="E"):
        print("Excelente cliente")
        #fin_if
    #fin_for

