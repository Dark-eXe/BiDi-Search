import pytest
from src.main import Queue, Graph, BiDi_Search

def process_txt(txt):
    testGraph = None
    with open(txt, "r") as file:
        firstLine, secondLine = True, False
        for line in file:
            if firstLine:
                vertices, edges = [int(x) for x in line.split(" ")]
                testGraph = Graph(vertices)
                firstLine, secondLine = False, True
                continue

            if secondLine:
                src, dest = [int(x) for x in line.split(" ")]
                secondLine = False
                continue

            u, v = [int(x) for x in line.split(" ")]
            testGraph.addEdge(u, v)

    return (vertices, edges, src, dest, testGraph)
            

def test_queue():
    testQueue = Queue()
    assert testQueue.isEmpty()

    for i in range(5):
        testQueue.enqueue(i)
    assert not testQueue.isEmpty()
    for i in range(5):
        assert i == testQueue.dequeue()

    assert testQueue.isEmpty()

def test_bidisearch():
    vertices, edges, src, dest, testGraph = process_txt("data/1.txt")

    assert (vertices, edges) == (8, 9)
    assert (src, dest) == (0, 7)
    assert testGraph.vertices == vertices
    assert testGraph.adjList[0] == [1, 2]

    testSearch = BiDi_Search(testGraph)
    testSearch.search(src, dest)

    assert 1