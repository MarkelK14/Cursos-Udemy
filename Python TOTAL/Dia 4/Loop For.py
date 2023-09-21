lista = ['A', 'B', 'C', 'D']

for letra in lista:
    numeroLetra = lista.index(letra) + 1
    print(f"Letra: {numeroLetra}: {letra}")

listaNombres = ["Pablo", "Laura", "Fede", "Luis", "Julia"]
for nombre in listaNombres:
    if nombre.startswith("L"):
        print(nombre)

listaNumeros = [1,2,3,4,5]
miValor = 0

for numero in listaNumeros:
    miValor = miValor + numero

print(miValor)

for letra in "Python":
    print(letra)

for item in [[1,2],[3,4],[5,6]]:
    print(item)

for a, b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {"Clave1":"A","Clave2":"B","Clave3":"C"}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)