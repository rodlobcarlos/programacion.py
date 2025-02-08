#Realizar un programa que solicite un carácter por teclado e informe por pantalla si el carácter es una vocal o no lo es
#Si es una vocal mostrará el mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.


letra = input('Dime una letra: ')

vocal = ('a, e, i, o, u')

if letra == 'a':
    print('Es la primera vocal.')
elif letra == 'e':
    print('Es la segunda vocal.')
elif letra == 'i':
    print('Es la tercera vocal.')
elif letra == 'o':
    print('Es la cuarta vocal.')
elif letra == 'u':
    print('Es la quinta vocal..')
else:
    print('No es vocal.')