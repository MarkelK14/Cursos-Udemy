monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else:
    print("No tengo más dinero")

respuesta = "S"

while respuesta == "S":
    respuesta = input("Quieres seguir? (S/N) ").upper()
else:
    print("Gracias")

while respuesta == "S":
    pass #es para que ignore la iteración. "Ticket para reservar un espacio para el developer"
print("Hola")

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra.upper() == "K":
        break #Para el loop
    print(letra)

for letra in nombre:
    if letra.upper() == "K":
        continue #Salta la iteración, pasa a la siguiente iteración
    print(letra)