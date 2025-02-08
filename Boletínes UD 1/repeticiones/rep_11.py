# Diseñar un programa que muestre el producto de los 10 primeros números impares.



num = int(input('Dame un número: '))

for i in range (1,11,2):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')