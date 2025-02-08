#pegaPorDelanteNVeces: Similar al ejercicio 9 pero ahora añado por el principio en lugar de por el final.
cadena = input('Dame un número: ')
añadir = input('Dame un número adicional: ')
veces = int(input('Dime cuatas veces lo quieres: '))

cadena_1 = cadena + añadir*veces + len(cadena)
print('El número resultante es:',cadena_1)