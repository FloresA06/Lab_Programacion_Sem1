#Este programa separa edades en distintas categorias

edad=int(input("Ingresar edad: "))

#Estableciendo las condiciones e imprimiendo resultados
if(edad<12):
	print("Usted es un niño.")
elif(edad<18):
	print("Usted es un adolescente.")
elif(edad<60):
	print("Usted es un adulto.")
else:
	print("Usted es un adulto mayor.")