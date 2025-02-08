#pegaPorDelante: Añade un dígito a un número por delante. 
cadena = input('Dame un número: ')
num_digitos = int(input('Dime cuantos digitos quieres que quite: '))
cadena_1 = cadena [num_digitos:len(cadena) + cadena]
print('Número resultante:',cadena_1)