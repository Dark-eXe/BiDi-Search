class QueueNode:
    """Linked list node"""
    def __init__(self, x):
        self.val = x
        self.next = None


class Queue:
    """Manual implementation for queue data strucutre using linked lists and pointers to head and tail."""

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

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

    def dequeue(self) -> any | None:
        if self.isEmpty():
            return None

        popVal = self.__head.val
        self.__head = self.__head.next

        if self.isEmpty():
            self.__tail = None

        return popVal

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
        ...

    def _expand(self, frontier: str = "src") -> int | None:
        """Search an entire level/depth for an intersection given on either 'src' or 'dest' frontier"""
        pass

    def _nextFrontier(self) -> str:
        """Returns either 'src' or 'dest'"""
        pass

    def _reconstructPath(self, intersection) -> list | None:
        """Returns list representation of found path: [src, ..., intersection, ..., dest]"""
        pass

    def clean(self) -> None:
        """Cleans variables, allowing for new src and dest searches"""
        self.visited_src = [False for vertex in range(self.graph.vertices)]
        self.parent_src = [None for vertex in range(self.graph.vertices)]
        self.queue_src = Queue()

        self.visited_dest = [False for vertex in range(self.graph.vertices)]
        self.parent_dest = [None for vertex in range(self.graph.vertices)]
        self.queue_dest = Queue()