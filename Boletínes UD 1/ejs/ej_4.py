#Lea unnúmeropor teclado y nos diga si o no múltiplo de 3 y de 2.

numero = int(input('Introduce un número: '))

multiplo_1 = 2
multiplo_2 = 3

if numero % multiplo_1 == 0:
    print(f'El número {numero} es múltiplo de {multiplo_1}')
else: 
    print(f'El número {numero} es múltiplo de {multiplo_2}')