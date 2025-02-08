num = int(input('Dame un número: '))

calculo = num ** 2
while num >= 0:
    calculo = num ** 2
    print(calculo)
    num = int(input('Dame un número: '))
else:
    print('No se puede elevar un número negativo.')