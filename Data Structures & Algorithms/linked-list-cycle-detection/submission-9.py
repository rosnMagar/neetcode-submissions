# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        if not head:
            return False

        while fast.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            if not fast:
                return False
        
        return False