serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")


cliente = {"Nombre":"Federico",
           "Edad":45,
           "Ocupacion":"Instructor"}
pelicula = {"Titulo":"Matrix",
            "FichaTecnica": {"Protagonista":"Keanu Reeves",
                             "Director":"Lana y Lilly Wachowski"}}
elementos = [cliente, pelicula, "Libro"]
print(elementos)

for element in elementos:
    match element:
        case {"Nombre":Nombre,
              "Edad":Edad,
              "Ocupacion":Ocupacion}:
            print("Es un cliente")
            print(Nombre, Edad, Ocupacion)
        case {"Titulo":Titulo,
              "FichaTecnica":{"Protagonista":Protagonista,
                              "Director":Director}}:
            print("Es una pelicula")
            print(Titulo, Protagonista, Director)
        case _:
            print("No se que es esto")