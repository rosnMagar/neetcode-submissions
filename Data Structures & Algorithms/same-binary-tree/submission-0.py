# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = deque([p])
        q1 = deque([q])

        while p1 and q1:
            c1, c2 = p1.popleft(), q1.popleft() 

            if c1 == None and c2 == None:
                continue

            if c1 == None or c2 == None or c1.val != c2.val:
                return False

            else:
                p1.extend([c1.left, c1.right])
                q1.extend([c2.left, c2.right])


        return True

        

            
            






            
