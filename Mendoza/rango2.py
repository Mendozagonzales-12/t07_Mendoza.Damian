#Programa que pregunte al usuario su edad
#y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
#Declaracion
edad=0

#Input
edad=int(input("¿Cuántos años tienes? "))

for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")
#fin_for
