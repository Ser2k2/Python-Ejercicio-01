'''
 Los números primos tienen diversas aplicaciones en Ciencia de Datos, 
 como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. 
 Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.
'''

numero = int(input('Ingresa un número entero: '))

if (numero > 1): #Los números menores o iguales a 1 no son primos
    if (numero <= 3): #Los números 2 y 3 son primos
        print(f' {numero} es un número primo.')
    elif ((numero % 2 == 0) or (numero % 3 == 0)): #Los números divisibles por 2 o 3 no son primos
        print(f' {numero} no es un número primo.')
    else:
         print(f'{numero} es un número primo.')
        
else:
    print(f'{numero} no es un número primo.')


