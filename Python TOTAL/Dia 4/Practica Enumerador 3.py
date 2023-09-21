lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(index)