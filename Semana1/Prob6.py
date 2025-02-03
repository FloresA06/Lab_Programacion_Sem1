#Este programa convierte grados Celsius a Fahrenheit y Kelvin

temp_cel=float(input("Ingresar temperatura en Celsius: "))

temp_far=temp_cel*9/5+32
temp_kel=temp_cel+273.15

print("La temperatura en grados Fahrenheit es: ",temp_far)
print("La temperatura en grados Kelvin es: ", temp_kel)