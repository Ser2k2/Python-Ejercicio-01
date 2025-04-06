'''
Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
'''

letra = input('Ingrese una letra: ')
vocales = 'aeiou'
consonantes = 'bcdfgjklmnñpqrstvwxyz'

if (letra.lower() in vocales):
    print(f'La letra es una vocal: {letra}.')
elif (letra.lower() in consonantes):
    print(f'La letra es una consonante: {letra}.')
else:
    print(f'Lo ingresado no es una consonante ó vocal: {letra}.')
