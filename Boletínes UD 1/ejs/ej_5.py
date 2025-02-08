#Modifica el programa anterior para que nos diga: ○ Siespar, i.
# ese caso mire si, además, es múltiplo de 6.
#Si es múltiplo de 6 → imprime múltiplo de 6
#Si no, no hace nada

numero = int(input('Introduce un número: '))

multiplo = 6 

if numero % 2 == 0: 
    print('Es par.')
if numero % multiplo == 0:
    print('Y es múltiplo de 6.')
else:
    print('Pero no es múltiplo de 6.')