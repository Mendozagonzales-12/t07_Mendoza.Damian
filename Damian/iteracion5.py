Asignacion="BMDM"
import os
Asignacion=str(os.sys.argv[1])

for letra in Asignacion:
#Si es B muestre buen alumno
    if(letra=="B"):
        print("Buen alumno")
#Si es D muestre alumno deficiente
    if(letra=="D"):
        print("Alumno deficiente")
#Si es M muetre mal alumno
    if(letra=="M"):
        print("Mal alumno")
    #fin_if
#fin_for
