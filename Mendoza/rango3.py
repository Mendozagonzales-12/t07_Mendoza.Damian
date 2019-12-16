#Programa que pida al usuario un número entero positivo
#y muestre por pantalla todos los números impares
#desde 1 hasta ese número separados por comas.
#Declaracion
nro=0

#Input
nro=int(input("Introduce un número entero positivo: "))

for i in range(1, nro+1, 2):
    print(i, end=", ")
#fin_for
