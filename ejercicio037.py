'''
Un programa debe ser escrito para leer dos números y 
luego preguntar a la persona usuaria qué operación desea realizar. 
El resultado de la operación debe incluir información sobre el número, 
si es par o impar, positivo o negativo, e entero o decimal.
'''

numero_1 = float(input('Ingrese el primer número: '))
numero_2 = float(input('Ingrese el segundo número: '))
operacion = input('Ingrese la operacion a realizar (+, -, *, /):') 

if (operacion == '+'):
    resultado = numero_1 + numero_2
elif (operacion == '-'):
    resultado = numero_1 - numero_2
elif (operacion == '*'):
    resultado = numero_1 * numero_2
elif (operacion == '/'):
    resultado = numero_1 / numero_2
else:
    print('Operacion invalida!')

if (resultado % 2 == 0):
    print(f'El resultado es par: {resultado}')
else:
    print(f'El resultado es impar: {resultado}')

if (resultado > 0):
    print(f'El resultado es positivo: {resultado}')
else:
    print(f'El resultado es negativo: {resultado}')

if (resultado % 1 == 0):
    print(f'El resultado es entero: {resultado}')
else:
    print(f'El resultado es decimal: {resultado}')

