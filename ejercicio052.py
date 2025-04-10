'''
Crea un programa que, al ingresar un número cualquiera, 
genere una lista que contenga todos los números primos entre 1 y el número ingresado.
'''

# Recopilamos el número
numero = int(input('Ingresa un número entero: '))
# Lista para almacenar los números primos
lista_primos = []
# Bucle que recorre todos los números por debajo del número ingresado
for num in range(2, numero):
  # Primo es una bandera que nos permite saber si el valor analizado es primo o no.
  primo = True
  # Probamos si todos los números por debajo del especificado en el primer bucle pueden dar una división exacta.
  for prueba_divisibles in range(2, num):
    if num % prueba_divisibles == 0:
      # Si es divisible por algún número, entendemos que el número no es primo y terminamos el bucle interno con break.
      primo = False
      break
  # La condición se convierte en el resultado booleano de primo: False. Ignoramos la condición True y ejecutamos el bloque del if.
  if primo:
    lista_primos.append(num)
# Resultado
print(f'Lista de números primos: {lista_primos}')

