'''
Modifica el programa anterior para añadir una función que pase a horas, 
otra que pase a minutos y otra a segundos. 
Escribe un programa principal con un menú donde se pueda elegir la opción de 
convertir a segundos, convertir a minutos y  horas  o salir del programa.
'''
def convertirHoras(segundos):
    horas = int(segundos / 3600)  
    minutos = int((segundos % 3600) / 60)  
    return horas

def convertirMinutos(segundos):
    minutos = int(segundos / 60) 
    return minutos

salida = 0
while salida == 0:

    segundos = int(input('Dame los segundos que quieras: '))
    menu = input('Introduce una opción:')
    match menu:
        case ('A'):
            resultado = convertirHoras(segundos)
            print(resultado, 'horas')
        case ('B'):
            resultado = convertirMinutos(segundos)
            print(resultado, 'minutos')
        case ('C'):
            print(segundos, 'segundos')
        case('-1'):
            print('Saliste.')
            salida = 1