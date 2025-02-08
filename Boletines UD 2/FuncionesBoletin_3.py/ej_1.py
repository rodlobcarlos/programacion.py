'''
Escribir un programa que solicite al usuario cuántos números desea introducir. 
A continuación, se introducirá por teclado esa cantidad de números enteros, y por último, 
los mostrará en el orden inverso al introducido. Diseña una solución que haga uso de funciones. 
'''
lista = []
numero = int(input('Dime cuantos números quieres: '))

for numero in range(1,1,numero):
    numero_1 = int(input('Dime un número: '))
    lista.append(numero_1)
    print(lista)