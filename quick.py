import random
import timeit

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
numeros_ejemplo = [3, 66, 8, 10, 1, 2, 23, 21, 33, 77]

# Lista aleatoria generada
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
# Lista invertida de la de ejemplo
numeros_invertidos = list(reversed(numeros_ejemplo))

print("Lista de ejemplo:", numeros_ejemplo)
print("Ordenada:", quicksort(numeros_ejemplo))

print("\nLista aleatoria generada:", numeros_aleatorios)
print("Ordenada:", quicksort(numeros_aleatorios))

print("\nLista invertida de la de ejemplo:", numeros_invertidos)
print("Ordenada:", quicksort(numeros_invertidos))

# Medir tiempos de ejecución
tiempo_ejemplo = timeit.timeit(lambda: quicksort(numeros_ejemplo), number=1000)
tiempo_aleatoria = timeit.timeit(lambda: quicksort(numeros_aleatorios), number=1000)
tiempo_invertida = timeit.timeit(lambda: quicksort(numeros_invertidos), number=1000)

print(f"\nTiempo de ordenación (lista de ejemplo): {tiempo_ejemplo:.6f} segundos")
print(f"Tiempo de ordenación (lista aleatoria): {tiempo_aleatoria:.6f} segundos")
print(f"Tiempo de ordenación (lista invertida): {tiempo_invertida:.6f} segundos")