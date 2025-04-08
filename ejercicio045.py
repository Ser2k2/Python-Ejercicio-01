'''
Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. 
Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. 
Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.
'''

numeroFactorial = int(input('Ingrese un número entero para calcular su factorial: '))
factorial = 1

for numero in range(numeroFactorial, 0, -1):
    #print(numero)
    factorial *= numero
    #print(factorial)

print(f'El factorial de {numeroFactorial}! es {factorial}')