'''
Crea una función "calcularMaxMin" que recibe una lista con valores numéricos 
y devuelve el valor máximo y el mínimo. Crea un programa que pida 10 números por teclado, 
los guarde en una lista y muestre el máximo y el mínimo, utilizando la función anterior.

'''
def calcularMaxMin(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = []
for i in range(10):
    numero = float(input('Dame el número ' + str(i+1) + ": "))
    numeros.append(numero)

maximo, minimo = calcularMaxMin(numeros)
print('El número máximo es:', maximo)
print('El número mínimo es:', minimo)