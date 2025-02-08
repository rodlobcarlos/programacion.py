'''
Construye una función que te devuelva esto:
[2, 9, 4]
[7, 5, 3]
[6, 1, 8]
De manera que el último elemento aparece el primero y el primero aparece el último. 
Pista: fila invertida y columna invertida
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
        lista_1.insert(0, num) 
        lista_1.insert(lista_1)   
    for i in range(3):
        num = int(input('Dame números: '))
        lista_2.insert(0, num)
    for i in range(3): 
        num = int(input('Dame números: '))
        lista_3.insert(0, num)
        lista_3.insert(lista_3)
    
    lista.append(lista_1)
    lista.append(lista_2)
    lista.append(lista_3)
    return lista

lista.append(lista_1)
lista.append(lista_2)
lista.append(lista_3)
lista_0 = guardarLista()
lista_nueva = imprimeLista(lista_0)