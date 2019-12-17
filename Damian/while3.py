#Programa que muestre si la operacion es recomendada
#Declaracion
saldo_capital=0
suma_factores=0

#Input
saldo_capital_invalida=(saldo_capital<100 or saldo_capital>400)
suma_factores_invalido=(suma_factores<8)

while(saldo_capital_invalida):
    saldo_capital=int(input("ingrese el saldo capital del cliente:"))
    saldo_capital_invalida=(saldo_capital<100 or saldo_capital>400)
#fin_while

while(suma_factores_invalido):
    suma_factores=int(input("ingrese la cuota del cliente:"))
    suma_factores_invalido=(suma_factores<8)
#fin_while
print("la operacion a realizar no es recomendada")
