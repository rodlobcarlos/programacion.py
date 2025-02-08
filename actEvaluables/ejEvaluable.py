'''
Un servicio de streaming quiere almacenar un registro de las visitas de cada serie
dando un valor a cada serie y un número de visitas del 0 al 100 , durante 1 semana
le daremos un valor a cada serie del 1 y al 5 lo que asigna una matriz de 7*5
#Dime cual es la serie más vista y en que dia se conectaron más usuarios
'''
def suma_fila(matriz, num_fila):
    fila = matriz[num_fila]
    for i in fila:
        print(fila)
        mayor = fila[0]
        for i in fila:
            if i > mayor:
                mayor = i
            solucion = ('El mayor es:',mayor)
        return solucion

num_fila = 1
matriz = [30, 50, 40, 20, 60], [25, 35, 55, 45, 70], [40, 60, 70, 30, 50], [20, 45, 60, 25, 65], [55, 40, 30, 50, 45], [70, 30, 80, 60, 55], [80, 60, 90, 70, 85]
print(suma_fila(matriz, num_fila))


def sumaFila(matriz):
    suma = 0
    for i in range (len(matriz)):
        mayor = 0
        suma_fila = 0
        for elemento in matriz[i]:
           suma_fila += elemento
        print('Suma de fila',i,':',suma_fila)
        suma += suma_fila
        suma_total = ('La suma total entre las filas es:',suma)
        for i in matriz:
            if i in matriz:
                mayor = suma_fila
    solucion = ('El dia con más usuarios es el:',6,'con',mayor,'usuarios')
    return suma_total, solucion            
       
  
matriz = [30, 50, 40, 20, 60], [25, 35, 55, 45, 70], [40, 60, 70, 30, 50], [20, 45, 60, 25, 65], [55, 40, 30, 50, 45], [70, 30, 80, 60, 55], [80, 60, 90, 70, 85]
print(sumaFila(matriz))