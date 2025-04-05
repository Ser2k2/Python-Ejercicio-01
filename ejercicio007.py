#Crea un programa que solicite al usuario que escriba su nombre, 
# edad y altura en metros, y luego imprima "Hola, [nombre], tienes [edad] años y 
# mides [altura] metros."

nombre = input('Escriba su nombre: ')
edad = input('Escriba su edad: ')
altura = input('Escriba su altura (metros): ')

print('Hola, {}, tienes {} años y mides {} metros'.format(nombre, edad, altura))