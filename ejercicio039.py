'''
Un establecimiento está vendiendo combustibles con descuentos variables. 
Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. 
En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, 
el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y 
el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y 
el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:

El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro 
por la cantidad de litros menos el valor del descuento resultante del cálculo.
'''

litros_combustible = float(input('Ingrese la cantidad de litros vendidos: '))
tipo_combustible = input('Ingrese el tipo de combustible (E) Etanlol ó (D) Diésel: ')

if (tipo_combustible.upper() == 'E'):
    precio_litro = 1.70

    if (litros_combustible <= 15):
        descuento = 0.02
    else:
        descuento = 0.04
elif (tipo_combustible.upper() == 'D'):
    precio_litro = 2.00

    if (litros_combustible <= 15):
        descuento = 0.03
    else:
        descuento = 0.05
else:
    print('Entradas no validas!')
    precio_litro = 0
    descuento = 0

valor_descuento = precio_litro * litros_combustible * descuento
valor_pagado = precio_litro * litros_combustible - valor_descuento

print(f'Precio a pagar por el cliente: $ {valor_pagado} ') 