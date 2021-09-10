# Desafío - Listas Cinco
# Patricio Cortés
# G18
# 09-09-2021

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

# define una lista temporal con los valores flotantes
list_tmp1 = [] # lista de los primeros numericos (flotantes)

# crea una nueva lista con el primer numerico de la lista anidada
for i in lista_anidada:
    list_tmp1.append(i[1]) # agrega un nuevo valor a la lista temporal 1

# imprime la lista de valores flotantes
# print(list_tmp1)

# calcula el promedio de los primeros numericos
promedio_list1 = round(promedio(list_tmp1),2)
# print(promedio_list1)

# genera lista con los valores flotantes que sean mayores que el promedio
lista_final = filter(lambda x: x > promedio_list1, list_tmp1) # usa operacion funcional "filter"

# imprime la lista
print("La lista de valores flotantes mayores que el promedio es:")
print(list(lista_final))

# Fin del Programa
