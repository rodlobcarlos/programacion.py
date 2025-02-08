'''
Dada una matriz de números enteros, escribe una función  que cuente cuántos 
números son pares y cuántos son impares. Recorre la matriz para contar. 
Invoca a esta función e imprime el resultado total al final.
'''
def paresImpares(matriz):
    par = 0  
    impar = 0  
    for fila in matriz:
        for numero in fila:
            if numero % 2 == 0:
                par += 1  
            else:
                impar += 1  
    print('Total pares:' ,par)
    print('Total impares:' ,impar)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]
paresImpares(matriz)
