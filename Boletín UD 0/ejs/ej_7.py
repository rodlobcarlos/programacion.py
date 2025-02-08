número_1 = int(input('Introduce un número: '))
número_2 = int(input('Introduce otro número: '))

positivo = 0

if número_1 >= 0:
    positivo += 1
if número_2 >= 0:
    positivo += 1 

print(f'Hay {positivo} números positivos.')