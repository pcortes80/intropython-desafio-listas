# Desafío - Listas Dos
# Patricio Cortés
# G18
# 07-09-2021

# vel es el parametro de la funcion
def promedio(vel):
    promedio_lista = sum(vel)/len(vel)  # saca el promedio
    return promedio_lista               # devuelve el promedio de la lista

# listas de autos
auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

lista_anidada = [auto1,auto2,auto3,auto4,auto5,auto6]

# define 3 listas temporales
list_tmp1 = [] # lista de los primeros numericos
list_tmp2 = [] # listas de los segundos numericos 
list_tmp3 = [] # listas de los terceros numericos

# crea una nueva lista con el primer numerico de la lista anidada
for i in lista_anidada:
    list_tmp1.append(i[1]) # agrega un nuevo valor a la lista temporal 1
    list_tmp2.append(i[2]) # agrega un nuevo valor a la lista temporal 2
    list_tmp3.append(i[4]) # agrega un nuevo valor a la lista temporal 3

# calcula el promedio de los primeros numericos
promedio_list1 = round(promedio(list_tmp1),2)
print(promedio_list1)

# calcula el promedio de los segundos numericos
promedio_list2 = round(promedio(list_tmp2),2)
print(promedio_list2)

# calcula el promedio de los terceros numericos
promedio_list3 = round(promedio(list_tmp3),2)
print(promedio_list3)

# Fin del Programa
