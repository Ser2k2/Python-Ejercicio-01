'''
Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", 
"tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", 
"¡Buenas Noches!" o "Valor Inválido!", según el caso.
'''

turno_estudio = input('Ingresa que turno estudias (mañana, tarde o noches): ')

if (turno_estudio.lower() == 'mañana' ):
    print('¡Buenos Días!')
elif (turno_estudio.lower() == 'tarde'):
    print('¡Buenas Tardes')
elif (turno_estudio.lower() == 'noche'):
    print('¡Buenas Noches')
else:
    print('¡Valor Inválido')