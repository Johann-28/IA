import math
import heapq

class Grafo():
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de tuplas de la forma (nodo_destino, peso)
    def __init__(self, graph={}):
        self.graph = graph

    def distancia(self, nodo_a, nodo_b):
        # La distancia euclidiana se usa como la heurística.
        x1 = y1 = len(nodo_a)
        x2 = y2 = len(nodo_b)
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def a_estrella(self, nodo_inicial, nodo_final):
        # Inicializa los conjuntos de nodos abiertos y cerrados
        abiertos = [(0, nodo_inicial)]
        cerrados = set()
        # Inicializa el diccionario de padres, los costos hasta cada nodo y la ruta hasta cada nodo
        padres = {}
        costos = {nodo_inicial: 0}
        ruta = {nodo_inicial: [nodo_inicial]}
        # Comienza la búsqueda
        while abiertos:
            # Saca el nodo con el costo estimado más bajo de la lista de abiertos
            costo_actual, nodo_actual = heapq.heappop(abiertos)
            # Si el nodo actual es el nodo final, termina la búsqueda y devuelve la ruta y el costo de la ruta
            if nodo_actual == nodo_final:
                return ruta[nodo_actual], costos[nodo_actual]
            # Si el nodo actual no es el nodo final, sigue buscando
            cerrados.add(nodo_actual)
            for nodo_vecino, peso in self.graph[nodo_actual]:
                if nodo_vecino in cerrados:
                    continue
                nuevo_costo = costos[nodo_actual] + peso
                if nodo_vecino not in costos or nuevo_costo < costos[nodo_vecino]:
                    costos[nodo_vecino] = nuevo_costo
                    heuristica = self.distancia(self.graph[nodo_vecino], self.graph[nodo_final])
                    heapq.heappush(abiertos, (nuevo_costo + heuristica, nodo_vecino))
                    padres[nodo_vecino] = nodo_actual
                    ruta[nodo_vecino] = ruta[nodo_actual] + [nodo_vecino]
        # Si no hay camino, devuelve None
        return None