#Escribe un programa que pida al usuario un número y devuelva la tabla de múltiplicar de ese número del 1 al 10



num = int(input('Dame un número: '))
print(f'Tabla de multiplicar del {num}: ')

for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado} ')