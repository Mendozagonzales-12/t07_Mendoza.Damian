#Para tributar un determinado impuesto se debe ser mayor a 18 años
#tener unos ingresos superiores a 1000 soles mensuales
#Programa que pregunte al usuario su edad y sus ingresos mensuales
#Muestre en pantalla si el usuario tiene que tributar
#Declaracion
edad_usua=0
ingresos=0.0

#Input
edad_usua_invalida=(edad_usua<18 or edad_usua>90)
ingresos_invalido=(ingresos<1000)

while (edad_usua_invalida):
    edad_usua=int(input("Ingrese edad del usuario:"))
    edad_usua_invalida=(edad_usua<18 or edad_usua>90)
#fin_while

while (ingresos_invalido):
    ingresos=float(input("Ingrese los ingresos del usuario:"))
    ingresos_invalido=(ingresos<1000)
#fin_while
print("Tienes que cotizar")
