clave = int(input('Dame una contraseña: '))
match clave: 
    case 1234 | 4321:
        print('Has acertado!')
    case _: 
        print('No has adivinado.')