# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # so far works for numbers with same number of digits
        carry = 0

        curr2_prev = None
        curr1_prev = None
        curr1, curr2 = l1, l2
        c1_count, c2_count = 0, 0

        while curr1 or curr2:
            c2 = curr2.val if curr2 else 0
            c1 = curr1.val if curr1 else 0
            s = c2 + c1 + carry
            v = s % 10
            carry = s // 10

            if curr1:
                curr1.val = v
                curr1_prev = curr1
                curr1 = curr1.next
                c1_count += 1

            if curr2:
                curr2.val = v
                curr2_prev = curr2
                curr2 = curr2.next
                c2_count += 1

        # same length
        if c2_count >= c1_count:
            if carry > 0:
                curr2_prev.next = ListNode(carry)
            return l2
        else:
            if carry > 0:
                curr1_prev.next = ListNode(carry)
            return l1

