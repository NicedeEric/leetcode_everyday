## 使用dequeu实现bfs和获取每个level的list

```python
def bfs(root: TreeNode):
    queue = deque([root])
    levels = []
    while queue:
        cur_level = []
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            cur_val = cur_node.val
            cur_level.append(cur_val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        levels.append(cur_level) 

```
