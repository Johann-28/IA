import random
import math
import time
inicio = time.time()

    # Lista de objetos (peso, valor)

objetos = [(32, 10), (52, 24), (15, 15), (23, 35), (67, 7), (23, 11), (84, 78), (96, 88), (76, 34), (4, 87), 
           (40, 30), (53, 58), (21, 13), (10, 30), (35, 61), (23, 78), (64, 45), (71, 9), (59, 2), (99, 12), 
           (53, 87), (48, 58), (24, 90), (89, 8), (39, 91), (6, 89), (45, 73), (80, 75), (62, 20), (60, 68), 
           (49, 60), (74, 46), (35, 30), (89, 59), (5, 56), (36, 29), (50, 10), (61, 35), (89, 52), (8, 6), 
           (72, 6), (77, 28), (47, 69), (9, 14), (37, 97), (47, 17), (67, 48), (46, 33), (7, 83), (98, 56), 
           (35, 62), (13, 27), (37, 29), (22, 49), (52, 7), (29, 95), (84, 64), (23, 64), (27, 4), (27, 58), 
           (46, 18), (77, 17), (3, 92), (28, 50), (13, 28), (92, 13), (34, 56), (51, 35), (18, 36), (72, 81), 
           (40, 25), (31, 17), (37, 31), (85, 48), (78, 30), (6, 29), (68, 73), (23, 58), (32, 24), (7, 48), 
           (46, 34), (28, 17), (56, 67), (8, 16), (71, 2), (92, 67), (61, 47), (18, 61), (15, 97), (62, 95), 
           (9, 77), (33, 17), (90, 5), (84, 51), (29, 47), (84, 48), (12, 73), (23, 85), (89, 72), (58, 48), 
           (69, 30), (64, 6), (47, 13), (25, 23)]
capacidad_mochila = 500
temperatura_inicial = 100
enfriamiento = 0.999



 

# Función para calcular el valor total de una solución
def calcular_valor(solucion, objetos):
    valor = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            valor += objetos[i][1]
    return valor

 

# Función para calcular el peso total de una solución
def calcular_peso(solucion, objetos):
    peso = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            peso += objetos[i][0]
    return peso

 

# Función para generar una solución vecina
def generar_vecino(solucion):
    vecino = list(solucion)
    i = random.randint(0, len(vecino) - 1)
    if vecino[i] == 0:
        vecino[i] = 1
    else:
        vecino[i] = 0
    return vecino

 

# Función para aplicar el algoritmo de reconocimiento simulado
def simulated_annealing(objetos, capacidad_mochila, temperatura_inicial, enfriamiento):
    # Inicialización
    solucion_actual = [random.randint(0, 1) for _ in range(len(objetos))]
    valor_actual = calcular_valor(solucion_actual, objetos)
    mejor_solucion = list(solucion_actual)
    mejor_valor = valor_actual

    # Bucle principal
    temperatura = temperatura_inicial
    while temperatura > 1:
        for i in range(100):
            # Generar una solución vecina
            vecino = generar_vecino(solucion_actual)

            # Evaluar la solución vecina
            valor_vecino = calcular_valor(vecino, objetos)
            peso_vecino = calcular_peso(vecino, objetos)

            # Aceptar o rechazar la solución vecina
            if peso_vecino <= capacidad_mochila and (valor_vecino > valor_actual or math.exp((valor_vecino - valor_actual) / temperatura) > random.random()):
                solucion_actual = list(vecino)
                valor_actual = valor_vecino

            # Actualizar la mejor solución encontrada
            if valor_actual > mejor_valor and peso_vecino <= capacidad_mochila:
                mejor_solucion = list(solucion_actual)
                mejor_valor = valor_actual

        # Enfriamiento
        temperatura *= enfriamiento

    return mejor_solucion, mejor_valor
def imprimir_resultados(solucion, valor, peso):
    print("Solución: ", end="")
    for i in range(len(solucion)):
        if solucion[i] == 1:
            print(f"{i+1} ", end="")
    print("\nValor: ", valor)
    print("Peso: ", peso)



solucion, valor = simulated_annealing(objetos, capacidad_mochila, temperatura_inicial, enfriamiento)
peso = calcular_peso(solucion, objetos)
imprimir_resultados(solucion, valor, peso)

final = time.time()

print(final - inicio)
