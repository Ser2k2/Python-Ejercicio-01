#Crea un programa que solicite dos valores numéricos, un numerador y un denominador, 
# y devuelva el resto de la división entre los dos valores. 
# Asegúrate de que el valor del denominador no sea igual a 0.

dividendo = int(input('Escriba el primer número: '))
divisor = int(input('Escriba el segundo número (no debe ser cero): '))

print(f'El residuo de la división de {dividendo} / {divisor} es {dividendo % divisor}.')