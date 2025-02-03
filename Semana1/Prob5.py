#Este programa aplica calcula el descuento de un producto y lo aplica

precio=float(input("Ingresar precio del producto: "))
por_desc=int(input("Ingresar porcentaje de descuento: "))

pre_desc=precio*por_desc/100
total=precio-pre_desc

print("El precio con el descuento aplicado es de: ", total)

