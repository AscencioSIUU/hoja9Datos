import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Función para leer el archivo y crear el grafo
def crear_grafo(archivo):
    G = nx.Graph()
    with open(archivo, 'r') as file:
        for line in file:
            origen, destino, costo = line.strip().split(', ')
            costo = int(costo)
            G.add_edge(origen, destino, weight=costo)
            G.add_edge(destino, origen, weight=costo)  # Añadir ruta simétrica
    return G

# Función para encontrar las rutas más baratas usando el algoritmo de Dijkstra
def dijkstra(graph, start):
    pq = []
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    heapq.heappush(pq, (0, start))
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous

# Función para visualizar el grafo
def ver_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Mapa de Posibles Destinos")
    plt.show()


archivo_rutas = "./src/rutas.txt"
grafo_rutas = crear_grafo(archivo_rutas)


ver_grafo(grafo_rutas)

# Encontrar las rutas más baratas desde una estación de salida
estacion_salida = "Pueblo Paleta"
distancias, rutas = dijkstra(grafo_rutas, estacion_salida)
for destino in rutas:
    ruta = rutas[destino]
    costo = distancias[destino]
    print(f"Desde {estacion_salida} hasta {destino}: {ruta} con costo {costo}")
