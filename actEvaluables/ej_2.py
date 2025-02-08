#Realiza el mismo ejercicio pero calculando la suma por filas

def suma_por_filas(matriz):
    suma_total = 0

    for i in range(len(matriz)):
        suma_fila = 0
        for elemento in matriz[i]:
            suma_fila += elemento
        print('Suma de fila',i,':',suma_fila)
        suma_total += suma_fila
    return suma_total

matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
suma_total = suma_por_filas(matriz)
print('La suma total de las filas es:',suma_total)
