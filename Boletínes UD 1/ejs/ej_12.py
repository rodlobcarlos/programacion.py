#Realizar un programa que lea el estado civil de una persona (S-Soltero,
#CCasado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
#pantalla el porcentaje de retención que debe aplicarse de acuerdo con las
#siguientes reglas:
#○ Alossolteros o divorciados menores de 35 años, un 12% 
# Unidad 1 Boletín 0 Programación Estructurada: Condicionales
#○ Todaslaspersonas mayores de 50 años, un 8.5%
#○ Alosviudosocasados menores de 35 años, un 11.3%
# ○ Alresto decasos se le aplica un 10.5%


Estado_civil = input('Dime su estado civil: ')
edad = int(input('Dime su edad: '))

estado_civil_1 = 'soltero'
estado_civil_2 = 'casado'
estado_civil_3 = 'viudo'
estado_civil_4 = 'divorciado'

if estado_civil_1 or estado_civil_4 < 35:
    print('El porcentaje de retención es de un 12%')
elif estado_civil_1 or estado_civil_2 or estado_civil_3 or estado_civil_4 > 50: 
    print('El porcentaje de retención es de 8,5%. ')
elif estado_civil_3 or estado_civil_2 < 35: 
    print('El porcentaje de retención es de 11,3%. ')
else: 
    print('El porcetaje de retención es de 10,5%. ')