'''
Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, 
necesitamos verificar si las calificaciones son válidas. Por lo tanto, 
escribe un programa que recibirá calificaciones del 0 al 5 y verificará si son valores válidos. 
Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario ingrese un valor válido.
'''

for contador in range(1, 16):
    calificacion = float(input(f'Ingresa la calificacion del usuario {contador}: '))
    #print(contador)

    while((calificacion < 0) or (calificacion > 5)):
        calificacion = float(input(f'calificacion no valida, ingresa la calificacion del usuario {contador}: '))

print('Verificacion completa. Todas las calificaciones son validas.')