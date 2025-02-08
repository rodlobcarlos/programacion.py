#quitaPorDelante: Le quita a un número n dígitos por delante (por la izquierda). 
cadena = input('Dame un número: ')
num_digitos = int(input('Dime cuantos digitos quieres que quite: '))
cadena_1 = cadena [num_digitos:len(cadena)]
print('Número resultante:',cadena_1)