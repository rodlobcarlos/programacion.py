import random

estudiantes = ['Carlos', 'Pepe', 'Maria', 'Lucia', 'Antonio']
indice = random.randint(0, 4) # Creamos variable para que elija una posicion aleatoria
estudiante = estudiantes[indice] # estudiante = el elemento de la lista en la posicion elegida antes
print(indice,estudiante)