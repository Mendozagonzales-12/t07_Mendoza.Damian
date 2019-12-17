#Programa que muestre el importe alto del cliente
#Declaracion
capital_inicial=0.0
interes_simple=0.0

#Input
capital_inicial_invalido=(capital_inicial<200.9 or capital_inicial>600.9)
interes_simple_invalido=(interes_simple<0.5 or interes_simple>0.9)

while(capital_inicial_invalido):
    capital_inicial=int(input("Ingrese la capital inicial:"))
    capital_inicial_invalido=(capital_inicial<200.9 or capital_inicial>600.9)
#fin_while

while(interes_simple_invalido):
    interes_simple=float(input("ingrese el interes simple:"))
    interes_simple_invalido=(interes_simple>0.5 or interes_simple>0.9)
#fin_while
print("importe de interes alto")
