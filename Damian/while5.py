#Dado los numeros mostrar si el estudiante esta desaprobado
#Declaracion
exam1=0
exam2=0

#Input
exam1_invalido=(exam1<1 or exam1>10)
exam2_invalido=(exam2<2 or exam2>9)

while(exam1_invalido):
    exam1=int(input("Ingresar la nota del estudiante del primer examen:"))
    exam1_invalido=(exam1<1 or exam1>10)
#fin_while

while(exam2_invalido):
    exam2=int(input("ingresar la nota del estudiante del segundo examen :"))
    exam2_invalido=(exam2<2 or exam2>9)
#fin_while
print("El estudiante esta desaprobado")
