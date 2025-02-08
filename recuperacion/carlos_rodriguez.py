#Para el primer método imprime el menú y retorno la elección que elijamos.
#Para el segundo método, para la opción 'r' del primer método nos pedirá los datos de los equipos, dependiendo de la fase que elijamos
#Para el tercer método, dependiendo de la fase que elijamos nos dará los datos de esa fase

def menu():
    print('=== MENU ==============')
    print('=== R) Registrar puntuaciones de equipo =======')
    print('=== L) Listar equipos y su puntuación por fase =====')
    print('=== C) Clasificados por fases ================')
    print('=== S) Salir =================')
    eleccion = input('¿Qué opcción quieres elegir?: ').upper()

    while eleccion != 'R' and eleccion != 'L' and eleccion != 'C' and eleccion != 'S':
        print('Opción incorrecta.')
        menu()
    if eleccion == 'S':
        print('Salir.')
    else:
        print('Has seleccionado la opción',eleccion)
    return eleccion

def registroPuntuaciones():
    eleccion = menu()
    if eleccion == 'R':
        fase = input('¿Qué fase quieres?: ').lower()
        while fase != 'inicial' and fase != 'semifinal' and fase != 'final':
            print('Error debe ser inicial, semifinal o final.')
            fase = input('¿Qué fase quieres?: ')
        else: 
            if fase == 'inicial':               
                num_equipos = 8
            elif fase == 'semifinal':
                num_equipos = 4
            elif fase == 'final':
                num_equipos = 2

            for fase in range(num_equipos):
                entrada = input('Escribe el nombre y la puntuación con este formato: (nombreEquipo:puntuacion); ')
                print(entrada)
            print('==================================')
            print('Datos registrados correctamente')
            print('==================================')

registroPuntuaciones()

def listarPuntuacionesEquipo():
    eleccion = menu()
    if eleccion == 'L':
        fase = input('¿Qué fase quieres?: ').lower()
        while fase != 'inicial' and fase != 'semifinal' and fase != 'final':
           print('Error debe ser inicial, semifinal o final.')
           fase = input('¿Qué fase quieres?: ')
        else:
            if fase == 'inicial':
                puntuaciones = entrada
            elif fase == 'semifinal': 
                puntuaciones == entrada
            elif fase == 'final':
                puntuaciones = entrada

listarPuntuacionesEquipo()