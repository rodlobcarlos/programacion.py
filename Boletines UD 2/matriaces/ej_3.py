def getParesImpares(matriz):
    pares = []
    for fila in matriz:
        for num in fila:
            if num % 2 == 0:
                pares.append(num)   
    return pares

matriz = [8, 1, 6],[3, 5, 7],[4, 9, 2]
print(getParesImpares((matriz)))