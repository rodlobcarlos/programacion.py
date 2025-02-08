#quitaPorDetras: Le quita a un número n dígitos por detrás (por la derecha). 

cadena = input('Dame un número: ')
num_digitos = int(input('Dime cuantos digitos quieres que quite: '))
cadena_1 = cadena [0:len(cadena)-num_digitos]
print('Número resultante:',cadena_1)