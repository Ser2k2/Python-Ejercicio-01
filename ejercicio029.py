'''
Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e 
informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).
'''

crecimiento = float(input('Ingrese el porcentaje de crecimiento de producción(%): '))

if (crecimiento > 0):
    print(f'Hubo un incremento de {crecimiento}%.')
elif (crecimiento < 0):
    print(f'Hubo un decresimiento de {crecimiento}%.')
else:
    print(f'Hubo un crecimiento nulo {crecimiento}%.')