lista = ["A","B","C"]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)

for indice,item in enumerate(range(50,55)):
    print(indice,item)

misTuples = list(enumerate(lista))
print(misTuples)
print(misTuples[1])
print(misTuples[1][1])