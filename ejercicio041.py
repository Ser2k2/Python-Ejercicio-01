'''
Escribe un programa que solicite dos números enteros e imprima todos los números enteros entre ellos.
'''

inicio = int(input('Ingrese el primer númro: '))
fin = int(input('Ingrese el segundo númro: '))

if (inicio < fin):
    for numero in range (inicio + 1, fin):
        print(numero)
elif (inicio > fin):
    for numero in range (fin + 1, inicio):
        print(numero)
else:
    print('Los números son iguales!')
