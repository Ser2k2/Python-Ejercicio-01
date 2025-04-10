'''
Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel 
[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. 
Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().
'''

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]


total_gastos = sum(gastos)
cantidad_compras = len(gastos)

media_gastos = total_gastos / cantidad_compras

print(f'El promedio de gastos es {media_gastos} reales.')

'''
Con los mismos datos de la pregunta anterior, 
determina cuántas compras se realizaron por encima de 3000 reales y 
calcula el porcentaje con respecto al total de compras.
'''

contador_3000 = 0

for gasto_3000 in gastos:
    if gasto_3000 > 3000:
        contador_3000 += 1

porcentaje_arriba3000 = 100 * contador_3000 / cantidad_compras

print(f'{contador_3000} compras estuvieron por encima de $3000,00 .')
print(f'{porcentaje_arriba3000}% de los gastos estuvieron por encima de $3000,00.')