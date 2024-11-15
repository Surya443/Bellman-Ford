This project implements the Bellman-Ford shortest path algorithm in Python for a directed, weighted graph. It includes both brute-force and algebraic approaches to the Bellman-Ford algorithm and compares their performance in terms of execution time.

The Bellman-Ford algorithm calculates the shortest paths from a single source node to all other nodes in a weighted graph, even when the graph has negative weights. This project provides:

### Graph Representation: 
    A Graph class that supports directed and weighted edges.
### Adjacency Matrix Generation: 
    A function to convert the graph representation to an adjacency matrix.
### Bellman-Ford Implementations:
    Brute-Force Approach: Calculates shortest paths by iterating through all edges.
### Algebraic Approach: 
    Utilizes matrix operations to compute shortest paths.

'''
|-- graph.py           # Contains the Graph class with methods to add edges and represent the graph
|-- Bellmanford.py     # Contains the Bellman-Ford implementations (Brute-Force and Algebraic)
|-- main.py            # Main script to run the Bellman-Ford algorithm and performance comparison
|-- README.md          # This readme file
'''