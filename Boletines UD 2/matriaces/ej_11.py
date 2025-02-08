'''
Construye una función que te devuelve 
la suma de los elementos de una diagonal, 
según indique el argumento de entrada 
esPrincipal  verdadero → principal,  
falso → secundaria.
'''
import ej_10

matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

ej_10.DiagonalPrincipal(matriz)

def suma_elemento(matriz, principal):
    suma = 0