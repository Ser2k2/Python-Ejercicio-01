'''
 Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
'''

numeroUno = float(input('Ingrese el primer número: '))
numeroDos = float(input('Ingrese el segundo número: '))

if (numeroUno > numeroDos):
    print(f'El primer número es mayor: {numeroUno}')
elif (numeroDos >numeroUno):
        print(f'El segundo número es mayor: {numeroDos}')
else:
      print(f'Ambos son iguales: {numeroUno} y {numeroDos}')

