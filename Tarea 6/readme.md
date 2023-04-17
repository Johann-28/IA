# Reconocido Simulado

<div style=justify-content:center >
Equipo: 

| Felix Yahveh Alanis Candelaria | 1947480 |
| --- | --- |
| Juan Carlos Diaz Gonzalez |  |
| Johann Joseph Velazquez Antonio | 1962111 |

</div>
---
## Instrucciones

Programar una de la siguientes metaheurísticas para el problema de ruta más corta o problema de la mochila:

- Algoritmos Genéticos
- GRASP
- Recocido Simulado* (Esta metaheurística no la vimos en clase pero es más sencilla que las anteriores)

**Parte 1 (10 puntos)**

Programar la metaheurística

**Parte 2 Extra (5 puntos)**

Hacer una comparativa con algún algoritmo informado o no informado de las tareas anteriores.

**Indicaciones Generales (Aplican a casi todas sus tareas)**
<div style= text-align:justify>
- Necesito ver gráficas de los resultados de su experimentación (boxplot, barras, etc.) y una pequeña conclusión en base a los resultados que obtuvieron, así como la descripción de las características del equipo donde corrieron los experimentos y las instancias que utilizaron.
- Necesito que agreguen la liga al repositorio con el código que usaron.
- No peguen código en su tarea , en su lugar, escríbanlo como pseudocódigo.
- Si se deciden por el problema de ruta más corta utilicen las instancias del problema de ruta más corta que crearon en la tarea 2 y obtengan el valor óptimo con su algoritmo Dijkstra que también utilizaron en la tarea 2.
- Si eligen el problema de la mochila utilicen las instancias del problema de la mochila.
- La tarea es en equipo, **máximo 3 personas**, en el reporte indiquen por favor los nombres de los integrantes, no es obligatorio usar las herramientas como overleaf o Seaborn, etc. pueden hacer el reporte en Word y las gráficas en Excel o lo que les parezca adecuado, siempre y cuando al final exporten su reporte a un PDF e incluya lo que les pido en la tarea. El código de la tarea debe de ser en Python.
</div>

-------

## Introduccion

<div style=text-align:justify>
El algoritmo del reconocimiento simulado (Simulated Annealing) se puede describir en los siguientes pasos:

- Inicializar la solución: Comenzar con una solución aleatoria para el problema de optimización.

- Establecer los parámetros: Establecer los parámetros del algoritmo, incluyendo la temperatura inicial, la función de enfriamiento y el número de iteraciones.

- Bucle principal: Repetir el siguiente proceso para un número predeterminado de iteraciones o hasta que se alcance un criterio de parada.

- __Generar una solución vecina__: Generar una solución vecina a partir de la solución actual cambiando algunos de sus componentes de manera aleatoria.

- __Evaluar la solución vecina__: Evaluar la función de costo de la nueva solución.

- __Aceptar o rechazar la solución__: Aceptar la nueva solución si su función de costo es menor que la de la solución actual. Si la función de costo es mayor, se debe calcular la probabilidad de aceptar la nueva solución, que depende de la temperatura y de la diferencia de costos entre la solución actual y la nueva solución.

- __Actualizar la temperatura__: Actualizar la temperatura utilizando una función de enfriamiento.

- __Devolver la mejor solución encontrada__: Al final del bucle principal, se devuelve la mejor solución encontrada durante todas las iteraciones.



- __Inicialización__: Se comienza con una solución aleatoria, que representa una posible combinación de objetos que se pueden colocar en la mochila.

- __Evaluación__: Se calcula el valor total de la solución actual y se compara con el mejor valor obtenido hasta el momento.

- __Generación de vecinos__: Para generar una solución vecina, se puede realizar una de las siguientes operaciones:

- __Agregar un objeto aleatorio que aún no está en la mochila__.
Eliminar un objeto aleatorio de la mochila.
Intercambiar un objeto aleatorio de la mochila por otro objeto que aún no está en la mochila.
Evaluación de vecinos: Se calcula el valor de la solución vecina y se compara con el valor de la solución actual.

- __Aceptación o rechazo de vecinos__: Si el valor de la solución vecina es mayor que el valor de la solución actual, se acepta la solución vecina como la nueva solución actual. Si el valor de la solución vecina es menor que el valor de la solución actual, se calcula la probabilidad de aceptar la solución vecina. La probabilidad de aceptación depende de la temperatura actual y de la diferencia entre los valores de las soluciones.

- __Enfriamiento__: Se disminuye la temperatura actual utilizando una función de enfriamiento.

- __Criterio de parada:__ Se repiten los pasos 3-6 hasta que se alcance un criterio de parada, como un número máximo de iteraciones o un tiempo límite.

- __Retorno:__ Se devuelve la mejor solución encontrada.

En resumen, el algoritmo del reconocimiento simulado para resolver el problema de la mochila consiste en generar soluciones aleatorias, evaluarlas y generar soluciones vecinas mediante operaciones específicas. Luego, se aceptan o rechazan las soluciones vecinas en función de una probabilidad calculada utilizando la temperatura actual y se disminuye la temperatura gradualmente. El algoritmo se repite hasta que se alcance un criterio de parada, y se devuelve la mejor solución encontrada.
</div>
GITHUB: [https://github.com/Johann-28/IA](https://github.com/Johann-28/IA)



```basic
Algoritmo reconocimiento Simulado
Inicio

importar random
importar math

# Definir los objetos (peso, valor)
objetos = [(269, 10), (95, 55), (4, 10), (60, 47), (32, 5), (23, 4), (72, 50), (80, 8), (62, 61), (65, 85), (46, 87)]

# Definir la capacidad de la mochila, la temperatura inicial y el enfriamiento
capacidad_mochila = 300
temperatura_inicial = 100
enfriamiento = 0.999

# Función para calcular el valor total de una solución
función calcular_valor(solucion, objetos)
	valor = 0
	Para i en rango de longitud(solucion)
		Si solucion[i] es igual a 1
			valor = valor + objetos[i][1]
	Retornar valor

# Función para calcular el peso total de una solución
función calcular_peso(solucion, objetos)
	peso = 0
	Para i en rango de longitud(solucion)
		Si solucion[i] es igual a 1
			peso = peso + objetos[i][0]
	Retornar peso

# Función para generar una solución vecina
función generar_vecino(solucion)
	vecino = lista(solucion)
	i = aleatorio entre 0 y longitud(vecino) - 1
	Si vecino[i] es igual a 0
		vecino[i] = 1
	Sino
		vecino[i] = 0
	Retornar vecino

# Función para aplicar el algoritmo de reconocimiento simulado
función simulated_annealing(objetos, capacidad_mochila, temperatura_inicial, enfriamiento)
	# Inicialización
	solucion_actual = [aleatorio entre 0 y 1 para _ en rango de longitud(objetos)]
	valor_actual = calcular_valor(solucion_actual, objetos)
	mejor_solucion = lista(solucion_actual)
	mejor_valor = valor_actual
	
	# Bucle principal
	temperatura = temperatura_inicial
	Mientras temperatura sea mayor que 1
		Para i en rango de 100
			# Generar una solución vecina
			vecino = generar_vecino(solucion_actual)
			
			# Evaluar la solución vecina
			valor_vecino = calcular_valor(vecino, objetos)
			peso_vecino = calcular_peso(vecino, objetos)
			
			# Aceptar o rechazar la solución vecina
			Si peso_vecino es menor o igual a capacidad_mochila y (valor_vecino es mayor que valor_actual o math.exp((valor_vecino - valor_actual) / temperatura) es mayor que un número aleatorio entre 0 y 1)
				solucion_actual = lista(vecino)
				valor_actual = valor_vecino
			
			# Actualizar la mejor solución encontrada
			Si valor_actual es mayor que mejor_valor y peso_vecino es menor o igual a capacidad_mochila
				mejor_solucion = lista(solucion_actual)
				mejor_valor = valor_actual
		
		# Enfriamiento
		temperatura = temperatura * enfriamiento
	
	Retornar mejor

Fin Algoritmo
```
---
### Parte 2
Compararemos los resultados de este algoritmo con el algoritmo informado A*, se utilizaron las mismas instancias en ambos análisis y se realizaron un número de 3 pruebas por cada instancia para poder mantener una mayor precisión y resultados, las isntancias utilizadas fueron: 



<details><summary><b>Instancias:</b></summary>
<p>
Considerando que objetos = [(peso, beneficio)]

    4 objetos
        >  objetos = [(5, 15), (3, 10), (8, 20), (6, 12)]
           capacidad_mochila = 12
           temperatura_inicial = 50
           enfriamiento = 0.995   

    10 objetos
        >  objetos = [(7, 40), (5, 35), (8, 50), (6, 10), (4, 25), (9, 45), (3, 15), (2, 5), (1, 30), (10, 20)]
           capacidad_mochila = 20
           temperatura_inicial = 100
           enfriamiento = 0.99

    10 objetos
        >  objetos = [(5, 40), (8, 35), (10, 50), (4, 10), (7, 25), (2, 45), (9, 15), (3, 5), (6, 30), (1, 20)]
           capacidad_mochila = 25
           temperatura_inicial = 50
           enfriamiento = 0.95

    20 objetos
        >  objetos = [(7, 40), (3, 60), (5, 70), (8, 10), (10, 80), (6, 20), (9, 30), (4, 50), (2, 90), (1, 100),
           (14, 80), (18, 70), (13, 40), (19, 20), (20, 30), (11, 50), (16, 60), (12, 90), (17, 10), (15, 100)]
           capacidad_mochila = 50
           temperatura_inicial = 100
           enfriamiento = 0.99

    20 objetos
        >  objetos = [(53, 85), (39, 38), (16, 7), (73, 11), (89, 88), (5, 31), (57, 34), (59, 51), (14, 50), (85, 94), (58, 66), (42, 2), (62, 60), (21, 36), (72, 25), (81, 64), (87, 10), (22, 8), (6, 53), (30, 50)]
           capacidad_mochila = 500
           temperatura_inicial = 100
           enfriamiento = 0.999
    
    23 objetos
        >   objetos = [(27, 70), (11, 85), (34, 98), (84, 25), (45, 63), (98, 99), (76, 37), (2, 45), (87, 57), (68, 77), (24, 4), (48, 62), (90, 6), (66, 16), (1, 6), (94, 15), (10, 14), (14, 58), (63, 90), (74, 36), (29, 97), (81, 85), (80, 20)]
            capacidad_mochila = 800
            temperatura_inicial = 100
            enfriamiento = 0.999

    100 objetos
        >  objetos = [(32, 10), (52, 24), (15, 15), (23, 35), (67, 7), (23, 11), (84, 78), (96, 88), (76, 34), (4, 87), 
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


</p>
</details>

```basic
Algoritmo a_estrella

    Incluir "grafo" como gr
    Incluir "math"
    Incluir "heapq"

    Funcion distancia(nodo_a, nodo_b)
        x1 = longitud(nodo_a)
        y1 = longitud(nodo_a)
        x2 = longitud(nodo_b)
        y2 = longitud(nodo_b)
        Retornar raiz_cuadrada((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
    FinFuncion

    Funcion a_estrella(nodo_inicial, nodo_final)
        abiertos = [(0, nodo_inicial)]
        cerrados = conjunto()
        padres = diccionario()
        costos = diccionario()
        ruta = diccionario()

        costos[nodo_inicial] = 0
        ruta[nodo_inicial] = [nodo_inicial]

        Mientras que abiertos no sea vacío Hacer
            costo_actual, nodo_actual = heapq.eliminar_menor(abiertos)

            Si nodo_actual = nodo_final Entonces
                Retornar ruta[nodo_actual], costos[nodo_actual]
            FinSi

            cerrados.insertar(nodo_actual)

            Para cada nodo_vecino, peso en gr.graph[nodo_actual] Hacer
                Si nodo_vecino está en cerrados Entonces
                    Continuar
                FinSi

                nuevo_costo = costos[nodo_actual] + peso
                Si nodo_vecino no está en costos o nuevo_costo < costos[nodo_vecino] Entonces
                    costos[nodo_vecino] = nuevo_costo
                    heuristica = distancia(gr.graph[nodo_vecino], gr.graph[nodo_final])
                    heapq.insertar(abiertos, (nuevo_costo + heuristica, nodo_vecino))
                    padres[nodo_vecino] = nodo_actual
                    ruta[nodo_vecino] = concatenar(ruta[nodo_actual], [nodo_vecino])
                FinSi
            FinPara
        FinMientras

        Retornar nulo
    FinFuncion

    grafica = {}

    grafo = gr.Grafo(grafica)

    Para cada g en grafica Hacer
        Para cada x en grafica Hacer
            Si g = x Entonces
                Continuar
            FinSi

            camino = a_estrella(g, x)
            Escribir("El camino mas corto de ", g, " a ", x, " es: ", camino[0], " con costo: ", camino[1])
        FinPara
    FinPara

FinAlgoritmo
```


![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e13965e-a872-4b71-836e-34dca3d0e5a2/Untitled.png)

> A*
> 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/686051e5-ae88-4880-b1ce-019d30a2ca1e/Untitled.png)

> Depth-First Search
> 
<div style = text-align:justify >
El algoritmo de reconocimiento simulado tiene un tiempo de ejecución que aumenta exponencialmente con la cantidad de objetos, por lo que cuando el número de objetos es muy grande, el tiempo de ejecución puede ser prohibitivo. Además, aunque el algoritmo puede ser útil para encontrar soluciones aproximadas a problemas de optimización combinatoria en general, se han desarrollado métodos más especializados y eficientes para problemas de la mochila con un gran número de objetos, como programación lineal entera y algoritmos genéticos.

La razón por la cual el algoritmo de reconocimiento simulado se vuelve exponencialmente ineficiente para problemas con una gran cantidad de objetos es debido a la cantidad de soluciones posibles que deben ser exploradas. Conforme la cantidad de objetos aumenta, la cantidad de soluciones posibles crece de forma exponencial, lo que implica que se deben explorar una gran cantidad de soluciones para encontrar la mejor. El algoritmo de reconocimiento simulado explora un número limitado de soluciones, y aunque es capaz de encontrar una buena solución en muchos casos, para problemas grandes la solución encontrada puede estar lejos de ser la mejor. Por lo tanto, para problemas grandes, el algoritmo de reconocimiento simulado puede ser ineficiente y puede ser necesario buscar otros enfoques más adecuados.

> 
> 
> 
> Se realizaron 3 iteraciones en cada configuración de grafo, y se graficó el promedio utilizado.
> Todas las pruebas fueron echas bajo el mismo ambiente del IDE Visual Studio Code.
> Las características del equipo en que se corrió fueron las siguientes:
> SO: Windows 11 Home Single Language x64
> Procesador: AMD Ryzen 5 5600H with Radeon Graphics            3.30 GHz
> RAM: 16,0 GB
>