'''
pegaPorDetrasNVeces: Modifica el ejercicio anterior para que ahora te pida el número, 
el número a poner por el final y el número de veces que quiero que lo ponga.
Por ejemplo, si mi número es 123456789 y quiero añadir por el final 
el número 8 tres veces el resultado debería ser 123456789888
'''
cadena = input('Dame un número: ')
añadir = input('Dame un número adicional: ')
veces = int(input('Dime cuatas veces lo quieres: '))

cadena_1 = cadena + añadir*veces
print('El número resultante es:',cadena_1)