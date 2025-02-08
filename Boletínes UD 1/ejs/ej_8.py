# Realizar un programa que lea un número por teclado.
# El programa debe imprimir en pantalla un mensaje 
# con “El número xx es múltiplo de 2” o un mensaje 
# con “El número xx es múltiplo de 3”. 
# Si es múltiplo de 2 y de 3 deben aparecer los dos 
# mensajes. Si no es múltiplo de ninguno de los dos 
# el programa finaliza sin mostrar ningún mensaje.


numero = int(input('Introduce un número: '))

multiplo_1 = 2
multiplo_2 = 3

if numero % multiplo_1 == 0:
    print(f'El número {numero} es múltiplo de {multiplo_1}.')
else:
    print(f'El número {numero} es mútiplo de {multiplo_1} y de {multiplo_2}.')

if numero % multiplo_2 == 0:
    print(f'El número {numero} es múltiplo de {multiplo_2}.')
else:
    print(f'El número {numero} es mútiplo de {multiplo_1} y de {multiplo_2}.')