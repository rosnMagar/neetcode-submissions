# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(x) -> None:
            if not x:
                return
            invert(x.left)
            invert(x.right)

            tmp = x.left
            x.left = x.right
            x.right = tmp
        
        invert(root)

        return root
            

        
        


