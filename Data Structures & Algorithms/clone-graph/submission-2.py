"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None 
        res = Node(node.val, [])
        visit = {node: res}
        q = deque([(node, res)])

        while q:
            n, child = q.popleft()
            for nbr in n.neighbors:
                if nbr not in visit:
                    tmp = Node(nbr.val)
                    visit[nbr] = tmp
                    q.append((nbr, tmp))
                child.neighbors.append(visit[nbr])
        
        return res

