# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # traverse through the list using fast and slow pointer to find out the middle of the ll
        fast_p = head.next
        slow_p = head

        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        
        first = head
        second = slow_p.next
        
        slow_p.next = None

        # reverse the second portion
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev

        # list is reversed for the second part
        # now join the two lists
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        