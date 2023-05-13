import csv

def cargar_actividades():
    actividades = []
    with open('instancias/f_1_0.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)  # Saltar la primera fila (encabezados)
        for fila in lector_csv:
            actividades.append({
                'subtema': int(fila[2]),
                'numero_actividad': int(fila[3]),
                'duracion': int(fila[4]),
                'valor': int(fila[5]),
                'obligatoria': bool(int(fila[7])),
                'requerimiento1': int(fila[8]),
                'requerimiento2': int(fila[9])
            })
    return actividades

def dfs(actividades, capacidad_mochila, tiempo_restante, indice_actividad, seleccionadas):
    if indice_actividad >= len(actividades) or tiempo_restante <= 0:
        return 0, []

    actividad_actual = actividades[indice_actividad]

    # Ignorar la actividad si excede el tiempo restante
    if actividad_actual['duracion'] > tiempo_restante:
        return dfs(actividades, capacidad_mochila, tiempo_restante, indice_actividad + 1, seleccionadas)

    # Ignorar la actividad si no cumple con los requisitos anteriores
    if (actividad_actual['requerimiento1'] != 0 and
            actividad_actual['requerimiento1'] > indice_actividad) or \
            (actividad_actual['requerimiento2'] != 0 and
             actividad_actual['requerimiento2'] > indice_actividad):
        return dfs(actividades, capacidad_mochila, tiempo_restante, indice_actividad + 1, seleccionadas)

    # No considerar la actividad
    no_considerar_calif, no_considerar_seleccionadas = dfs(actividades, capacidad_mochila, tiempo_restante, indice_actividad + 1, seleccionadas)

    # Considerar la actividad
    tiempo_restante -= actividad_actual['duracion']
    considerar_calif, considerar_seleccionadas = dfs(actividades, capacidad_mochila, tiempo_restante, indice_actividad + 1, seleccionadas + [actividad_actual])

    if considerar_calif + actividad_actual['valor'] > no_considerar_calif:
        return considerar_calif + actividad_actual['valor'], considerar_seleccionadas
    else:
        return no_considerar_calif, no_considerar_seleccionadas

def resolver_problema_mochila(capacidad_mochila, tiempo_disponible):
    actividades = cargar_actividades()
    calificacion, seleccionadas = dfs(actividades, capacidad_mochila, tiempo_disponible, 0, [])
    return calificacion, seleccionadas

# Parámetros de prueba
capacidad_mochila = 30
tiempo_disponible = 60

calificacion, actividades_seleccionadas = resolver_problema_mochila(capacidad_mochila, tiempo_disponible)

print(f"La calificación mínima obtenida en el tiempo disponible es: {calificacion}")
print("Actividades seleccionadas:")
for actividad in actividades_seleccionadas:
    print(f"Subtema: {actividad['subtema']}, Número de Actividad: {actividad['numero_actividad']}, Duración: {actividad['duracion']}, Valor: {actividad['valor']}")

