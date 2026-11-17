from typing import Any

class QueueNode:
    """Linked list node"""
    def __init__(self, x):
        self.val = x
        self.next = None


class Queue:
    """Manual implementation for queue data structure using linked lists and pointers to head and tail."""

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__length = 0

    def isEmpty(self) -> bool:
        return self.__head is None

    def enqueue(self, x) -> None:
        newNode = QueueNode(x)

        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode

        self.__length += 1

    def dequeue(self) -> Any | None:
        if self.isEmpty():
            return None

        popVal = self.__head.val
        self.__head = self.__head.next

        if self.isEmpty():
            self.__tail = None

        self.__length -= 1
        return popVal

    def __len__(self):
        return self.__length

class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjList = [[] for vertex in range(vertices)]

    def addEdge(self, u: int, v: int):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def neighbors(self, vertex: int) -> list[int]:
        return self.adjList[vertex]

class BiDi_Search:
    """Bidirectional breadth-first search on given graph, source, and destination using greedy frontier expansion."""

    def __init__(self, graph: Graph):
        """Given a Graph object with vertices and an adjacency list, initializes essential data structures for bidirectional search including:
            - visited arrays
            - parent arrays
            - search queues
        """
        self.graph = graph
        self.clean()

    def search(self, src, dest) -> list | None:
        """Search for intersection, returning path in list representation or None if no path found"""
        self.src, self.dest = src, dest
        self.clean()

        self.queue_src.enqueue(self.src)
        self.visited_src[src] = True
        self.__levelCount_src = 1

        self.queue_dest.enqueue(self.dest)
        self.visited_dest[dest] = True
        self.__levelCount_dest = 1

        while not self.queue_src.isEmpty() or not self.queue_dest.isEmpty():
            intersectionFound = self._expand(frontier=self._nextFrontier())
            if intersectionFound is not None:
                return self._reconstructPath(intersection=intersectionFound)
        return None

    def _expand(self, frontier: str) -> int | None:
        """Search an entire level/depth for an intersection given on either 'src' or 'dest' frontier"""
        if frontier != "src" and frontier != "dest":
            raise ValueError(f"Arg 'frontier' must either be 'src' or 'dest'...\
                              your 'frontier' value: {frontier}")

        nextLevel = 0
        if frontier == "src":
            for _ in range(self.__levelCount_src):
                current = self.queue_src.dequeue()
                for neighbor in self.graph.neighbors(current):
                    if not self.visited_src[neighbor]:
                        self.parent_src[neighbor] = current
                        self.visited_src[neighbor] = True
                        if self.visited_dest[neighbor]: # INTERSECTION
                            return neighbor
                        self.queue_src.enqueue(neighbor)
                        nextLevel += 1
            self.__levelCount_src = nextLevel
        else:
            for _ in range(self.__levelCount_dest):
                current = self.queue_dest.dequeue()
                for neighbor in self.graph.neighbors(current):
                    if not self.visited_dest[neighbor]:
                        self.parent_dest[neighbor] = current
                        self.visited_dest[neighbor] = True
                        if self.visited_src[neighbor]: # INTERSECTION
                            return neighbor
                        self.queue_dest.enqueue(neighbor)
                        nextLevel += 1
            self.__levelCount_dest = nextLevel
        

    def _nextFrontier(self) -> str:
        """Returns either 'src' or 'dest'"""
        if self.__levelCount_src == 0 and self.__levelCount_dest == 0:
            raise RuntimeError("Both src and dest queues for the next level are empty!")
        if self.__levelCount_src == 0:
            return "dest"
        if self.__levelCount_dest == 0:
            return "src"
        
        return "src" if self.__levelCount_src <= self.__levelCount_dest else "dest"

    def _reconstructPath(self, intersection: int) -> list | None:
        """Returns list representation of found path: [src, ..., intersection, ..., dest]"""
        if intersection not in range(self.graph.vertices):
            raise ValueError(f"Arg 'intersection' must be in valid vertex range: [0, {self.graph.vertices})...\
                             your 'intersection' value: {intersection}")

        path = [intersection]
        current = intersection
        while self.parent_src[current] is not None:
            current = self.parent_src[current]
            path.append(current)
        path.reverse()
        current = intersection
        while self.parent_dest[current] is not None:
            current = self.parent_dest[current]
            path.append(current)
            
        return path

    def clean(self) -> None:
        """Cleans variables, allowing for new src and dest searches"""
        self.visited_src = [False for vertex in range(self.graph.vertices)]
        self.parent_src = [None for vertex in range(self.graph.vertices)]
        self.queue_src = Queue()

        self.visited_dest = [False for vertex in range(self.graph.vertices)]
        self.parent_dest = [None for vertex in range(self.graph.vertices)]
        self.queue_dest = Queue()

if __name__ == "__main__":
    print("Run pytest for tests/test_bidisearch.py")
