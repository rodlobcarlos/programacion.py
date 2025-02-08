#Realizar un programa que solicite dos números 
# por teclado e imprima en pantalla si son iguales, 
# el primero mayor que el segundo o el primero más pequeño que el segundo

numero_1 = int(input('Introduce un número: '))
numero_2 = int(input('Introduce otro número: '))

if numero_1 == numero_2:
    print('Son iguales.')
elif numero_1 > numero_2:
    print(f'El número {numero_1} es mayor que {numero_2}.')
else:
    print(f'El número {numero_1} es más pequeño que {numero_2}.')
