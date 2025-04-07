'''
Escribe un programa que lea tres números y los muestre en orden descendente.
'''

numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
numero_3 = int(input('Ingrese el tercero número: '))

if (numero_1 > numero_2 and numero_1 > numero_3):
    print(numero_1)
    if (numero_2 > numero_3):
        print(numero_2)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_2)

elif (numero_2 > numero_1 and numero_2 > numero_3):
    print(numero_2)
    if (numero_1 > numero_3):
        print(numero_1)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_1)
else:
    print(numero_3)
    if (numero_1 > numero_2):
        print(numero_1)
        print(numero_2)
    else:
        print(numero_2)
        print(numero_1)
