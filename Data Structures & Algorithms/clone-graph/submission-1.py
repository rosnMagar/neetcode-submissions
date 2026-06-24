"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        queue = []
        cpy = Node(node.val)
        queue.append((node, cpy))
        visited = {node: cpy}

        while queue:
            nod, c = queue.pop(0)
            for n in nod.neighbors:
                if n not in visited:
                    newNode = Node(n.val)
                    visited[n] = newNode
                    queue.append((n, newNode))
                c.neighbors.append(visited[n])
        
        return cpy