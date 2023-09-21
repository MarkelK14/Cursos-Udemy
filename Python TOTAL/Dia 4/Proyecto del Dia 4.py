from random import *

nombre = input("Tu nombre: ")
print(f"{nombre}, piensa en un numero entre el 1 y el 100. Tienes solo 8 intentos para adivinarlo")
numeroAleatorio = randint(1,100)

print(f"NumAleatorio = {numeroAleatorio}")

intento = 1
while intento < 9:
    print(f"Intento Nº {intento}")
    numero = int(input("Numero: "))
    if numero < 1 or numero > 100:
        print("El numero tiene que ser entre 1 y 100")
        intento += 1
        continue
    else:
        if numero < numeroAleatorio:
            print("El premiado es mas grande que el introducido")
            intento += 1
        elif numero > numeroAleatorio:
            print(("El numero premiado es más pequeño que el introducido"))
            intento += 1
        else:
            print(f"HAS GANADO! Lo conseguiste en {intento} intento(s)")
            break
if intento == 9:
    print(("GAME OVER"))