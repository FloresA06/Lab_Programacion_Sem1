#Este programa calcula el IMC

peso=float(input("Ingresar su peso en kilogramos: "))
alt=float(input("Ingresar su altura en metros: "))

imc=peso/alt**2

print("Su indice de masa corporal (IMC) es: ", imc)