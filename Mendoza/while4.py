#Programa que muestre
#si el signo es ARIES, LEO O SANGITARIO pertenece a la categoria FUEGO
#Declaracion
signo=""

#Input
signo_invalido=(signo!="ARIES" and signo!="LEO" and signo!="SAGITARIO")

#Processing

while(signo_invalido):
    signo=input("Ingrese su signo:")
    signo_invalido=(signo!="ARIES" and signo!="LEO" and signo!="SAGITARIO")
#Fin_While
print(signo,"pertenece a la categoria FUEGO")
