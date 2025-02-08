'''
Crea un función "ConvertirEspaciado", que reciba como parámetro un texto
y devuelve una cadena con un espacio adicional tras cada letra. 
Por ejemplo, "Hola, tú" devolverá "H o l a , t ú ". 
Crea un programa principal donde se use dicha función.
'''
def ConvertirEspaciado(texto):
    resultado = ''
    for caracter in texto:
        resultado += caracter + ' '
    return resultado

texto_normal = input('Escribe un texto: ' )
texto_espaciado = ConvertirEspaciado(texto_normal)
print("Texto con espaciado:", texto_espaciado)
