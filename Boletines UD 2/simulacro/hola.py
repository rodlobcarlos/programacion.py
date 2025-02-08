import random

def print_menu():
    print('======================== MENU ===================================')
    print('========== 1. Asignar coche a surtidor y repostar ===============')
    print('========== 2. Consultar estado de surtidor ======================')
    print('========== 3. Asignar precio al surtidor ========================')
    print('========== 4. Recargar surtidor =================================')
    print('========== 5. Cerrar el programa y salir ========================')
    print('=================================================================')

# Inicializamos surtidores y precios
surtidores = [random.randint(100, 5000) for _ in range(4)]
precios = {'gasolina': 1.5, 'diesel': 1.2}

def pedir_matricula():
    numeros = input('Dame los números de la matrícula (4 dígitos): ')
    letras = input('Dame las letras de la matrícula (3 letras): ')
    return numeros + letras.upper()

def opcion_1():
    matricula = pedir_matricula()
    print(f"Matrícula {matricula} registrada.")

    surtidor = int(input('Elige un surtidor (1-4): ')) - 1
    combustible = input('Elige un combustible (gasolina/diesel): ').lower()
    dinero = float(input('¿Cuánto dinero quieres gastar?: '))

    if 0 <= surtidor < len(surtidores) and combustible in precios:
        litros = dinero / precios[combustible]
        if surtidores[surtidor] >= litros:
            surtidores[surtidor] -= litros
            print(f"Repostando {litros:.2f} litros de {combustible} en el surtidor {surtidor + 1}.")
        else:
            print(f"No hay suficiente combustible en el surtidor {surtidor + 1}.")
    else:
        print("Surtidor o combustible inválido.")

def opcion_2():
    for i, cantidad in enumerate(surtidores):
        print(f"Surtidor {i + 1}: {cantidad:.2f} litros disponibles.")

def opcion_3():
    combustible = input('Elige un combustible (gasolina/diesel): ').lower()
    nuevo_precio = float(input(f'Introduce el nuevo precio para {combustible}: '))
    if combustible in precios:
        precios[combustible] = nuevo_precio
        print(f"Nuevo precio de {combustible}: {nuevo_precio:.2f} €/litro.")
    else:
        print("Combustible inválido.")

def opcion_4():
    surtidor = int(input('Elige un surtidor (1-4): ')) - 1
    cantidad = float(input('¿Cuántos litros deseas agregar?: '))
    if 0 <= surtidor < len(surtidores):
        surtidores[surtidor] += cantidad
        print(f"Surtidor {surtidor + 1} recargado con {cantidad:.2f} litros.")
    else:
        print("Surtidor inválido.")

# Control principal
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
