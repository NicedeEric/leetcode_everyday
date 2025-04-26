## Pytho DFS implementation

### Assume the graph is like this. It is adjacency list

```python

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

```

### Method 1 with recursion. If the node not visited, record and move forward. If in visited, then revert back (simply return) and go next.

```python

def dfs(node, graph, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph[node], graph. visited)

    return visited

```

### Method 2 without recursion. Use stack to simulate the process. Every time a not is not inside visted, will append all its child

```python

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

```
