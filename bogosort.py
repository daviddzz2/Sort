import random
import timeit

def is_sorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def bogosort(lista):
    while not is_sorted(lista):
        random.shuffle(lista)
    return lista

start = timeit.default_timer()
lista_1 = [3, 2, 5, 8, 4, 6, 7, 1]

print("Original array:", lista_1)
sorted_lista1 = bogosort(lista_1)
print("Sorted array:", sorted_lista1)

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8]

print("Original array:", lista_2)
sorted_lista2 = bogosort(lista_2)
print("Sorted array:", sorted_lista2)

lista_3 = [8, 7, 6, 5, 4, 3, 2, 1]

print("Original array:", lista_3)
sorted_lista3 = bogosort(lista_3)
print("Sorted array:", sorted_lista3)

end = timeit.default_timer()
print("Execution time:", end - start)