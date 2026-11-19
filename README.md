# BiDi-Search
Object-oriented implementation of bidirectional breadth-first search of an undirected, unweighted graph.

## Algorithm

This implementation uses bidirectional breadth-first search (BFS) to find shortest paths in unweighted graphs.

Rather than searching exclusively from the source, it maintains two search frontiers:

- **Forward frontier:** Expands outward from the source.
- **Backward frontier:** Expands outward from the destination.

At each iteration, the algorithm expands the smaller frontier by one complete BFS level. When both searches discover a common vertex, their parent mappings are combined to reconstruct the shortest path.

### Features

- Shortest-path search in undirected, unweighted graphs
- Greedy frontier selection based on frontier size
- Level-by-level BFS expansion
- Custom linked-list queue implementation
- Path reconstruction using parent mappings
- No external runtime dependencies

## Installation

### Install directly from GitHub

```bash
pip install git+https://github.com/Dark-eXe/BiDi-Search.git
```

### Install from source

Clone the repository:

```bash
git clone https://github.com/Dark-eXe/BiDi-Search.git
cd BiDi-Search
```

Install the package in editable mode:

```bash
python -m pip install -e .
```

## Usage

### Basic Example

Import the graph and bidirectional search classes:

```python
from bidisearch import Graph, BiDiSearch
```

Create an undirected, unweighted graph:

```python
graph = Graph(7)

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
]

for u, v in edges:
    graph.addEdge(u, v)
```

Initialize the search and find the shortest path:

```python
search = BiDiSearch(graph)

path = search.search(0, 6)

print(path)
```

Expected output:

```text
[0, 1, 2, 3, 4, 5, 6]
```

### Handling Disconnected Vertices

If no path exists between the source and destination, `search()` returns `None`.


## Running Tests

Install pytest if necessary:

```bash
python -m pip install pytest
```

Run the test suite from the project root:

```bash
python -m pytest tests/
```
