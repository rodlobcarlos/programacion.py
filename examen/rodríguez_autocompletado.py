#Carlos Rodríguez Lobato
#En este actividad voy a usar una función para que me devuelva la lista de las palabras que empiezan por la letra dada.

lista = ["Core i9", "Ryzen 9", "core i7", "Ryzen 5", "fury Beast", "Vengeance LPX", "trident Z5", 
"Ballistix Sport", "980 PRO", "Black SN850X", "barracuda HDD", "MX500 SSD", "geForce RTX", "radeon RX", 
"GeForce GTX", "Radeon 6600",  "ROG STRIX", "MPG B550", "Aorus X570", "steel legend"]
print(lista)

letra = input('Elige una letra: ')

lista_1 = []
def letra_elegida():
    for palabra in lista:
        if letra == 'c' or letra == 'r' or letra == 'f' or letra == 'v' or letra == 't' or letra == 'b' or letra == '9' or letra == 'm' or letra == 'g' or letra == 'a' or letra == 's':
            lista_1.append(palabra[0])
    print(lista_1)
    return lista_1

letra_elegida()