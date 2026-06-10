# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # calculate the ahead and behind pointers
        ahead = head

        for i in range(0, n):
            ahead = ahead.next

        # make ahead reach the end
        # make current reach the nth element from the end

        curr = head
        prev = None

        while ahead:
            ahead = ahead.next
            prev = curr
            curr = curr.next
        
        # delete the curr
        if prev:
            prev.next = curr.next
        else:
            head = curr.next

        return head
        
        