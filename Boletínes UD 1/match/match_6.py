yo = input('Elige una opción: ')
yo = yo.upper() 

import random
apuesta_maquina = random.randint(0,2)
match yo:
    case 'PIEDRA'|'PAPEL'|'TIJERA':
        if yo == 'PIEDRA' and apuesta_maquina == 0:
            print('Empate.')
        elif yo == 'PIEDRA' and apuesta_maquina == 2:
            print('Gana la máquina.')
        elif yo == 'PIEDRA' and apuesta_maquina != 2 and apuesta_maquina != 0:
            print('Has ganado!')
        if yo == 'PAPEL' and apuesta_maquina == 1:
            print('Empate.')
        elif yo == 'PAPEL' and apuesta_maquina == 0:
            print('Gana la máquina.')
        elif yo == 'PAPEL' and apuesta_maquina != 1 and apuesta_maquina != 0:
            print('Has ganado!')
        if yo == 'TIJERA' and apuesta_maquina == 2:
            print('Empate.')
        elif yo == 'TIJERA' and apuesta_maquina == 1:
            print('Gana la máquina.')
        elif yo == 'TIJERA' and apuesta_maquina != 2 and apuesta_maquina !=1:
            print('Has ganado!') 