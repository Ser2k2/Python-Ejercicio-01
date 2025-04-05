#Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.

notaA = float(input('Ingrese la primera nota: '))
notaB = float(input('Ingrese la segunda nota: '))
notaC = float(input('Ingrese la tercera nota: '))

print(f'El promedio de las notas {notaA} + {notaB} + {notaC} es {(notaA + notaB + notaC) / 3}.')