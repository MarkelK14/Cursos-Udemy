from random import *

aleatorio = randint(1,50) #int
print(aleatorio)

aleatorio2 = round(uniform(1,50),2) #float
print(aleatorio2)

aleatorio3 = random() #elige aleatoriamente un num entre 0 y 1!
print(aleatorio3)

colores = ["Azul","Rojo","Verde","Amarillo"]
aleatorio4 = choice(colores) #Elige un item aleatorio de la lista
print(aleatorio4)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros) #Mezcla elementos de una lista
print(numeros)