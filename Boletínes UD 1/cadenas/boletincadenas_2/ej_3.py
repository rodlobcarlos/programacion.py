#Crea una programa que muestre un mensaje para elegir las siguientes opciones:
#Escribir por pantalla cada carácter de una cadena introducida por teclado.
#Contar el % de veces que aparece un carácter que se ha introducido por teclado. 

cadena = input('Escribe una cadena de texto: ')

for caracter in cadena:     
    print(caracter)


caracter = input('Dime el caracter que quieres calcular: ')
rep = cadena.count(caracter)
if len(cadena) > 0:
    calculo = (rep / len(cadena)) * 100
print(calculo,'%')