texto = input("Ingresa un texto: ")
letras = input("Ingresa 3 letras a tu elección:")

listLetras = list(letras)
print(listLetras)

#Cuantas veces aparece cada letra
print(f"La letra '{listLetras[0]}' aparece {texto.lower().count(letras[0].lower())} veces en el texto")
print(f"La letra '{listLetras[1]}' aparece {texto.lower().count(letras[2].lower())} veces en el texto")
print(f"La letra '{listLetras[2]}' aparece {texto.lower().count(letras[2].lower())} veces en el texto")

#Cuantas palabras hay en total
print(f"Hay {len(texto.split())} palabras en el texto")

#Primera y última letra
print(f"La primera letra del texto es la letra '{texto[0]}', y la última es {texto[-1]}")

#Palabras en orden inverso
print(" ".join(texto.split(" ")[::-1]))

#Aparece Pyhton en el texto?
print("pyhton" in texto)
buscarPython = "python".lower() in texto.lower()
diccionario = {True:"si",False:"no"}
print(f"La palabra python {diccionario[buscarPython]} se encuentra en el texto")