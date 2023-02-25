import networkx as nx
import matplotlib.pyplot as plt


grafica = {
        'A': [('B',1),('C',2),('D',3)],
        'B': [('A',1),('C',4)],
        'C': [('B',4),('A',2),('D',5)],
        'D': [('A',3),('C',5)],
}

graph = nx.Graph()

for node in grafica:
    graph.add_node(node)

for node in grafica:
    for edge in grafica[node]:
        graph.add_edge(node,edge[0],weight=edge[1])

pos = nx.spring_layout(graph)

nx.draw(graph, pos, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

plt.show()