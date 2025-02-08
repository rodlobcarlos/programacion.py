habitaciones_list = ['azul_1, roja_2, verde_3, rosa_4, gris_5']
print(habitaciones_list)
habitacion = int(input('Dime el número de una habitación: '))

azul = 1
roja = 2
verde = 3
rosa = 4
gris = 5

cama_1 = 2
cama_2 = 1
cama_3 = 3
cama_4 = 2
cama_5 = 1

planta_1 = 'primera'
planta_2 = 'segunda'
planta_3 = 'tercera'

match habitacion:
    case 1|2:
        if habitacion == 1:
            print(f'Tiene {cama_1} camas y está en la {planta_1} planta.')
        elif habitacion == 2:
            print(f'Tiene {cama_2} cama y está en la {planta_1} planta.')
    case 3|4:
        if habitacion == 3:
            print(f'Tiene {cama_3} camas y está en la {planta_2} planta.')
        elif habitacion == 4:
            print(f'Tiene {cama_4} camas y está en la {planta_2} planta.')
    case 5:
        print(f'Tiene {cama_5} cama y está en la {planta_3} planta.')