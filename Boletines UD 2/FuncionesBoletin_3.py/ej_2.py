'''
Construye un programa que almacene en una lista de listas los siguientes valores.
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
        lista_1.append(lista)
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