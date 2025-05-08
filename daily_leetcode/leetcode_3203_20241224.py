from typing import List

class AdjecencyList:
    def __init__(self, num_vertices):
        self.adj_list = [[] for _ in range (num_vertices)]
    
    def add_edge(self, edge: List[int]):
        node1, node2 = edge
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1) # Undirected Graph

class Solution:
    def longestPathStartAtNode(self, node_num: int, adj_list:List[List[int]] , visited: List[int]):
        max_length = 0
        
        if set(adj_list[node_num]) <= set(visited) :
            return len(visited)

        for node in adj_list[node_num]:
            # visit current node
            if node not in visited:
                visited.append(node)
                longest_path_length = self.longestPathStartAtNode(node, adj_list, visited)
                # print(longest_path_length)
                max_length = max(longest_path_length, max_length)
                visited.pop()
        return max_length

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adjListObj = AdjecencyList(len(edges1)+1)
        for edge in edges1:
            adjListObj.add_edge(edge)
        print(adjListObj.adj_list)
        visited = [0]
        max_length_node_0 = self.longestPathStartAtNode(0, adjListObj.adj_list, visited)
        print(max_length_node_0)