#Realizar un programa que lea un carácter y dos números enteros por teclado.
#Si el carácter leído es un operador aritmético, calcular la operación correspondiente, si es cualquier otro debe mostrar un error.


numero_1 = int(input('Dame un número: '))
caracter = input('Dame un caracter: ')
numero_2 = int(input('Dame otro número: '))

signos = ('+, -, *, /, //, **, %')

if caracter == '+': 
    print(numero_1 + numero_2)
elif caracter == '-': 
    print(numero_1 - numero_2)
elif caracter == '*': 
    print(numero_1 * numero_2)
elif caracter == '/': 
    print(numero_1 / numero_2)
elif caracter == '//':
    print(numero_1 // numero_2)
elif caracter == '**':
    print(numero_1 ** numero_2)
elif caracter == '%':
    print(numero_1 % numero_2)
else: 
    print('Error.')