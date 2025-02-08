'''
Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia 
y muestre su área y perímetro. Área = radio2*Pi perímetro = 2*Pi*radio Pista: math.pi

'''
import math

def calcularAreaPerimetro(radio):
    area = radio ** 2 * math.pi
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input('Dame el radio de la circunferencia: '))
area, perimetro = calcularAreaPerimetro(radio)
print('El área es:', area)
print('El perímetro es:', perimetro)