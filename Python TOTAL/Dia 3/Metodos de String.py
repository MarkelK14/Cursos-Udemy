myString = "Este es el texto de Markel"
print(myString.upper())
print(myString.lower())
print(myString.split())
print(myString.split("t"))
print(" ".join(["Aprender","Python","es","genial"])) #Hay que pasarle una lista de palabras al separador.join
print(myString.find("o"))#igual que el index. La diferencia es que find si no existe devuelve un -1
print(myString.find("u"))#igual que el index. La diferencia es que find si no existe devuelve un -1
print(myString.replace("e","a"))
print(myString.replace("Markel","todos"))