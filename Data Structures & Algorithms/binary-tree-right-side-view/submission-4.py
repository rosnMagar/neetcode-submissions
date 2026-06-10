# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # going to do a BFS
        if not root:
            return []
        res = [root.val]
        q = [[root]]

        i = 0
        while i < len(q):
            level_values = []
            level_nodes = []
            for curr in q[i]:
                if curr.left:
                    level_nodes.append(curr.left)
                    level_values.append(curr.left.val)
                if curr.right:
                    level_nodes.append(curr.right)
                    level_values.append(curr.right.val)
            if len(level_nodes):
                res.append(level_values[-1])
                q.append(level_nodes)
            i += 1
        return res

            