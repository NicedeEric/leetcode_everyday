from typing import List

class AdjecencyMatrix:
    def __init__(self, num_vertices: int):
        self.adj_matrix = [[0] * num_vertices for _ in range (num_vertices)]

    def add_edge(self, edge: List[int]):
        node1, node2 = edge
        self.adj_matrix[node1][node2] = 1
        self.adj_matrix[node2][node1] = 1

adjMatrixObj = AdjecencyMatrix(4)
edges = [[0,1],[0,2],[0,3]]
for edge in edges:
    adjMatrixObj.add_edge(edge)
print(adjMatrixObj.adj_matrix)