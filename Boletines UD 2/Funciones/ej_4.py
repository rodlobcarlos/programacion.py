'''
Crea una función "calcularMax" que recibe una lista con valores numéricos 
y devuelve el valor máximo. Crea un programa que pida 10 números por teclado, 
los guarde en una lista y muestre el máximo, utilizando la función anterior.
'''

def calcularMax(lista):
    return max(lista)

numeros = []
for i in range(10):
    numero = float(input("Ingrese el número " + str(i+1) + ": "))
    numeros.append(numero)

maximo = calcularMax(numeros)
print("El número máximo es:", maximo)
