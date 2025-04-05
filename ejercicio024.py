#Crea un código que solicite una frase al usuario y 
# luego imprima la misma frase sin espacios en blanco al principio y al final, 
# además de convertirla a minúsculas.

frase = input('Escriba una frase con espacios en blanco al principio y al final: ')

print(frase)
print(frase.strip().lower())