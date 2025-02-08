'''
Escribir una función que reciba una cadena que contiene un número entero y 
devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 1234567890, 
debe devolver 1.234.567.890.
'''
'''
cadena = '123456789'
num = int(cadena)
resultado = f'{num: ,}'.replace(',','.')
print(resultado)
'''
cadena = "1234567890"
contador = 0
i = 0
cadena_salida = ''
for i in range (len(cadena)-1,-1,-1):
    contador = contador + 1
    if contador != 3:
        cadena_salida = cadena[i] + cadena_salida
        print(cadena_salida)    
    else:
        cadena_salida = '.' + cadena[i] + cadena_salida
        contador = 0    
        print(cadena_salida)