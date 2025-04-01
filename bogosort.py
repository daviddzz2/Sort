import random

def is_sorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def bogosort(lista):
    while not is_sorted(lista):
        random.shuffle(lista)
    return lista

lista = [3, 2, 5, 1, 4]
print("Original array:", lista)
sorted_lista = bogosort(lista)
print("Sorted array:", sorted_lista)