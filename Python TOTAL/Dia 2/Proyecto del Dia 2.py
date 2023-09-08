nombre = input("Tu nombre: ")
ventas = float(input("Tus ventas: "))
comision = ventas*13/100

print(f"{nombre}, te vas a llevar {round(comision,2)}€ de comisión")