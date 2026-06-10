# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def valid(self, root):
        if not root:
            # condition satisfied, lowest, highest
            return [True, float('inf'), float('-inf')]

        l  = self.valid(root.left)
        r = self.valid(root.right)

        if not l[0] or not r[0]:
            return [False, min(r[1], l[1]), max(r[2], l[2])]

        if root.val >= r[1] or root.val <= l[2]:
            return [False, min(r[1], l[1], root.val), max(r[2], l[2], root.val)]

        return [True, min(r[1], l[1], root.val), max(r[2], l[2], root.val)]

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True        
        return self.valid(root)[0]
        

                
                