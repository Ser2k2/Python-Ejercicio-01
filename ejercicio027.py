#Crea un código que solicite una frase al usuario y 
# luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".

frase = input('Escribe una frase que contenga la mayoria de palabras la letra "s": ')

print(frase)
print(frase.lower().replace('s', '$'))