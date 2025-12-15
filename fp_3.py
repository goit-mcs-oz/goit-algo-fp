import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Завдання 3

graph = {
    'K': ['A'],
    'E': ['A'],
    'F': ['B'],
    'R': ['B'],
    'A': ['B', 'C', 'E', 'K'],
    'B': ['A', 'C', 'F', 'R'],
    'C': ['A', 'B']
}

G = nx.Graph(graph)

G["K"]["A"]["weight"] = 10
G["E"]["A"]["weight"] = 7
G["F"]["B"]["weight"] = 12
G["R"]["B"]["weight"] = 1
G["A"]["B"]["weight"] = 3
G["A"]["C"]["weight"] = 5
G["C"]["B"]["weight"] = 2


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = []
    min_heap = [(0, start)]

    while min_heap:
        current_vertex = heapq.heappop(min_heap)[1]

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex]:
            weight = G[current_vertex][neighbor]["weight"]
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

        visited.append(current_vertex)

        print_table(distances, visited)

    return distances


print(dijkstra(graph, 'K'))

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
