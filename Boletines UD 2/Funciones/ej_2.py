'''
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
El programa pedirá el número de días que se van a introducir.
'''
def temperaturaMedia(num_1, num_2):
    media = (num_1 + num_2) / 2
    return media

dias = int(input('Dame el número de días que quieres calcular: '))

for i in range(0, dias):
    temp_max = int(input('Dime la temperatura máxima: '))
    temp_min = int(input('Dime la temperatura mínima: '))
    resultado = temperaturaMedia(temp_max, temp_min)
    print(resultado)