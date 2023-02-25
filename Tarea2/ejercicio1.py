import grafo as gr
import time

inicio = time.time()

grafica = {
        'A': [('B',1),('C',2),('D',3)],
        'B': [('A',1),('C',4)],
        'C': [('B',4),('A',2),('D',5)],
        'D': [('A',3),('C',5)],
}

graph = gr.Grafo(grafica)


for g in grafica:
    for x in grafica:
        if g == x:
            continue

        path = graph.shortestPath(start=g,end=x)
        print('El camino mas corto de ',g,' a ',x,' es: ',path[0], 'con costo: ', path[1])

print(graph.shortestPath(start='B',end='C'))

fin = time.time()

print('Tiempo de ejecucion: ', fin-inicio)