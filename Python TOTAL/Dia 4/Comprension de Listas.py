palabra = "Python"
lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

lista2 = [letra for letra in palabra] #1 letra por cada letra que haya en palabra
print(lista2)

lista3 = [letra for letra in "palabra"] #1 letra por cada letra que haya en palabra
print(lista3)

lista4 = [n for n in range(0,21,2)]
print(lista4)

lista5 = [n/2 for n in range(0,21,2)]
print(lista5)

lista6 = [n for n in range(0,21,2) if n*2 > 10] #1 num por cada num siempre que el num * 2 sea > 10
print(lista6)

lista7 = [n if n*2 > 10 else "No" for n in range(0,21,2)] #si n*2 no es > 10 imprime 'No'
print(lista7)

pies = [10,20,30,40,50]
metros = [pie * 3.281 for pie in pies]
print(pies)
print(metros)