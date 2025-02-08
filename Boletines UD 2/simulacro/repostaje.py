import random

surtidor_1 = random.randint(100, 5000)
surtidor_2 = random.randint(100, 5000)
surtidor_3 = random.randint(100, 5000)
surtidor_4 = random.randint(100, 5000)

def print_menu():
    print('======================== MENU ===================================')
    print('========== 1. Asignar coche a surtidor y repostar ===============')
    print('========== 2. Consultar estado de surtidor ======================')
    print('========== 3. Asignar precio al surtidor ========================')
    print('========== 4. Recargar surtidor =================================')
    print('========== 5. Cerrar el programa y salir ========================')
    print('=================================================================')
    return print_menu

print_menu()

opcion = input('Elige una opción: ')

def matricula():
    num = input('Dame los números de la matícula: ')
    if len(num) == 4:
        print(num) 
    else:
        print('Tiene que ser 4 números.')
        num = input('Dame los números de la matícula: ')
    letra = input('Dame las letras de la matrícula: ')
    if len(letra) == 3:
        print(letra)
    else:
        print('La matrícula debe tener 3 letras.')
        letra = input('Dame las letras de la matrícula: ')

    return 

matricula()

combustible = 'gasolina' or 'diesel'

def opcion_1():
    cantidad = int(input('Cuanto quieres hechar: '))
    combustible = input('Elige un combustible: ')
    surtidor = input('Elige un surtidor: ')
    dinero = int(input('¿Cuanto dinero quieres gastar?: '))
    litros = cantidad / dinero
    if combustible == 'gasolina' and surtidor == '1':
        print('Repostando',litros,'litros de',combustible,'en el sustidor', surtidor) 
    elif combustible == 'gasolina' and surtidor == '2':
        print('Repostando',litros,'litros de',combustible,'en el sustidor', surtidor)
    elif combustible == 'diesel' and surtidor == '3':
        print('Repostando',litros,'litros de',combustible,'en el sustidor', surtidor) 
    elif combustible == 'diesel' and surtidor == '4':
        print('Repostando',litros,'litros de',combustible,'en el sustidor', surtidor)     

    return cantidad, combustible, surtidor, litros

opcion_1()

lista_surtidor = [surtidor_1, surtidor_2, surtidor_3, surtidor_4]
i = 0
def opcion_2():
    for cantidad in lista_surtidor:
        print('Surtidor:',(i + 1)),':', 'cantidad:',  

while True:
    print_menu()
    opcion = input('Elige una opción: ')
    
    if opcion == '1':
        opcion_1()
    elif opcion == '2':
        opcion_2()
    elif opcion == '3':
        opcion_3()
    elif opcion == '4':
        opcion_4()
    elif opcion == '5':
        print("Saliendo del programa. ¡Adiós!")
        break
    else:
        print('Opción no válida.')