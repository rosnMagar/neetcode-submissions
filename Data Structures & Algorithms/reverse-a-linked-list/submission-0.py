# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  rl = []
        #  [h] -> [n1] -> [n2]
        #  [n2] -> [n1] -> [h]
        #  tail = head
        #  node2 = n1
        #  node2.next = tail
        #  node3 = n2
        #  node3.next = node2

        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev












        
            