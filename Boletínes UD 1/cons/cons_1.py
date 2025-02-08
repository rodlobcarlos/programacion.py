#Calcula cuánto vale resultado siguiendo la traza de ejecución:

i = int(input('Dame un número: '))

n = 15 
while i % 2 == 0: 
    resultado = n + 2 * i
else: 
    resultado = n + 2 * i + 1

print(f'El resultado es: {resultado}')