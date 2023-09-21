habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"


if sabe_python == True:
    if habla_ingles == True:
        print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas tener conocimientos de inglés")
else:
    if habla_ingles == True:
        print("Para postularte, necesitas saber programar en Python")
    else:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")