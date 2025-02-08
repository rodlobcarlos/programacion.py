mes =int(input('Dame un mes: '))
dia = int(input('Dime un día: '))
match mes: 
    case 1|2|3:
        if mes == 3 and dia <=20:
            print('Invierno')
        elif mes == 3 and dia >=20:
            print('Primavera.')
    case 4|5|6:
        if mes == 6 and dia <= 20:
            print('Primavera.')
        elif mes == 6 and dia >= 20:
            print('Verano.')
    case 7|8|9:
        if mes == 9 and dia <= 20:
            print('Verano.')
        elif mes == 9 and dia >= 20:
            print('Otoño.')
    case 10|11|12:
        if mes == 12 and dia <= 20:
            print('Otoño.')
        elif mes == 12 and dia >= 20:
            print('Invierno.')