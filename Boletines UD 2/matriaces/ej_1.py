def getElemento(matriz, num_fila, num_col):
    elemento =  matriz [num_fila][num_col]
    return elemento

matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(getElemento(matriz,1,1))

def getFila(matriz, num_fila):
    fila = matriz[num_fila]
    return fila

def getColumna(matriz, num_col):
    columna = []
    for i in range(0,len(matriz)):
        columna.append(matriz[i][num_col])
    return columna

matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(getColumna(matriz, 0))