#Introducir por teclado dos palabras e indicar cuál de ellas es la más corta.
palabra_1 = input('Escribe una palabra: ')
palabra_2 = input('Escribe una palabra: ')

if len(palabra_1) < len(palabra_2):
    print('La palabra',{palabra_1},'es más chica que',{palabra_2})
elif len(palabra_1) > len(palabra_2):
    print('La palabra',{palabra_1},'es más grande que',{palabra_2})