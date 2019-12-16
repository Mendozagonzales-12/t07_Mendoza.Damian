#Programa sobre una lista de comida depende de la categoria para mostrar sus elementos
comida=""
import os

comida=str(os.sys.argv[1])

for i in comida:
    if(comida=="DESAYUNO"):
        print("LOS COMENSALES DESAYUNARAN: CEREALES CON YOGURTH Y TORTILLAS")
    if(comida=="ALMUERZO"):
        print("LOS COMENSALES ALMORZARAN: SOPA DE TRIGO, CABRITO Y SU REFRESCO DE CEBADA")
    if(comida=="CENA"):
        print("LOS COMENSALES CENARAN: MANZANILLA Y PANES CON MANTEQUILLA")
    #FIN_IF
#FIN_FOR
