#Muestra el valor del elemento 6 de una lista f con los días de la semana.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[6])


#Inicializa los 5 primeros elementos de una lista  con números enteros aleatorios del 0 al 8.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[0:5])


#Crea una lista con los 20 primeros números múltiplos de 3
lista = []
for i in range (0,63,3):
    lista.append(i)
print(lista)


#Usa la lista anterior para copiarle por el final
# elemento a elemento ['martes', 'miércoles', 'jueves']
lista = []
for i in range(0, 63, 3):
    lista.append(i)
lista.append('martes')
lista.append('miércoles')
lista.append('jueves')
print(lista)


#Partiendo de la lista de múltiplos de 3, 
# inserta en la posición 8 la palabra “programo”
lista = []
for i in range (0,63,3):
    lista.append(i)
lista.insert(8, 'programo')
print(lista)

'''
#Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, 
# el primero que se introduce es el último en mostrarse y viceversa.
lista = []
i = 0
while i < 10:
    num_1 = int(input('Dame un número:'))
    lista.append(num_1)
    i = i + 1                                          #Falta intentar darle la vuelta a la lista, pero dentro de los [].
    print(lista)
for i in range (len(lista)-1, -1, -1):
    print(lista[i])
'''

#Define tres listas de 20 números enteros cada uno, con nombres numeros, 
# cuadrados y cubos. Inicializa la lista de numeros con valores aleatorios entre 0 y 100. 
# En la lista de cuadrados se deben almacenar los cuadrados de los valores que hay en la lista numeros. 
# En la lista cubos se deben almacenar los cubos de los valores que hay en numeros. A continuación, 
# muestra el contenido de los tres arrays dispuesto en tres columnas.

'''
#Escribe un programa que pida 10 números por teclado y 
# que luego muestre los números introducidos junto 
# con las palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.
lista = []
for i in range(10):
    num=int(input('Dame un número: '))
    lista.append(num)
print(lista)

maximo=max(lista)
minimo=min(lista)

for num in lista:
    if num==maximo:
        print(num,'es el máximo')
    elif num==minimo:
        print(num,'es el mínimo')
    else:
        print(num)      
'''

#Realiza un programa que pida la temperatura media 
# que ha hecho en cada mes de un determinado año y 
# que muestre a continuación un diagrama de barras horizontales con esos datos. 
# Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.



#Escribe un programa que genere 20 números enteros aleatorios 
# entre 0 y 100 y que los almacene en un array. 
# El programa debe ser capaz de pasar todos los números pares a las 
# primeras posiciones de la lista (del 0 en adelante) y 
# todos los números impares a las celdas restantes. 
# Utiliza arrays auxiliares si es necesario.
lista=[]
import random
for i in range(0,100):
    num=random.randint(0,20)
    print(num)