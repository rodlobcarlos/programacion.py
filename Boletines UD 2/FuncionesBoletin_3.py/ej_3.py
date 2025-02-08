'''
Codifica un programa usando funciones que lea 10 números por teclado, y 
te devuelva la lista de los números que terminan en 3.
'''
lista = []
lista_1 = []
def imprimeLista(lista):
    for i in range(10):
        print(lista[i])
   
def guardarLista():
    lista = []
    lista_1 = []
    for i in range(10):
        num = int(input('Dame números: '))
        lista.append(num)
    
    lista.append(lista_1)
    return lista

lista.append(lista_1)
lista_0 = guardarLista()
lista_nueva = imprimeLista(lista_0)