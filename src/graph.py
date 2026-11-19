class Graph:
    """Adjacency list based implementation of graph data structure where each vertex is referred to by integer in [0, self.vertices)"""
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjList = [[] for vertex in range(vertices)]

    def addEdge(self, u: int, v: int):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def neighbors(self, vertex: int) -> list[int]:
        return self.adjList[vertex]