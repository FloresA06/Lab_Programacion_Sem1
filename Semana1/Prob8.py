#Este programa describe si un año en especifico es bisiesto o no

año=int(input("Ingresar año: "))

if(año%4==0):
	print(año, "es bisiesto.")
elif(año%400==0):
	print(año, "es bisiesto.")
else:
	print(año, "no es bisiesto.")