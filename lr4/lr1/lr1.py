class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, start, end):
        self.adj_matrix[start][end] = 1

    def remove_edge(self, start, end):
        self.adj_matrix[start][end] = 0

    def print_graph(self):
        for row in self.adj_matrix:
            print(row)

    def read_graph_from_file(self, filename):
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                row = [int(x) for x in line.split()]
                self.adj_matrix[i] = row

# Пример использования
graph = DirectedGraph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(3, 0)

graph.print_graph()

# Запись графа в файл
with open('graph.txt', 'w') as file:
    for row in graph.adj_matrix:
        file.write(' '.join(str(cell) for cell in row) + '\n')

# Чтение графа из файла
new_graph = DirectedGraph(4)
new_graph.read_graph_from_file('graph.txt')
new_graph.print_graph()
