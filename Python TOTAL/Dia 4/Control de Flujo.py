if 10 > 9:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "perro"
if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("No sé qué animal tienes")

edad = 23
calificacion = 9

if edad > 18:
    print("Eres mayor de edad")
    if calificacion >= 5:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres menor de edad")