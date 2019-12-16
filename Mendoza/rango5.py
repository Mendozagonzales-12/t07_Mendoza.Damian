#Programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años
#Muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
#Declaracion
cantidad,interes=0.0,0.0
años=0

#Input
cantidad=float(input("¿Cantidad a invertir? "))
interes=float(input("¿Interés porcentual anual? "))
años=int(input("¿Años?"))

for i in range(años):
    cantidad *= 1 + interes / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))
#fin_for
