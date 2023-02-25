import grafo as gr
import time
import networkx as nx
import matplotlib.pyplot as plt


inicio = time.time()

grafica = {
0: [(1, 9), (2, 1), (4, 1), (9, 3)],
1: [(0, 9), (2, 2), (4, 8), (5, 2), (8, 6)],
2: [(0, 1), (1, 2), (3, 4), (4, 3), (5, 4), (7, 2)],
3: [(2, 4), (4, 4), (6, 7), (7, 2)],
4: [(0, 1), (1, 8), (2, 3), (3, 4)],
5: [(1, 2), (2, 4), (8, 10), (9, 10)],
6: [(3, 7), (8, 1)],
7: [(2, 2), (3, 2)],
8: [(1, 6), (5, 10), (6, 1), (9, 7)],
9: [(0, 3), (5, 10), (8, 7)]

}
graph = gr.Grafo(grafica)


for g in grafica:
    for x in grafica:
        if g == x:
            continue

        path = graph.shortestPath(start=g,end=x)
        print('El camino mas corto de ',g,' a ',x,' es: ',path[0], 'con costo: ', path[1])

fin = time.time()

print('Tiempo de ejecucion: ', fin-inicio)


#imprimir grafo
e = nx.Graph()

for node in grafica:
    e.add_node(node)

for node in grafica:
    for edge in grafica[node]:
        e.add_edge(node,edge[0],weight=edge[1])

pos = nx.spring_layout(e)

nx.draw(e, pos, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(e, 'weight')
nx.draw_networkx_edge_labels(e, pos, edge_labels=edge_labels, font_size=10)
plt.show()

print(e)
