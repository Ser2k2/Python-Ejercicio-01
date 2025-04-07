'''
Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. 
El programa debe informar si los valores pueden utilizarse para formar un triángulo y, 
en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:

Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
Triángulo Equilátero: tres lados iguales;
Triángulo Isósceles: dos lados iguales;
Triángulo Escaleno: tres lados diferentes.
'''

lado_a = int(input('Ingrese la longitud del primer lado (A): '))
lado_b = int(input('Ingrese la longitud del primer lado (B): '))
lado_c = int(input('Ingrese la longitud del primer lado (C): '))

if (lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a):
    print(f'Los lados A ({lado_a}), B ({lado_b}) y C ({lado_c}) forman un triangulo. ')

    if (lado_a == lado_b and lado_b == lado_c):
          print(f'Los lados A ({lado_a}), B ({lado_b}) y C ({lado_c}) forman un triangulo Equilatero. ')
    elif (lado_a != lado_b and lado_a != lado_c and lado_b != lado_c):
          print(f'Los lados A ({lado_a}), B ({lado_b}) y C ({lado_c}) forman un triangulo Escaleno. ')
    else:
          print(f'Los lados A ({lado_a}), B ({lado_b}) y C ({lado_c}) forman un triangulo Isósceles. ')
else:
        print(f'Los lados A ({lado_a}), B ({lado_b}) y C ({lado_c}) no forman un triangulo. ')
