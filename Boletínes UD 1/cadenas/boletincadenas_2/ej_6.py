#Realiza un programa que dado el siguiente texto:
#Presente cada frase (terminada con .)  en una línea diferente. 
#Cuente cuántas frases hay y cuántas palabras. 

cadena = ('La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos. Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios. Le explicamos cómo funcionan los ataques de inyección de SQL, cómo combatirlos y cómo una herramienta antivirus potente lo puede proteger contra las consecuencias.')
cadena = cadena.replace('.','.\n')
print(cadena)

cadena = cadena.split('.') and cadena.replace('.','.\n')
print(cadena)

separado = cadena.split('.')

espacio = cadena.split()

for cadena in separado:
    print(cadena)

print(len(separado))
print(len(espacio))