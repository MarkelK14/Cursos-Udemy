nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]
ciudades = ["Lima", "Madrid", "Mexico"]
combinados = list(zip(nombres, edades))
print(combinados)

nombres2 = ["Ana", "Hugo", "Valeria"]
edades2 = [65, 29, 42, 55] #añadimos un valor
combinados2 = list(zip(nombres2, edades2)) #llega hasta el largo de la lista más corta
print(combinados2)

combinados3 = list(zip(nombres, edades, ciudades))
print(combinados3)

for nombre, edad, ciudad in combinados3:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")