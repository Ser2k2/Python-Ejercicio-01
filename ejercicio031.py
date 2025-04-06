'''
Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y 
muestre el valor más alto y más bajo entre esos tres años.
'''

promedio_1 = float(input('Ingrese el precio promedio del vehiculo en el primer año: '))
promedio_2 = float(input('Ingrese el precio promedio del vehiculo en el segungo año: '))
promedio_3 = float(input('Ingrese el precio promedio del vehiculo en el tercer año: '))

if (promedio_1 >= promedio_2 and promedio_1 >= promedio_3):
    mayor = promedio_1
elif (promedio_2 >= promedio_1 and promedio_2 >= promedio_3):
    mayor = promedio_2
else:
    mayor = promedio_3

if (promedio_1 <= promedio_2 and promedio_1 <= promedio_3):
    menor = promedio_1
elif (promedio_2 <= promedio_1 and promedio_2 <= promedio_3):
    menor = promedio_2
else:
    menor = promedio_3

print(f'El precio más alto es $ {mayor}.')
print(f'El precio más bajo es $ {menor}.')