# Crea un código que solicite una frase al usuario y 
# luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".

frase = input('Escribe una frase que contenga la mayoria de palabras la letra "a": ')

print(frase)
print(frase.lower().replace('a', '@'))