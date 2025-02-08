# Modifica el programa anterior para incluir otra condición que nos diga, además, si el número es menor que 6

mes = int(input('Introduce un numero correspondiente a un mes: '))

if mes < 12: 
    print('Valor correcto')
if mes < 6: 
    print('El valor es menor que 12 y 6.')