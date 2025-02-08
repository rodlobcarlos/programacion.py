'''
Crea un programa que te pida por teclado tu nombre y tus dos apellidos y los guarde en una lista. 
A continuación, crea una función que reciba esta lista e imprima cuántas letras “a” contiene. 
Modifica el programa anterior para que lo devuelva en un return y sea en el bloque principal donde se imprima.
'''
def letraA(lista ,letra = 'a'):
    contador = 0
    for palabra in lista:
        for caracter in palabra: 
            if caracter == 'a':
                contador += 1
    return contador
    
nombre = input('Dame tu nombre: ')
apellido_1 = input('Dame tu apellido: ')
apellido_2 = input('Dame otro apellido: ')
lista = [nombre, apellido_1, apellido_2]
print(lista)
caracter_total = letraA(lista)
print('Hay', caracter_total, 'a')