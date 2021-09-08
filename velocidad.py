# Desafío - Velocidad
# Patricio Cortés
# G18
# 07-09-2021

# define la lista de velocidades
velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

# vel es el parametro de la funcion
def promedio(vel):
    promedio_lista = sum(vel)/len(vel)  # saca el promedio
    return promedio_lista               # devuelve el promedio de la lista

# muestra en pantalla, aunque no se solicite en el desafio
print(promedio(velocidad))

# Fin de Programa
