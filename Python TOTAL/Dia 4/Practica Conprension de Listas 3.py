temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(temp-32)*(5/9) for temp in temperatura_fahrenheit]

print(grados_celsius)