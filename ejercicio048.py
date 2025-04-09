'''
Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. 
Escribe un programa que lea las edades de una cantidad no informada de clientes y 
muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. 
La entrada de datos se detendrá al ingresar un número negativo.
'''
contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0

edad = int(input('Ingrese la edad (o un número negativo para salir): '))

while (edad >= 0):
    if (0 >= edad <= 25):
        contador_0_25 += 1
    elif (26 >= edad <= 50):
        contador_26_50 += 1
    elif (51 >= edad <= 75):
        contador_51_75 += 1
    elif (76 >= edad <= 100):
        contador_76_100 += 1

    edad = int(input('Ingrese la edad (o un número negativo para salir): '))

print('Distribución de edades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)