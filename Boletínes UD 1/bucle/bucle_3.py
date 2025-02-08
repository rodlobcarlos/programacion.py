#Escribe un programa que pida al usuario un número y devuelva la tabla de múltiplicar 
#de ese número del 1 al 10

num_1 = int(input('Dame un número: '))
num_2 = int(input('Dame un número: '))

suma = num_1 + num_2
while num_1 and num_2 != 0: 
    print(suma)
    num_1 = int(input('Dame un número: '))
    num_2 = int(input('Dame un número: '))
print('El resultado es 0. ')