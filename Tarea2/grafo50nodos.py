import random

n = 10
# Crear una lista de adyacencia vacía con 50 nodos
grafo = [[] for _ in range(n)]

# Conectar los nodos aleatoriamente mediante aristas ponderadas
for i in range(n):
    for j in range(i+1, n):
        if random.random() < 0.5:
            peso = random.randint(1, 10)
            grafo[i].append((j, peso))
            grafo[j].append((i, peso))

# Imprimir la lista de adyacencia
for i, adyacentes in enumerate(grafo):
    print(f"{i}: {adyacentes},")