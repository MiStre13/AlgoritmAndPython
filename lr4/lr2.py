class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, start_vertex, end_vertex, weight):
        self.graph.append((start_vertex, end_vertex, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            start_vertex, end_vertex, weight = self.graph[i]
            i += 1
            x = self.find_parent(parent, start_vertex)
            y = self.find_parent(parent, end_vertex)

            if x != y:
                e += 1
                result.append((start_vertex, end_vertex, weight))
                self.union(parent, rank, x, y)

        return result

# Пример использования
vertices = 4
mst = KruskalMST(vertices)

mst.add_edge(0, 1, 10)
mst.add_edge(0, 2, 6)
mst.add_edge(0, 3, 5)
mst.add_edge(1, 3, 15)
mst.add_edge(2, 3, 4)

result = mst.kruskal()
for start_vertex, end_vertex, weight in result:
    print(f"{start_vertex} -- {end_vertex} == {weight}")
