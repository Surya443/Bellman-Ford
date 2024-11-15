import numpy as np

INF = float('inf')

class BellmanFord:
    
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        
    def BellmanFord_Brute(graph):        
        """
        performs brute force approach of BellmanFord algorithm.
        """             
        
        shortest_paths = {}       
        nodes = list(graph.graph.keys())        
        
        for src in nodes:
            dist = {node: float('Inf') for node in nodes}
            dist[src] = 0            
            
            for _ in range(len(nodes) - 1):
                for u, v, w in graph.get_all_edges():
                    if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            
            # Check for negative-weight cycles
            for u, v, w in graph.get_all_edges():
                if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                    print(f"Negative weight cycle detected starting from node {src}")
                    return None             
            
            shortest_paths[src] = dist
        
        return shortest_paths
    
    
    def BellmanFord_Algebraic(matrix):
        """
        matrix: Adjacency matrix of the graph.
        performs isomorphic min-plus multiplication using the algebraic approach.        
        """
        
        N = len(matrix)
        cur = matrix.copy()  

        i = 0  

        while i < 2:  
            new_cur = np.full_like(matrix, INF)  
            
            for i in range(N):
                for j in range(N):                                    
                    new_cur[i, j] = min(matrix[i, k] + cur[k, j] for k in range(N) )
            
            if np.array_equal(new_cur, cur):
                i += 1  
            else:
                i = 0              
            cur = new_cur            
        
        return cur
    
    