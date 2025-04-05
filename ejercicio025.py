#Crea un código que solicite una frase al usuario y 
# luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".

frase = input('Escribe una frase que contenga la mayoria de palabras la letra "e": ')

print(frase)
print(frase.lower().replace('e', 'f'))