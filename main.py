import numpy as np
import time
from graph import Graph
from Bellmanford import BellmanFord

INF = float('inf')

def adjacency_matrix(graph):
    """Generate an adjacency matrix from the given directed graph."""
    
    # Get all nodes and sort them to maintain consistent ordering
    nodes = sorted(graph.graph.keys())
    node_count = len(nodes)       
    node_index = {node: i for i, node in enumerate(nodes)}
   
    if graph.weighted:
        adj_matrix = np.full((node_count, node_count), INF)  
        np.fill_diagonal(adj_matrix, 0)  
    else:
        adj_matrix = np.zeros((node_count, node_count), dtype=int)  # Use 0 for unweighted graphs
    
    # Populate the adjacency matrix
    for node in graph.graph:
        for neighbor in graph.graph[node]:
            if graph.weighted:
                neighbor_node, weight = neighbor
                adj_matrix[node_index[node], node_index[neighbor_node]] = weight
            else:
                adj_matrix[node_index[node], node_index[neighbor]] = 1      
                
    
    return adj_matrix, node_index
graph = Graph(directed=True, weighted=True)
edges = [(0, 1, 10), (0, 9, 5), (0, 8, 4), (0, 11, 9),
        (1, 9, 11), (1, 10, 11), (1, 3, 1), (1, 4, 10), (1, 19, 5),
        (2, 18, 12),
        (3, 10, 13), (3, 13, 13), (3, 7, 11), 
        (4, 7, 7), (4, 5, 6),
        (5, 6, 12), (5, 12, 12), 
        (6, 16, 11), (6, 14, 15),
        (7, 8, 13), (7, 16, 11), 
        (8, 13, 11),
        (9, 19, 10), (9, 20, 9),
        (10, 3, 13), (10, 13, 11), (10, 8, 11),
        (11, 0, 5), (11, 21, 5),
        (12, 18, 11),
        (13, 16, 9),
        (14, 23, 9), (14, 15, 5),
        (15, 22, 15), (15, 23, 7),
        (16, 21, 7),
        (17, 22, 11),
        (18, 17, 11),
        (19, 2, 12),
        (20, 14, 15),
        (21, 20, 8),
        (22, 17, 11),
        (23, 14, 8)
    ]

    # Adding the edges to the graph
for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])


# graph = Graph(directed=True, weighted=True)  
# graph.add_edge('A', 'B', 6)
# graph.add_edge('A', 'C', 3)
# graph.add_edge('C', 'D', 1)
# graph.add_edge('D', 'B', 1)
# graph.add_edge('C', 'B', 4)

adj_matrix, node_mapping = adjacency_matrix(graph)

print("Adjacency Matrix:")
print(adj_matrix)

print('----------------------------------------------------------------------------')

print("\nNode to Index Mapping:")
print(node_mapping)

print('----------------------------------------------------------------------------')

start_brute = time.time()
l = BellmanFord.BellmanFord_Brute(graph)
end_brute = time.time()

start_algebraic = time.time()
l2 = BellmanFord.BellmanFord_Algebraic(adj_matrix)
end_algebraic = time.time()

for i in l:
    print(i, l[i])

print('----------------------------------------------------------------------------')

print(l2)

print('----------------------------------------------------------------------------')

print(f"Time taken for brute force approach: {float(end_brute - start_brute)} seconds \n Time taken for algebraic approach: {float(end_algebraic - start_algebraic)} seconds")