# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode() 
        curr = res

        while list1 and list2:
            v1, v2 = list1.val, list2.val

            if v1 <= v2:
                curr.next = ListNode(v1)
                list1 = list1.next
            else:
                curr.next = ListNode(v2)
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2

        return res.next
            