'''
Queremos guardar la cantidad de coches que se arreglan en el taller durante 10 semanas.
Para ello usaremos una matriz de 7 columnas para cada día de la semana y 10 filas, una fila
por semana.
#Crea una función que imprima los coches arreglados en una semana
#Por último, imprime cuántos coches se han arreglado en total
'''
def coches_arreglados(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma_fila = 0
        for elemento in matriz[i]:
            suma_fila += elemento
        print('Coche arreglados en la semana',i,':',suma_fila)
        suma += suma_fila
        suma_total = ('Coches arreglados en total:',suma)
    return suma_total

matriz = [[12, 23, 34, 45, 10, 34, 23], 
          [35, 23, 3, 8, 10, 45, 34], 
          [56, 23, 60, 45, 100, 34, 37],
          [54, 23, 34, 45, 10, 34, 67], 
          [12, 76, 34, 265, 123, 35, 69], 
          [32, 34, 26, 12, 34, 150, 91], 
          [4, 68, 87, 45, 98, 94, 83], 
          [12, 300, 100, 233, 31, 76, 23], 
          [12, 47, 254, 234, 55, 44, 77], 
          [11, 22, 98, 79, 68, 69, 15]]
print(coches_arreglados(matriz))