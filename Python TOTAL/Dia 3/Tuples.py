miTuple = (1,2,3)
miTuple2 = 1,2,3
miTuple3 = (5,5.6,"string")
print(type(miTuple))
print(type(miTuple2))
print(type(miTuple3))

print(miTuple[0])
print(miTuple[-1])

miTuple4 = (1,2,(10,20))
print(miTuple4[2])
print(miTuple4[2][1])
print(type(list(miTuple4)))

x, y, z = miTuple
print(miTuple)
print(x, y, z)

miTuple5 = (1,2,3,4,1)
print("len(miTuple) ==> " + str(len(miTuple5)));
print(miTuple5.count(1))
print(miTuple5.index(2))