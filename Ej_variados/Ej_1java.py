'''
En un centro educativo, en un determinado nivel existen 4 grupos: A, B, C y D. 
El grupo A tiene 25 alumnos, el B tiene 28, el C tiene 31 y el D tiene 29. Para cada alumno disponemos de las notas del primer, segundo y tercer parcial. Realizar un programa en Java que:
Pida la letra del grupo que se va a introducir (sólo se va a introducir un grupo).
Para ese grupo, pida para cada alumno el nombre, la nota del primer parcial, del segundo y del tercero. 
Debe mostrarse al final: El nombre del alumno con mayor nota media (media de los tres parciales). Cuántos alumnos tienen la nota media suspensa. Si existe algún 
Debe mostrarse al final: 
El nombre del alumno con mayor nota media 
Si existe alumnado con nota  igual o superior a 9, debe indicarse al final con el mensaje:
“Existen sobresalientes”
'''
def grupos():
    mayor = 0
    contador = 0
    grupo = input('Escribe la letra del grupo: ').upper()
    while grupo == 'A' or grupo == 'B' or grupo == 'C' or grupo == 'D':
        print('Has elegido el grupo',grupo)
        if grupo == 'A':
            alumnos = 5
        elif grupo == 'B':
            alumnos = 6
        elif grupo == 'C':
            alumnos = 3
        elif grupo == 'D':
            alumnos = 4
        for grupo in range(alumnos):
            alumno = input('Escribe tu nombre: ')
            nota = int(input('Nota del primer parcial: '))
            nota_2 = int(input('Nota del segundo parcial: '))
            nota_3 = int(input('Nota del tercer parcial: '))
            print('Alumno:',alumno,'; Notas:',nota,';',nota_2,';',nota_3)
            nota_media = (nota + nota_2 + nota_3) / 3
            print('Nota media',nota_media)
            if nota_media > mayor:
                mayor = nota_media
                print('El alumno con mayor nota media es:',alumno,mayor)
            if nota_media < 5:
                contador += 1
            if nota_media >= 9:
                print('Existen sobresalientes.')
        print('Suspensos',contador)

grupos()