#Haz un programa que permita calcular la suma de dos números. Pedirá dos números al usuario y mostrará su suma, volviendo a repetir hasta que ambos números introducidos sean 0.

import random

numero = random.randint(1,10)

num_1 = int(input('Dame un número: '))
while numero != num_1: 
    num_1 = int(input('Dame un número: '))
print(f'Has acertado!')