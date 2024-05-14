class DirectedGraph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.inc_matrix = [[0 for _ in range(edges)] for _ in range(vertices)]

    def add_edge(self, edge_index, start_vertex, end_vertex):
        self.inc_matrix[start_vertex][edge_index] = 1
        self.inc_matrix[end_vertex][edge_index] = -1

    def remove_edge(self, edge_index):
        for i in range(self.vertices):
            if self.inc_matrix[i][edge_index] != 0:
                self.inc_matrix[i][edge_index] = 0

    def print_graph(self):
        for row in self.inc_matrix:
            print(row)

# Пример использования
graph = DirectedGraph(4, 3)
graph.add_edge(0, 0, 1)
graph.add_edge(1, 0, 2)
graph.add_edge(2, 3, 0)

graph.print_graph()
