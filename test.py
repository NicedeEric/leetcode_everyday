graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(graph, node):
    visited = set()
    stack = [node]
    traversal = []

    while len(stack) > 0:
        cur = stack.pop()
        if cur not in visited:
            visited.add(cur)
            traversal.append(cur)
            stack.extend(reversed(graph[cur]))
    
    return traversal

order = dfs(graph1, 'A')
print(order)

