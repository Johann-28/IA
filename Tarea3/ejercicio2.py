import time
inicio = time.time()

# Objetos con sus beneficios y pesos
items = [
    {"value": 10, "weight": 269},
    {"value": 55, "weight": 95},
    {"value": 10, "weight": 4},
    {"value": 47, "weight": 60},
    {"value": 5, "weight": 32},
    {"value": 4, "weight": 23},
    {"value": 50, "weight": 72},
    {"value": 8, "weight": 80},
    {"value": 61, "weight": 62},
    {"value": 85, "weight": 65},
    {"value": 87, "weight": 46},
]
# Define valor maximo de la mochila
max_weight = 300
# Función de búsqueda de profundidad
def knapsack_dfs(items, max_weight):
    stack = [(0, 0, [])] # (beneficio, peso, item)
    best_value = 0
    best_items = []
    while stack:
        value, weight, taken_items = stack.pop()
        if weight > max_weight:
            continue
        if value > best_value:
            best_value = value
            best_items = taken_items
        for i, item in enumerate(items):
            if i not in taken_items:
                new_value = value + item["value"]
                new_weight = weight + item["weight"]
                new_items = taken_items + [i]
                stack.append((new_value, new_weight, new_items))
    return (best_value, best_items)
# Imprime resultados
best_value, best_items = knapsack_dfs(items, max_weight)
print("Mejor beneficio:", best_value)
print("Items:", best_items)

fin = time.time()

print('Tiempo de ejecucion: ', fin-inicio)