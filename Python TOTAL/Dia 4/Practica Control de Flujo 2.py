edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    if tiene_licencia == False:
        print("No puedes conducir. Necesitas contar con una licencia")
    else:
        print("Puedes conducir")