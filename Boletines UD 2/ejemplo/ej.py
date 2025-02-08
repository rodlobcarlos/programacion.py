cadena = input('Dame un cadena: ')
num = int(input('Dame un número: '))

long = len(cadena)
while long < 4:
    cadena = input('Dame un cadena: ')

if num % 2 == 0:
    cadena = (cadena[2] + cadena[4]) * len(cadena)
    print(cadena)
elif num % 3 == 0:
    cadena = (cadena[1] + cadena[2]) * len(cadena)
    print(cadena)