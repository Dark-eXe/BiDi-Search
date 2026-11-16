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

def test_bidisearch_1():
    vertices, edges, src, dest, testGraph = process_txt("data/1.txt")

    assert (vertices, edges) == (8, 9)
    assert (src, dest) == (0, 7)
    assert testGraph.vertices == vertices
    assert testGraph.neighbors(0) == [1, 2]

    testSearch = BiDi_Search(testGraph)
    possible_paths = []
    possible_paths.append([0, 2, 4, 5, 6, 7])
    possible_paths.append([0, 1, 3, 5, 6, 7])
    possible_paths.append([0, 2, 3, 5, 6, 7])
    assert testSearch.search(src, dest) in possible_paths

def test_bidisearch_2():
    vertices, edges, src, dest, testGraph = process_txt("data/2.txt")
    
    assert (vertices, edges) == (10, 8)
    assert (src, dest) == (0, 9)
    assert testGraph.vertices == vertices
    assert testGraph.neighbors(0) == [1, 2]

    testSearch = BiDi_Search(testGraph)
    assert testSearch.search(src, dest) is None

def test_bidisearch_3():
    vertices, edges, src, dest, testGraph = process_txt("data/3.txt")
        
    assert (vertices, edges) == (12, 14)
    assert (src, dest) == (0, 11)
    assert testGraph.vertices == vertices
    assert testGraph.neighbors(0) == [1, 5, 7]

    testSearch = BiDi_Search(testGraph)
    shortest_path = [0, 5, 6, 11]
    assert testSearch.search(src, dest) == shortest_path

def test_bdidisearch_4():
    vertices, edges, src, dest, testGraph = process_txt("data/4.txt")
        
    assert (vertices, edges) == (16, 15)
    assert (src, dest) == (0, 15)
    assert testGraph.vertices == vertices
    assert testGraph.neighbors(0) == list(range(1, 9))

    testSearch = BiDi_Search(testGraph)
    shortest_path = [0, 1, 9, 10, 11, 12, 13, 14, 15]
    assert testSearch.search(src, dest) == shortest_path