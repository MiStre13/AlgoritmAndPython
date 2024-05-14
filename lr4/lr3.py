from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def is_connected(self):
        visited = [False] * len(self.graph)
        
        def dfs(node):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for node in self.graph:
            if len(self.graph[node]) > 0:
                start_node = node
                break
        
        dfs(start_node)
        
        for i in range(len(self.graph)):
            if len(self.graph[i]) > 0 and not visited[i]:
                return False
        
        return True
    
    def has_eulerian_cycle(self):
        if not self.is_connected():
            return False
        
        for node in self.graph:
            if len(self.graph[node]) % 2 != 0:
                return False
        
        return True

# Пример использования
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

if g.has_eulerian_cycle():
    print("Граф содержит Эйлеров цикл")
else:
    print("Граф не содержит Эйлеров цикл")
