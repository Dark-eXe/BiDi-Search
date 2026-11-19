from .queue import Queue
from .graph import Graph

class BiDiSearch:
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