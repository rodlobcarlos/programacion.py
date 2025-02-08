'''''
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
'''
def Multiplo(num1, num2):
    return num1 % num2 == 0

num_1 = int(input('Dame un número: ' ))
num_2 = int(input('Dame otro número: '))

if Multiplo(num_1, num_2):
    print({num_1},'es múltiplo de',{num_2})
elif Multiplo(num_2, num_1):
    print({num_2}, 'es múltiplo de',{num_1})
else:
    print('No hay múltiplos.')