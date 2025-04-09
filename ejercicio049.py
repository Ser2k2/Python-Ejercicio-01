'''
En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. 
Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:

Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).

También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).

Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, 
los votos nulos y los votos en blanco. Además, debe calcular y 
mostrar el porcentaje de votos nulos con respecto al total de votos y 
el porcentaje de votos en blanco con respecto al total de votos.
'''
voto_candidato_1 = 0
voto_candidato_2 = 0
voto_candidato_3 = 0
voto_candidato_4 = 0
voto_nulo = 0
voto_blanco = 0

for contador in range(0, 20):
    voto = int(input(f'Ingrese su voto {contador + 1}: '))
    if (voto == 1):
        voto_candidato_1 += 1
    elif (voto == 2):
        voto_candidato_2 += 1
    elif (voto == 3):
        voto_candidato_3 += 1
    elif (voto == 4):
        voto_candidato_4 += 1
    elif (voto == 5):
        voto_nulo += 1
    elif (voto == 6):
        voto_blanco += 1
    else:
        print('Voto invalido!')

print('Cantidad de Votos:')
print(f'Votos candidato 1: {voto_candidato_1}')
print(f'Votos candidato 2: {voto_candidato_2}')
print(f'Votos candidato 3: {voto_candidato_3}')
print(f'Votos candidato 4: {voto_candidato_4}')
print(f'Votos nulos: {voto_nulo}')
print(f'Votos en blanco: {voto_blanco}')
print(f'Porcentaje de votos nulos: {(voto_nulo / 20 * 100)}')
print(f'Porcentaje de votos  en blanco: {(voto_blanco / 20 * 100)}')




