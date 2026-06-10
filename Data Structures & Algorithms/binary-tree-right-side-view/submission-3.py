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
        q = deque([root])

        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    level.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    level.append(curr.right.val)
            if len(level):
                res.append(level[-1])
        
        return res

            