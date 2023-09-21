print(min(2,6,4,8,0,1,5))
print(max(2,6,4,8,0,1,5))

lista = [43,65,26,24,86,23,45,73,54]
print(min(lista))
print(max(lista))

nombres = ["Juan", "Pablo", "Alicia", "Carlos"]
print(min(nombres))
print(max(nombres))

nombre = "Markel"
print(min(nombre)) #Primero busca en mayus y luego minus
print(min(nombre))
print(min(nombre.lower()))

dic = {"C1":45, "C2":11, "C3":35}
print(min(dic))
print(min(dic.values()))