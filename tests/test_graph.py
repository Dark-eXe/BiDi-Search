from bidisearch import Graph

def test_graph():
    testGraph = Graph(10)
    assert testGraph.vertices == 10
    assert not testGraph.adjList[testGraph.vertices - 1]

    testGraph.addEdge(0, 9)
    assert testGraph.adjList[0] == [9] == testGraph.neighbors(0)
    assert testGraph.adjList[9] == [0] == testGraph.neighbors(9)