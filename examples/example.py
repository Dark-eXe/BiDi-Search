from bidisearch import Graph, BiDiSearch

if __name__ == "__main__":
    # Create graph
    myGraph = Graph(10)
    myGraph.addEdge(0, 1)
    myGraph.addEdge(0, 2)
    myGraph.addEdge(0, 5)
    assert 0 in myGraph.neighbors(5) # undirected graph
    myGraph.addEdge(1, 2)
    myGraph.addEdge(1, 5)
    myGraph.addEdge(2, 6)
    myGraph.addEdge(3, 7)
    myGraph.addEdge(5, 7)
    myGraph.addEdge(6, 8)
    myGraph.addEdge(7, 9)
    myGraph.addEdge(8, 9)

    # Search for path between src vertex and dest vertex
    src, dest = 0, 9
    mySearch = BiDiSearch(myGraph)
    searchResult = mySearch.search(src=src, dest=dest)

    # Print path
    if searchResult is None:
        print(f"No path found between {src} and {dest}.")
    else:
        print(f"searchResult: {searchResult}")
        print(f"Path found between {src} and {dest}:")
        print(" -> ".join([str(vertex) for vertex in searchResult]))