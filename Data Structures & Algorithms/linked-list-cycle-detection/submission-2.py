# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use fast and slow pointer approach

        fp = head
        sp = head

        while fp != None:
            
            if fp.next == None:
                return False

            fp = fp.next.next
            sp = sp.next

            if fp == sp:
                return True
        
        return False

