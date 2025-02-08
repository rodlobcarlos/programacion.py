#Dado el siguiente código, responde qué devolverán las siguientes instrucciones:
frase = "Esto es un ejemplo"
subcadena = "ejemplo"
resultado = ""

print(frase[1]+subcadena)
print(frase[1]+subcadena[:3])
print( frase[frase.find("s"):])

cadena = "HOLA LOLA"
cadena =cadena.replace("L", "C")
print(cadena)