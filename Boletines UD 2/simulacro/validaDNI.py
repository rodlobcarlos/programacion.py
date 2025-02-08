list_letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X' , 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

def validar_dni_español():
    dni = int(input('Dame un dni: '))
    letra = input('Dame una letra: ')
    if dni > 7 or dni <= 8:
        print('El DNI es valido:',dni,letra)
        digito_control = dni % 23
        if digito_control > 0 and digito_control < 23:
            digito_control = list_letras[digito_control]
            print('El digito control es:',digito_control)
    else:
        print('El DNI no es valido.')
    return digito_control

print(validar_dni_español())

list_letra = ['X', 'Y', 'Z']
def extranjeros_en_españa():
    dni = int(input('Dame un DNI: '))
    letra = input('Dame una letra: ')
    if dni == 7:
        print('El DNI es valido:',dni,letra)
        digito_control = dni % 3
    if digito_control > 0 and digito_control < 3:
        digito_control = list_letra[digito_control]
        print('El digito control es:',digito_control)
    else:
        print('El DNI no es valido.')
    return digito_control

print(extranjeros_en_españa())