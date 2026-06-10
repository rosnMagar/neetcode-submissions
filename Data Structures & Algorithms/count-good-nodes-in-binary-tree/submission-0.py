# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countHighNodes(self, root: TreeNode, g: Optional[int]):
        if not root:
            return 0
        if not g or root.val >= g:
            return 1 + self.countHighNodes(root.left, root.val) + self.countHighNodes(root.right, root.val)
        return self.countHighNodes(root.left, g) + self.countHighNodes(root.right, g)

    def goodNodes(self, root: TreeNode) -> int:
        return self.countHighNodes(root, None)


        