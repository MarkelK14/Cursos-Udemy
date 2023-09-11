miLista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
miLista2 = ["hola", 23, 45.98]
miLista3 = miLista
print(type(miLista))
print(type(miLista2))
print(len(miLista))#Cuantos elementos contiene la lista ==> Como en Stings
print(miLista[0])#Qué hay en la posición 0 de la lista ==> Como en Stings
print(miLista[0:2])#Qué hay de la posición 0 a la 2 (sin incluir) ==> Como en Stings
print(miLista[3:9:2])#Qué hay de la posición 3 a la 7 (sin incluir) saltando 2 ==> Como en Stings
print(miLista+miLista2)
miLista3[0] = "Alfa" #Modificar un elemento
print(miLista3)
miLista3.append("L") #Agregar nuevo elmento a la lista
print(miLista3)
miLista3.pop() #Por defecto elimina el ultimo elemento
print(miLista3)
miLista3.pop(0) #Elimina el elemento que esta en el indice 0
eliminado = miLista3.pop(0) #Elimina el elemento que esta en el indice 0 y lo en una variable
print(miLista3)
print(eliminado)

miLista4 = ["j","u","e","o","s","w","l","b"]
print(miLista4)
nuevaLista4 = miLista4.sort()#NULL
print(type(nuevaLista4))
miLista4.sort()#No devuelve nada, solo ordena
print(miLista4)
miLista4.reverse()#Invierte el orden
print(miLista4)