miSet = set([1,2,3,4,5])
print(type(miSet))
print(miSet)
print(len(miSet))
print(2 in miSet)
miSet.add(6)
print(miSet)
miSet.add(2)
print(miSet)
miSet.remove(3)
print(miSet)
#miSet.remove(7) #Da error porque el 7 no existe
miSet.discard(7)#Lo mismo que remove pero sin que de error
print(miSet)
sorteo = miSet.pop()#como set no tiene orden (no indexable), elimina un elemento aleatorio
print("sorteo: " + str(sorteo))
print(miSet)
miSet.clear() #Vacia el set
print(miSet)

miSet2 = {1,2,3,4,5}
print(type(miSet2))
print(miSet2)

miSet3 = {1,2,3,4,5,1,1,2,2,3,4,5,5}
print(miSet3)

miSet4 = set([1,2,(1,2,3),4,5])
print(miSet4)

miSet5 = {1,2,3}
miSet6 = {3,4,5}
miSet7 = miSet5.union(miSet6)
print(miSet7) #Como un elemento se repite, no lo coge
