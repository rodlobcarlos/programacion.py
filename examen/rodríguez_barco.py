#Carlos Rodríguez Lobato
#En esta actividad voy a usar una función para el menu, que no resivirá nada e imprimirá por pantalla el menu.


def menu():
    print('============= Hundir la flota ================')
    print('========== I) Iniciar partida ===============')
    print('========== D) Disparar ======================')
    print('========== R) Imprime resultado actual ========================')
    print('========== S) Salir =================================')
    print('=================================================================')
    return menu

menu()

import random
lista = ['pos_0', 'pos_1', 'pos_2', 'pos_3', 'pos_4', 'pos_5', 'pos_6', 'pos_7', 
         'pos_8', 'pos_9', 'pos_10', 'pos_11', 'pos_12',  'pos_13', 'pos_14', 'pos_15', 
         'pos_16', 'pos_17', 'pos_18', 'pos_19','pos_20', 'pos_21', 'pos_22', 'pos_23', 
         'pos_24', 'pos_25', 'pos_26','pos_27', 'pos_28', 'pos_29', ' pos_30', 'pos_31', 
         'pos_32', 'pos_33', 'pos_34', 'pos_35', 'pos_36', 'pos_37', 'pos_38', 'pos_39',
         'pos_40', 'pos_41', 'pos_42','pos_43', 'pos_44', 'pos_45', 'pos_46', 'pos_47', 
         'pos_48', 'pos_49', 'pos_50']

jugador = input('Selecciona una opción: ')

maquina = ('barco_1', 'barco_2', 'barco_3', 'barco_4', 'barco_5', 'barco_6', 'barco_7', 'barco_8', 'barco_9', 'barco_10')
salida = True
while salida:
    if jugador == 'I': 
        sistema = lista.replace('barco_1', (lista))
    print(sistema)
    elif jugador == 'D':

    elif jugador == 'R':

    elif jugador == 'S':
        print('Has salido.')
        sadida = False