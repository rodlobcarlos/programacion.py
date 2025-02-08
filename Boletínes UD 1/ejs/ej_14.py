#Escribe un programa que tome la calificación de un examen como entrada y
#muestre la calificación equivalente en letras (A, B, C, D o F) según la siguiente
#escala: 90-100 A, 80-89 B, 70-79 C, 60-69 D, por debajo de 60 F

examen = int(input('Dime la nota del examen: '))

if examen >= 90 and examen <= 100: 
    print('A')
if examen >= 80 and examen <= 89: 
    print('B')
if examen >= 70 and examen <= 79: 
    print('C')
if examen >= 60 and examen <= 69: 
    print('D')
if examen >= 0 and examen <= 60: 
    print('F')