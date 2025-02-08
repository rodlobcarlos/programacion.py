#Realizar un programa que lea la edad de una persona 
# menor a 100 años e informe de si es un niño 
# (0-12 años), un adolescente (13-17), un joven (18- 29) o unadulto

edad = int(input('Dime una edad: '))

if edad < 0 or edad >= 100: 
    print('Error, tiene que se menor que 100 y mayor que 0.')

if edad <= 12: 
    print('Es un niño.')
elif edad <= 17: 
    print('Es un adolescente.')
elif edad <= 29: 
    print('Es un joven.')
else:
    print('Es un adulto. ')