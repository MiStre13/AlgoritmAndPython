class DirectedGraph:
    def __init__(self):
        self.edges = []

    def add_edge(self, start_vertex, end_vertex):
        self.edges.append((start_vertex, end_vertex))

    def remove_edge(self, start_vertex, end_vertex):
        self.edges.remove((start_vertex, end_vertex))

    def print_graph(self):
        for edge in self.edges:
            print(f"{edge[0]} -> {edge[1]}")

# Пример использования
graph = DirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(3, 0)

graph.print_graph()
