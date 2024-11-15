class Graph:
    def __init__(self, directed=False, weighted=False):
        # Initialize an empty graph using an adjacency list
        self.graph = {}
        self.directed = directed  
        self.weighted = weighted  

    def add_node(self, node):        
        if node not in self.graph:
            self.graph[node] = []  

    def add_edge(self, node1, node2, weight=None):
        
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        
        if self.weighted:
            if weight is None:
                raise ValueError("Weight not provided.")
            
            self.graph[node1].append((node2, weight))
            
            if not self.directed:
                self.graph[node2].append((node1, weight))
        else:
            # Unweighted graph, so just add the node without a weight (implicitly weighted as 1)
            self.graph[node1].append(node2)
            if not self.directed:
                self.graph[node2].append(node1)
                
    def get_all_edges(self):        
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if self.weighted:
                    # For weighted graph, the neighbors are tuples (v, weight)
                    edges.append((u, v[0], v[1]))
                else:
                    # For unweighted graph, the neighbors are just the nodes
                    edges.append((u, v))
        return edges

    def display(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")

