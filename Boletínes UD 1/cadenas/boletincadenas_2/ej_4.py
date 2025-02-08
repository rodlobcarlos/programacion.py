'''
Realizar un programa que comprueba si una cadena leída por 
teclado comienza por una subcadena introducida por teclado.
'''
'''
cadena = input('Dame una cadena de texto: ')
comienza_sub = cadena[0:len(cadena)]

intr_sub = input('Introduce una subcadena: ')
if intr_sub == comienza_sub:
    print('Correcto.')
else:
    print('Esa no es la subcadena inicial.')

'''

cadena = input('Dame una cadena de texto: ')
subcadena = input('Introduce una subcadena: ')

if len(cadena) > len(subcadena):
    print('Error.')
elif len(subcadena) <= len(cadena):
    if cadena[len(cadena) - len(subcadena) : len(cadena)] == subcadena:
        print('La cadena termina por:',subcadena)
else: 
    print('La cadena no termina así.')