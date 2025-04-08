'''
 Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o 
 iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, respectivamente. 
 Supón que la colonia A comienza con 4 elementos y B con 10.
'''

colonia_A = 4
colonia_B = 10

tCrecimiento_A = 0.03
tCrecimiento_B = 0.015

dias  = 0

while (colonia_A <= colonia_B):
    #print(colonia_A, colonia_B)
    colonia_A *= 1 + tCrecimiento_A #colonia_A = colonia_A * (1 + tCrecimiento_A)
    colonia_B *= 1 + tCrecimiento_B

    dias += 1

print(f'Necesitará {dias} días para que la colonia A supere a la colonia B.')   
