'''
Crear una funciónllamada "Login", que recibe un nombre de usuario 
y una contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" 
y la contraseña es "asdasd". Además recibe el número de intentos que se ha intentado hacer login 
y si no se ha podido hacer login incremente este valor.  
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo.
'''
def Login(usuario, contrasena):
    return usuario == "usuario1" and contraseña == "asdasd"

max_intentos = 3
intento = 0
for intento in range(max_intentos):
    usuario = input('Dame el nombre de usuario: ')
    contrasena = input('Dame la contraseña: ')

    if Login(usuario, contraseña):
        print('Bienvenido!')
        intentos = max_intentos
    else:
        print("Usuario o contraseña incorrectos.")
        if intento < max_intentos - 1:
                print('Intentos restantes:', max_intentos - (intento + 1))
        else:
            print('Acceso denegado.')