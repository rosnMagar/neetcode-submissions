# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node, l) -> int:
            if not node:
                return l

            left = traverse(node.left, l + 1)
            right = traverse(node.right, l + 1)

            return max(left, right)

        return traverse(root, 0)

