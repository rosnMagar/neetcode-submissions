# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            while not root:
                return [True, 0]

            left = balanced(root.left)
            right = balanced(root.right)

            d = abs(left[1] - right[1])

            if d <= 1 and left[0] and right[0]:
                return [True, max(left[1], right[1]) + 1]
            else:
                return [False, max(left[1], right[1]) + 1]

        return balanced(root)[0]



