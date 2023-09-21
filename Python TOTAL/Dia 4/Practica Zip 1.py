capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for capital, pais in list(zip(capitales, paises)):
    print(f"La capital de {pais} es {capital}")