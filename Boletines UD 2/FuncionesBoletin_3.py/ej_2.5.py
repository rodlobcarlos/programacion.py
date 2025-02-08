'''
Ahora construye una función dameColumna que dada una matriz y un número de columna, me devuelva la lista de los elementos de esa columna. Por ejemplo si recibe esto 
[a ,b, c]
[d, e, f] 	
[g, h, i]	
y   Devuelvo una  LISTA
columna 0  → [a, d, g]
columna 1 →  [b, e, h] 
columna 2 → [ c, f, i]
'''
lista = []
lista_1 = []
lista_2 = []
lista_3 = []
def imprimeLista(lista):
    for i in range(3):
        print(lista[i])
   
def guardarLista():
    lista = []
    lista_1 = []
    lista_2 = []
    lista_3 = []
    for i in range(3):
        num = int(input('Dame números: '))
        lista_1.append(num)
    for i in range(3):
        num = int(input('Dame números: '))
        lista_2.append(num)
    for i in range(3): 
        num = int(input('Dame números: '))
        lista_3.append(num)
    
    lista.append(lista_1)
    lista.append(lista_2)
    lista.append(lista_3)
    return lista

lista.append(lista_1)
lista.append(lista_2)
lista.append(lista_3)
lista_0 = guardarLista()
lista_nueva = imprimeLista(lista_0)