'''
Diseñar el juego "Acierta la contraseña". El primer jugador introduce una
contraseña, el segundo, debe insertar otra intentando acertarla con las pistas
que le dará el programa: número de caracteres, primera y última letra. El
programa debe escribir "Acertaste" o "Fallaste".
'''
print('========= Acierta la contraseña ==========')

contraseña = ''
cont_1 = input('Introduce una contraseña: ')
contr_2 = input('Introduce una contraseña: ')

import random
caracteres = ''
pri_letra = ''
ult_letra = ''
pista = random.randint(caracteres, pri_letra, ult_letra)
print(pista) 
