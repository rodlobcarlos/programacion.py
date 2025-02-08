'''
Diseña y construye una función para cada uno de los siguientes  casos:
a) A partir de un número de fila, te devuelve el número máximo para esa fila.
b) A partir de un número de columna,te devuelve el número máximo para esa columna.
c) Diseña y construye una función que utilizando una de las funciones anteriores, calcula el máximo total en la matriz
'''

#A)
def filas(matriz, num_fila):
    fila = matriz[num_fila]
    for posicion in fila:
        mayor = fila[0]
    for posicion in fila:
        if posicion > mayor:
            mayor = posicion
        solucion = ('El mayor es:',mayor)
    return fila, solucion 

num_fila = 2
matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(filas(matriz, num_fila))

#B)
def columnas(matriz, num_columna):
    columna = matriz[num_columna]  
    for fila in (matriz):
        mayor = columna[0]
        for posicion in range(len(fila)):
            if posicion > mayor:
                print(fila[posicion])
                mayor = fila[posicion]
            solucion = ('El mayor es:',mayor)
        return columna ,solucion

num_columna = 2
matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(columnas(matriz, num_columna))

#C)
'''def mayor_matriz(matriz, num_fila):
    fila = matriz[num_fila]
    for i in fila:
        mayor = len(matriz)
    for i in fila:
        if i > mayor:
            mayor = i
        solucion = ('El mayor es:',mayor)
    return solucion


matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(filas(matriz, num_fila))'''