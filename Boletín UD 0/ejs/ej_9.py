numero_1 = int(input('Dame un numero: '))
numero_2 = int(input('Dame un segundo numero: '))
numero_3 = int(input('Dame un tercer numero: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    mayor = numero_1
if numero_2 > numero_1 and numero_2 > numero_3: 
    mayor = numero_2
else: 
    mayor = numero_3

print(f'El número más grande de los tres es: {mayor}.')