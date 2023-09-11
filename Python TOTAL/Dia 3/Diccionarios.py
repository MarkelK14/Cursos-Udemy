diccionario = {"C1":"valor1", "C2":"valor2"}
print(type(diccionario))
print(diccionario)

print(diccionario["C1"]) #Buscar lo que hay en la clave C1

cliente = {"Nombre":"Juan", "Apellido":"Fuentes", "Edad":34, "Estatura":1.78}
print(type(cliente["Apellido"]))
print(cliente["Apellido"])
print(type(cliente["Edad"]))
print(cliente["Edad"])

dic = {"C1":55,"C2":[10,20,30],"C3":{"S1":100,"S2":200}}#Un diccionario puede almacenar listas y más diccionarios dentro
print(dic["C2"])
print(dic["C2"][1])
print(dic["C3"])
print(dic["C3"]["S2"])

dic2 = {"C1":["A","B","C"], "C2":["D","E","F"]}
print(dic2["C2"][1].lower())

dic3 = {"C1":"A","C2":"B"}
print(dic3)
dic3["C3"] = "C"
print(dic3)

dic4 = {1:"A",2:"B"}
print(dic4)
dic4[3] = "C"
print(dic4)
dic4[2] = "b"
print(dic4)
print(dic4.keys())
print(dic4.values())
print(dic4.items())