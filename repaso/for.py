'''cadena = 'Piogram'
for letra in cadena: 
    print('Hola') # Por cada letra de la palabra, imprime un 'Hola'

print('-------------------------------------------------')

cadena = 'Piogram'
for letra in cadena: 
    print(letra) # Imprime cada letra de la palabra

cadena = input('Escribe una palabra: ').lower()
for letra in cadena:
    if letra == 'a' or letra == 'e' or letra == 'o':
        print(letra) # Imprime cada vocal abierta de la palabra'''

'''lista = ['Hola', 'Adios', 'Carlos', 'Pepe']
for cadena in lista: # Este for recorre cada cadena de la lista
    print(cadena)
    for letra in cadena: # Este for recorre cada letra de la cadena recorrida anteriormente hasta completar dicha cadena
        if letra == 'a' or letra == 'o' or letra == 'e':
            print(letra)'''

'''num = int(input('Escribe un número: '))
for i in range(0, 11): # i = a cada numero de 0 a 11-1(10)
    resultado = i*num # Multiplica cada número recorrido por el número dado por el usuario
    print(i,'x',num,'=',resultado)'''

'''frutas = ['Mora','sandía','fresa','piña','uva']
for i in range(len(frutas)): # Recorre cada posicion de la lista
    fruta = frutas[i] #Cogemos cada elemento de la posicion recorrida
    print(i,fruta)'''

'''frutas = ['Mora','sandía','fresa','piña','uva']
precio_fruta = [0.50, 1.00, 1.55, 1.20, 2.00]
for i in range(len(frutas)):
    # Al ser listas paralelas, el valor de la i es el mismo en las dos listas
    fruta = frutas[i]
    precio = precio_fruta[i]
    if precio < 1.50:
        print(fruta)'''

'''frutas = ['Mora','fresa','Mora','piña','uva']
cantidad = [5, 10, 3, 5, 10]
clientes = ['Axell', 'Zarinna', 'Luis', 'Joel', 'Kevin']
for i in range(len(frutas)):
    fruta = frutas[i]
    if fruta == 'Mora':
        cant = cantidad[i]
        clint = clientes[i]
        print(cant, clint)'''