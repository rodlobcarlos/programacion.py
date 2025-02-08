#Construye un programa que pida  al usuario que ingrese  números hasta que ingrese un cero y luego muestra la suma de los números ingresados.



suma = 0
numero = int(input('Dame un numero: '))

while numero != 0: 
    suma = suma + numero
    numero = int(input('Dame un numero: '))
print(suma)