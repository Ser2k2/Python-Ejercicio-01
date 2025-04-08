'''
Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y calcule su promedio. 
La lectura debe detenerse al ingresar el valor -273°C.
'''


sumaTempC = 0
contador = 0

tempCelsius = float(input('Ingrese la temperatura en Celsius (C): '))

while (tempCelsius != -273 ):
    sumaTempC += tempCelsius
    contador += 1
    tempCelsius = float(input('Ingrese la temperatura en Celsius (C): '))
    

print(f'El promedio  de las temperaturas en Celsius (C) es: {sumaTempC / contador}.')
#print(f'Suma: {sumaTempC}')
#print(f'contador: {contador}')