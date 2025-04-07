'''
Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.
'''

producto_1 = float(input('Ingrese el precio del primer producto: '))
producto_2 = float(input('Ingrese el precio del segundo producto: '))
producto_3 = float(input('Ingrese el precio del tercer producto: '))

if (producto_1 < producto_2 and producto_1 < producto_3):
    print('El primer producto es el más baratato.')
elif (producto_2 < producto_1 and producto_2 < producto_3):
    print('El segundo producto es el más barato.')
else:
    print('El tercer producto es el más barato.')