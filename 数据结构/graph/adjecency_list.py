from typing import List

class AdjecencyList:
    def __init__(self, num_vertices):
        print(num_vertices)
        self.adj_list = [[] for _ in range (num_vertices)]
    
    def add_edge(self, edge: List[int]):
        node1, node2 = edge
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1) # Undirected Graph
    
