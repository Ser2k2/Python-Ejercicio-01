'''
En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas 
anuales para ayudar a la dirección en la toma de decisiones. 
El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y 
calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar 
las siguientes sugerencias:

Para una variación superior al 20%: bonificación para el equipo de ventas.
Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
Para bonificaciones inferiores al -10%: recorte de gastos.
'''

ventas_2022 = float(input('Ingrese la cantidad de ventass en 2022: '))
ventas_2023 = float(input('Ingrese la cantidad de ventqas en 2023: '))


variacion_porcentual = 100 * (ventas_2023 - ventas_2022) / (ventas_2022)

if (variacion_porcentual > 20):
    print('Bonificación para el equipo de venta')
elif (2 <= variacion_porcentual <= 20):
    print('Pequeña bonificación para el equipo de venta')
elif (-10 <= variacion_porcentual < 2):
    print('Planificación de políticas de incentivo a las venta')
else:
    print('Recorte de gasto')