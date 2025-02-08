'''
Escribir dos funciones que permitan calcular:
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
'''
def convertirSegundos(segundos):
    horas = int(segundos / 3600)  
    minutos = int((segundos % 3600) / 60)  
    segundos_restantes = segundos % 60  
    return horas, minutos, segundos_restantes


segundos = int(input('Dame el tiempo en segundos: '))
resultado = convertirSegundos(segundos)
print('horas:', resultado[0])
print('minutos:', resultado[1])
print('segundos_restantes:', resultado[2])