def sumaFilaPar(matriz):
    suma = 0
    for fila in range(len(matriz)):
        for i in matriz[fila]:
            if fila % 2 == 0:
                suma = i + suma
    return suma

matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
resultado = sumaFilaPar(matriz)
print(resultado)