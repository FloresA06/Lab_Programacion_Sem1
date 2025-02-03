#Este programa compara dos numeros y especifica si son mayores, menores o iguales

num_1= float(input("Ingresar primer numero: "))
num_2= float(input("Ingresar segundo numero: "))

if(num_1>num_2):
	print(num_1, "es mayor que" ,num_2) 
elif(num_1<num_2):
	print(num_1, "es menor que", num_2)
else:
	print("Los numeros son iguales.")