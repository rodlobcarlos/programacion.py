clave = '1234'

while True: 
    contraseña = input('Introduce una contraseña: ')
    
    if contraseña == clave:
        print('Bienvenido!')
        break
    else:
        print('Contraseña incorrecta.')