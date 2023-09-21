import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node,neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)

    print("Найден следующий лучший маршрут с ценностью".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

nodes = ["A", "B", "C", "D", "E", "F", "G", "J", "K", "M","N","O","P","R","Q"]
init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["A"]["D"] = 78
init_graph["A"]["E"] = 47
init_graph["A"]["J"] = 96
init_graph["A"]["P"] = 73
init_graph["A"]["F"] = 28
init_graph["A"]["B"] = 14
init_graph["B"]["F"] = 45
init_graph["B"]["N"] = 73
init_graph["B"]["C"] = 29
init_graph["C"]["F"] = 41
init_graph["C"]["N"] = 70
init_graph["D"]["E"] = 56
init_graph["D"]["J"] = 31
init_graph["E"]["J"] = 72
init_graph["F"]["Q"] = 44
init_graph["F"]["M"] = 40
init_graph["F"]["N"] = 55
init_graph["G"]["N"] = 9
init_graph["J"]["K"] = 35
init_graph["J"]["O"] = 30
init_graph["K"]["P"] = 20
init_graph["O"]["P"] = 39
init_graph["P"]["Q"] = 47
init_graph["N"]["M"] = 48
init_graph["R"]["M"] = 32
init_graph["R"]["Q"] = 19


graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="A")
print_result(previous_nodes, shortest_path, start_node="A", target_node="Q")




































