'''
Al código del ejercicio anterior añádele 
una comprobación para que te devuelva la 
diagonal sólo si la matriz es cuadrada, 
es decir si el número de filas es igual 
que el número de columnas. (NxN). 
Si la matriz no es cuadrada, devolverá una lista vacía.
'''
matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
def DiagonalPrincipal(matriz):
        columna=0
        fila=0
        principaldiagonal=[]
        for filas in matriz:
            elemento=(matriz[fila][columna])
            principaldiagonal.append(elemento)
            columna= columna+1
            fila= fila+1
            if fila == columna:
                return principaldiagonal

print(DiagonalPrincipal(matriz))



def esCuadrada(matriz):
    cadrada = True
    fila = len(matriz)
    columna = len(matriz[0])
    if fila == columna:
        cadrada = True
    else:
        cuadrada = False
    return cadrada

matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
print(esCuadrada(matriz))