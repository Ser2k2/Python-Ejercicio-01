'''
Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, 
según la elección del usuario. Como ejemplo, para el número 2, la tabla de multiplicar debe mostrarse en el siguiente formato:
'''
tablaNumero = int(input('Ingrese un número del 1 al 10: '))

print(f'Tabla de Multiplicar del {tablaNumero}')

for numero in range (1, 11):
    print(f'{tablaNumero} x {numero} = {tablaNumero * numero}')