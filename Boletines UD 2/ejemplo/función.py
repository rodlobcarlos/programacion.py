def exponente (num_1, num_2):
    contador = 0
    resultado = num_1
    for i in range(1, num_2 + 1):
        resultado = resultado * num_1
        contador += 1
    return resultado

resultadoFuncion = exponente(5, 1)
print(resultadoFuncion)
resultadoFuncion = exponente(5, 2)
print(resultadoFuncion)
resultadoFuncion = exponente(5, 3)
print(resultadoFuncion)