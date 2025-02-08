'''
Crea una función que calcule la suma  total, además imprima la suma de los elementos en cada columna. 
El programa debe recorrer la matriz columna por columna, calcular la suma por columna, 
mostrar el resultado para cada columna y actualizar y devolver su suma total. 
Por ejemplo, para la matriz:  Imprimirá:
matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
Suma de columna 0: 12
Suma de columna 1: 15
Suma de columna 2: 18
Fuera de la función: SumaTotal = 45
'''

def sumaColumnas(matriz):
    suma_total = 0 
    num_columnas = len(matriz[0])
    for col in range(num_columnas):
        suma_columna = 0  
        for fila in matriz:
            suma_columna += fila[col]
        print('Suma de columna',col,':',suma_columna)
        suma_total += suma_columna
    return suma_total

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
suma_total = sumaColumnas(matriz)
print('lA Suma Total:',suma_total)