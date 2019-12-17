texto="EBRE"
import os
texto=str(os.sys.argv[1])

for letra in texto:
#Si es R muestre cliente en riesgo
    if(letra=="R"):
        print("Cliente en riesgo")
#Si es B muestre buen cliente
    if(letra=="B"):
        print("Buen cliente")
#Si es E muestre excelente cliente
    if(letra=="E"):
        print("Excelente cliente")
        #fin_if
    #fin_for

