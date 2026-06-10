# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = [[root]]
        res = [[root.val]]

        i = 0
        while i < len(nodes):
            level = nodes[i]
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if len(next_level):
                nodes.append(next_level)
                res.append([n.val for n in next_level])
            
            i += 1 
       
        return res

