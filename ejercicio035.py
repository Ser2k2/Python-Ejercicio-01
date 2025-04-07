'''
Escribe un programa que solicite un número entero a la persona usuaria y 
determine si es par o impar. Pista: Puedes usar el operador módulo (%)
'''

numero = int(input('Ingrese un número entero: '))

#Si el residuo es '0' el número es par, pero si el residuo es '1' el número es impar.
residuo = numero % 2 

if (residuo == 0):
    print('El número es par!')
    #print(residuo)
else:
    print('El número es impar!')
    #print(residuo)
