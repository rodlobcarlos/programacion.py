# Realizar un programa que solicite 4 números e 
# imprima la media de los números. También debe imprimir 
# aquellos números que son superiores a la media


numero_1 = int(input('Dame un número: '))
numero_2 = int(input('Dame un número: '))
numero_3 = int(input('Dame un número: '))
numero_4 = int(input('Dame un número: '))

media = ((numero_1 + numero_2 + numero_3 + numero_4) / 4)
print(media)

if numero_1 > media:
    print(f'{numero_1} es mayor que la media.')
if numero_2 > media:
    print(f'{numero_2} es mayor que la media.')
if numero_3 > media:
    print(f'{numero_3} es mayor que la media.')
if numero_4 > media:
    print(f'{numero_4} es mayor que la media.')
