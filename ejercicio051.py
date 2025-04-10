'''
Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].
'''

lista_numeros = []

for contador in range(0, 5):
    numero = int(input('Ingresa un numero entero: '))
    lista_numeros.append(numero)

print(f'Lista de numeros ingresados: {lista_numeros}')

'''
Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.
'''

print(f'Lista de numeros invertida: {lista_numeros[:: -1]}')