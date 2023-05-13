import csv
import heapq
import pprint

class Node:
    def __lt__(self, other):
        return self.f() < other.f()

    def __init__(self, activity, parent=None, g=0, h=0):
        self.activity = activity
        self.parent = parent
        self.g = g
        self.h = h
    
    def f(self):
        return self.g + self.h

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            activity = {
                'materia': int(row[0]),
                'tema': int(row[1]),
                'subtema': int(row[2]),
                'numero': int(row[3]),
                'duracion': int(row[4]),
                'valor': int(row[5]),
                'requerimiento1': int(row[7]),
                'requerimiento2': int(row[8]),
                'obligatoria': int(row[9])
            }
            data.append(activity)
    return data

def heuristic(activity, target_value):
    return abs(target_value - activity['valor'])

def generate_successors(activity, data):
    successors = []
    for next_activity in data:
        if next_activity['requerimiento1'] == activity['numero'] or next_activity['requerimiento2'] == activity['numero']:
            successors.append(next_activity)
    return successors

def get_path(node):
    path = []
    while node:
        path.append(node.activity)
        node = node.parent
    return path[::-1]

def A_star(min_score, max_score, data):
    open_list = []
    closed_set = set()
    selected_activities = []  # Lista de actividades seleccionadas
    total_duration = 0
    total_value = 0
    
    #Obtener actividades obligatorias
    ob_acts = [activity for activity in data if activity['obligatoria'] == 1 ]
    for activity in ob_acts:
        start_node = Node(activity, None, 0, heuristic(activity, max_score))
        heapq.heappush(open_list, (start_node.f(), start_node))
    #Seleccionar las tareas obligatorias
    while open_list:
        _, current_node = heapq.heappop(open_list)
        current_activity = current_node.activity

        if current_activity['valor'] > max_score:
            continue

        
        # Agregar actividad a la secuencia seleccionada
        total_duration += current_activity['duracion']
        total_value += current_activity['valor']

        if(total_value >= max_score):
            total_duration -= current_activity['duracion']
            total_value -= current_activity['valor']
            break
        
        selected_activities.append(current_activity)

        if total_duration >= min_score and total_value <= max_score:
            return [selected_activities, total_duration,total_value]

        closed_set.add(current_activity['numero'])

        successors = generate_successors(current_activity, data)
        for successor in successors:
            if successor['numero'] not in closed_set:
                g = current_node.g + successor['duracion']
                h = heuristic(successor, current_activity['valor'])
                successor_node = Node(successor, current_node, g, h)
                heapq.heappush(open_list, (successor_node.f(), successor_node))
        
    open_list = []

    # Obtener actividades sin requisitos
    initial_activities = [activity for activity in data if activity['requerimiento1'] == 0 and activity['requerimiento2'] == 0 and activity not in ob_acts]
    for activity in initial_activities:
        start_node = Node(activity, None, 0, heuristic(activity, max_score))
        heapq.heappush(open_list, (start_node.f(), start_node))

    while open_list:
        _, current_node = heapq.heappop(open_list)
        current_activity = current_node.activity

        if current_activity['valor'] > max_score:
            continue

        
        # Agregar actividad a la secuencia seleccionada
        total_duration += current_activity['duracion']
        total_value += current_activity['valor']

        if(total_value >= max_score):
            total_duration -= current_activity['duracion']
            total_value -= current_activity['valor']
            break
        
        selected_activities.append(current_activity)

        if total_duration >= min_score and total_value <= max_score:
            return selected_activities

        closed_set.add(current_activity['numero'])

        successors = generate_successors(current_activity, data)
        for successor in successors:
            if successor['numero'] not in closed_set:
                g = current_node.g + successor['duracion']
                h = heuristic(successor, current_activity['valor'])
                successor_node = Node(successor, current_node, g, h)
                heapq.heappush(open_list, (successor_node.f(), successor_node))

    return [selected_activities, total_duration, total_value]

'''


def A_star(min_score, max_score, data):
    open_list = []
    closed_set = set()

    while data:
        current_activity = data.pop(0)

        if current_activity['valor'] > max_score:
            continue

        if current_activity['valor'] >= min_score and current_activity['valor'] <= max_score:
            path = [current_activity]
            return path

        closed_set.add(current_activity['numero'])

        start_node = Node(current_activity, None, 0, heuristic(current_activity, max_score))
        heapq.heappush(open_list, (start_node.f(), start_node))
        

        successors = generate_successors(current_activity, data)
        for successor in successors:
            if successor['numero'] not in closed_set:
                g = current_activity['duracion']
                h = heuristic(successor, current_activity['valor'])
                successor_node = Node(successor, None, g, h)
                heapq.heappush(open_list, (successor_node.f(), successor_node))
        
    while open_list:
        _, current_node = heapq.heappop(open_list)
        current_activity = current_node.activity
        print(current_activity)

        if current_activity['valor'] > max_score:
            continue

        if current_activity['valor'] >= min_score and current_activity['valor'] <= max_score:
            path = get_path(current_node)
            return path
    
        closed_set.add(current_activity['numero'])

        successors = generate_successors(current_activity, data)
        for successor in successors:
            print(successor)
            if successor['numero'] not in closed_set:
                g = current_node.g + successor['duracion']
                h = heuristic(successor, current_activity['valor'])
                successor_node = Node(successor, current_node, g, h)
                heapq.heappush(open_list, (successor_node.f(), successor_node))
    
    return None
'''

# Ejemplo de uso
data = read_csv('f_3_1.csv')
min_score = 70
max_score = 100

path = A_star(min_score, max_score, data)
pprint.pprint(path)

if path[0]:
    print("Secuencia de actividades encontrada:")
    for activity in path[0]:
        print(activity['numero'])
    print(f"Valor: {path[2]}")
    print(f"Duracion: {path[1]}")
else:
    print("No se encontró una secuencia de actividades válida.")
