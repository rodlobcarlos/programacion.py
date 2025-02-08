dia = input('Dime un día de la semana: ')

dia = dia.upper()

match dia: 
    case 'LUNES':
        print('====================')
        print('-------LUNES--------')
        print('====================')
        print('8-9 Prog')
        print('9-10 Bdd')
        print('====================')
    case'MARTES': 
        print('10-11 Ldm')
        print('11-12 Si')
    case'MIÉRCOLES': 
        print('10-11 Ent')
        print('11-12 Si')
    case'JUEVES': 
        print('10-11 Si')
        print('11-12 Si')
    case'VIERNES': 
        print('10-11 Prog')
        print('11-12 Si') 
    case 'SABADO': 
        print('Día de descanso.')
    case 'DOMINGO':
        print('Día de descanso.')
    case _: 
        print('Incorrecto.')