# Represent graph using adjacency list. 
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)   
    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("Adjacency List:")
g.display()
# Implement BFS. 
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("BFS Traversal:")
g.bfs(0)

# Implement DFS. 
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(vertex)
        print(vertex, end=" ")

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("DFS Traversal:")
g.dfs(0)

#Detect cycle in graph. 
# Shortest path problem. 
# Check graph connectivity.
  