'''
En una matriz, podemos encontrar dos diagonales: la que comienza por el elemento 0,0 y la que comienza por el elemento 0, 
numFila-1. Se trata de que crees dos funciones:
#devuelveDiagonalPrincipal que te devolverá la lista de los elementos que están en esa diagonal que comienza por 0,0
#devuelveDiagonalSecundaria que te devolverá la lista de los elementos que están en la otra diagonal
'''
matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
def DiagonalPrincipal(matriz):
    columna=0
    fila=0
    principaldiagonal=[]
    for fila     in matriz:
        elemento= matriz[fila][columna] 
        principaldiagonal.append(elemento)
        columna= columna+1
        fila= fila+1
    return principaldiagonal
print (DiagonalPrincipal(matriz))

'''
devuelveDiagonalSecundaria que te devolverá la lista 
de los elementos que están en la otra diagonal
'''
def diagonal_secundaria(matriz):
    diagonal = []
    columna = len(matriz) - 1 
    for fila in range(0,len(matriz)-1,1):
        elemento = matriz[fila][columna]
        diagonal.append(elemento)
        columna = columna - 1 
    return diagonal

matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
print(diagonal_secundaria(matriz))