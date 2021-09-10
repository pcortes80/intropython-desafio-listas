# Desafío - Asociar
# Patricio Cortés
# G18
# 10-09-2021

# define las listas velocidad y distancia
velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,11, 11, 12, 12, 12, 12, 13, 13,13, 13, 14, 14, 14, 14, 15, 15,15, 16, 16, 17, 17, 17, 18, 18,18, 18, 19, 19, 19, 20, 20, 20,20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,17, 28, 14, 20, 24, 28, 26, 34, 34,46, 26, 36, 60, 80, 20, 26, 54, 32,40, 32, 40, 50, 42, 56, 76, 84, 36,46, 68, 32, 48, 52, 56, 64, 66, 54,70, 92, 93, 120, 85]

# var es el parametro de la funcion
def promedio(var):
    promedio_lista = sum(var)/len(var)  # saca el promedio
    return promedio_lista               # devuelve el promedio de la lista

# obtiene velocidad y distancia promedio
vel_prom = promedio(velocidad)
dist_prom = promedio(distancia)

# define la lista de tuplas
lista_tuplas = []

# asociar velocidad y distancia
for i in zip(velocidad, distancia):
    lista_tuplas.append(i)

# imprime la lista de asociaciones (tuplas)
# print("Lista de asociaciones = ",lista_tuplas)

# define contadores
contador1 = 0 # cuenta cuantas veces ocurre que: velocidad bajo el promedio
contador2 = 0 # cuenta cuantas veces ocurre que: velocidad bajo el promedio y distancia sobre el promedio
contador3 = 0 # cuenta cuantas veces ocurre que: velocidad sobre el promedio
contador4 = 0 # cuenta cuantas veces ocurre que: velocidad sobre el promedio y distancia bajo el promedio

# busca cuantas veces ocurre velocidad bajo el promedio
for i in lista_tuplas:
    vel = i[0]
    if vel < vel_prom:
        contador1 += 1
print("Velocidad bajo el promedio de {} ocurrió {} veces.".format(vel_prom,contador1))

# busca cuantas veces ocurre velocidad bajo el promedio y distancia sobre el promedio
for i in lista_tuplas:
    vel = i[0]
    dis = i[1]
    if (vel < vel_prom) and (dis > dist_prom):
        contador2 += 1
print("Velocidad bajo el promedio de {} y distancia sobre el promedio de {} ocurrió {} veces.".format(vel_prom,dist_prom,contador2))

# busca cuantas veces ocurre velocidad sobre el promedio
for i in lista_tuplas:
    vel = i[0]
    if vel > vel_prom:
        contador3 += 1
print("Velocidad sobre el promedio de {} ocurrió {} veces.".format(vel_prom,contador3))

# busca cuantas veces ocurre velocidad sobre el promedio y distancia bajo el promedio
for i in lista_tuplas:
    vel = i[0]
    dis = i[1]
    if (vel > vel_prom) and (dis < dist_prom):
        contador4 += 1
print("Velocidad sobre el promedio de {} y distancia bajo el promedio de {} ocurrió {} veces.".format(vel_prom,dist_prom,contador4))

# Fin del programa
