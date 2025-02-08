print('========================')
print('       Calculadora      ')
print('========================')
signo= input(
    'Introduzca + se desea sumar.\n'
    'Introduzca - se desea restar.\n'
    'Introduzca * se desea multi.\n'
    'Introduzca / se desea div.\n'
    'Introduzca @ para salir del menú.\n'
    'Introducir valor: '
)
finaliza = signo != '@'
while finaliza:
    match signo:
        case '+':
            num = int(input('Dame un número: '))
            num_1 = int(input('Dame otro número: '))
            resultado = num + num_1
            print(f'{num} + {num_1} = {resultado}')
        case '-':
            num = int(input('Dame un número: '))
            num_1 = int(input('Dame otro número: '))
            resultado = num - num_1 
            print(f'{num} - {num_1} = {resultado}')
        case '*':
            num = int(input('Dame un número: '))
            num_1 = int(input('Dame otro número: '))
            resultado = num * num_1
            print(f'{num} * {num_1} = {resultado}')
        case '/':
            num = int(input('Dame un número: '))
            num_1 = int(input('Dame otro número: '))
            if num_1 !=0:
                resultado = num / num_1
                print(f'{num} / {num_1} = {resultado}')
            else:
                print('No se puede dividir entre 0.')    
        case '@':
                print('Adiós!')
                break
    signo = input(
        'Introduzca + se desea sumar.\n'
        'Introduzca - se desea restar.\n'
        'Introduzca * se desea multi.\n'
        'Introduzca / se desea div.\n'
        'Introduzca @ para salir del menú.\n'
        'Introducir valor: '
    )