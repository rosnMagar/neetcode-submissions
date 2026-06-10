"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer1 = head

        order = []
        original_map = {None: None}
        
        while pointer1:
            pointer2 = Node(pointer1.val)
            original_map[pointer1] = pointer2
            pointer1 = pointer1.next

        pointer1 = head
        while pointer1:
            copy = original_map[pointer1]
            copy.next = original_map[pointer1.next]
            copy.random = original_map[pointer1.random]
            pointer1 = pointer1.next
        
        return original_map[head]
