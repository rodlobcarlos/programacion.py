# Modifica el programa anterior para que además nos muestre si el número es impar.

numero = int(input('Introduce un número: '))

multiplo = 6 

if numero % 2 == 0: 
    print('Es par.')
else:
    print('Es impar.')
if numero % multiplo == 0:
    print('Y es múltiplo de 6.')
else:
    print('No es múltiplo de 6.')