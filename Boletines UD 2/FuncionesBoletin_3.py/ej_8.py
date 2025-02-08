'''
Crea un programa que genere 100 números de forma aleatoria (del 0 al 1000)  y que posteriormente ofrezca al usuario la posibilidad de:
#Conocer el mayor
#Conocer el menor
#Obtener la suma de todos los números
#Obtener la media
#Sustituir el valor de un elemento por otro número introducido por teclado
#Mostrar todos los números
    Utiliza funciones de manera que tu programa sea lo más modular posible. 
'''
import random

def menu():
    print('=============MENU===============')
    print('============ a)Conocer el mayor ============')
    print('============ b)Conocer el menor ============')
    print('============ c)Obtener la suma de todos los números ============')
    print('============ d)Obtener la media ============')
    print('============ e)Sustituir el valor de un elemento por otro número introducido por teclado ============')
    print('============ d)Mostrar todos los números ============')
    print('=====================================================================================================')
    eleccion = input('¿Qué opción quieres elegir?: ')
    return eleccion

        
def mayor():
    listaNum = []
    for i in range(0,100):
        numeros = random.randint(0,1000)
        listaNum.append(numeros)
    print(listaNum)
    mayor = listaNum[0]
    for i in listaNum:
        if i > mayor:
            mayor = i
    return mayor

salida = True
while salida:
    opcion = menu()
    if opcion == 'a':
        print('El mayor es:', mayor())
    else:
        salida = False

def menor():
    listaNum = []
    for i in range(0,100):
        numeros = random.randint(0,1000)
        listaNum.append(numeros)
    print(listaNum)
    menor = listaNum[0]
    for i in listaNum:
        if i < menor:
            menor = i
    return menor

salida = True
while salida:
    opcion = menu()
    if opcion == 'b':
        print('El menor es:', menor())
    elif opcion == 'a':
        print('El mayor es:', mayor())
    else:
        salida = False

def suma_total():
    listaNum = []
    for i in range(0,100):
        numeros = random.randint(0,1000)
        listaNum.append(numeros)
    print(listaNum)
    suma = 0
    for i in listaNum:
        suma = i + suma
    return suma

salida = True
while salida:
    opcion = menu()
    if opcion == 'c':
        print('La suma total es:', suma_total())
    elif opcion == 'a':
        print('El mayor es:', mayor())
    elif opcion == 'b':
        print('El menor es:', menor())
    else:
        salida = False

def media():
    lista_num = [] 
    for _ in range(100):  
        numero = random.randint(0, 1000)  
        lista_num.append(numero) 
    print(lista_num)  
    suma = 0  
    for i in lista_num: 
        suma += i 
    media = suma / len(lista_num)
    print('La media es:',media)
    return media  

salida = True
while salida:
    opcion = media()
    if opcion == 'd':
        print('La media es:', media()) 
    elif opcion == 'a':
        print('El mayor es:', mayor())
    elif opcion == 'b':
        print('El menor es:', menor())    
    elif opcion == 'c':
        print('La suma total es:', suma_total())
    else:
        salida = False

def sustituir():
    lista_num = [] 
    for _ in range(100):  
        numero = random.randint(0, 1000)  
        lista_num.append(numero) 
    print(lista_num)  
    lista_num.insert(5, '2')
    return lista_num

salida = True
while salida:
    opcion = media()
    if opcion == 'e':
        print('El valor sustituido es:', sustituir())
    elif opcion == 'd':
        print('La media es:', media()) 
    elif opcion == 'a':
        print('El mayor es:', mayor())
    elif opcion == 'b':
        print('El menor es:', menor())    
    elif opcion == 'c':
        print('La suma total es:', suma_total())
    else:
        salida = False