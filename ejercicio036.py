'''
Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
'''

numero = float(input('Ingrese un numero: '))
residuo = numero % 1

#Si el residuo es '0', el número es entero si no es decimal.

if (residuo == 0):
    print(f'Número entero: {numero}')
    #print(residuo)
else:
    print(f'Número decimal: {numero}')
    #print(residuo)