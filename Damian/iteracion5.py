Asignacion="BMDM"
import os
Asignacion=str(os.sys.argv[1])

for letra in Asignacion:
#Si es B muestre buen alumno
    if(Asignacion=="B"):
        print("Buen alumno")
#Si es D muestre alumno deficiente
    if(Asignacion=="D"):
        print("Alumno deficiente")
#Si es M muetre mal alumno
    if(Asignacion=="M"):
        print("Mal alumno")
    #fin_if
#fin_for
