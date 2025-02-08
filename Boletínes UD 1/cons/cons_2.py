#Construye un programa que dado un número me devuelva un triángulo de *. Imagina que le damos el 5, la primera fila tendrá un *, dos la segunda, así hasta que la quinta tenga 5. 


n = 5
i = 1

while i <= n:
    print(i * '*')
    i += 1