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

