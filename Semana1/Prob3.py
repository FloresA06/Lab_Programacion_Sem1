#Este programa indica si un numero es par o impar

num= float(input("Ingresar un numero: "))

#El residuo siempre es cero cuando se divide un numero par entre dos, de ahi la condicion establecida
if(num%2==0):
	print("El numero es par.")
else:
	print("El numero es impar.")