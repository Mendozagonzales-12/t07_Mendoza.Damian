#Programa para indicar si un caracter es vocal
#Declaracion
letra=""

#Input
letra_invalida=(letra!='a' and letra!='e' and letra!='i' and letra!='o' and letra!='u')

while(letra_invalida):
    letra=input("Ingrese una letra:")
    letra_invalida=(letra!='a' and letra!='e' and letra!='i' and letra!='o' and letra!='u')
#Fin_While
print ("La vocal es:",letra)
