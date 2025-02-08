'''
Suma columna. Diseña y construye  una función que te sume 
los elementos de una columna que se recibe por parámetros.
'''
def suma_columna(matriz, num_col):
    suma = 0
    for i in matriz[num_col]:
        print(i)
        suma = i + suma    
    return suma, num_col

matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(suma_columna(matriz,0))  