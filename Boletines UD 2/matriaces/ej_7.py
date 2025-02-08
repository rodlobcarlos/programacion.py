'''
Diseña y construye  una función que recorra una matriz y  
la suma de los elementos que están en una columna par. 
Considera el 0 como par.
'''
def suma_columna_par(matriz):
    suma = 0
    for fila in (matriz):
        for posicion in range(len(fila)):
            if posicion % 2 == 0:
                print(fila[posicion])
                suma = fila[posicion] + suma
                solucion = 'La suma total es:',suma
    return solucion

matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
print(suma_columna_par(matriz))