'''
esCapicua: Devuelve verdadero si el número que se pasa como 
parámetro es capicúa y falso en caso contrario.
'''
num = '1331'

if num[0] == num[-1] and num[1] == num[-2]:
    print('Verdadero.')
else:
    print('Falso.')