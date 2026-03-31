# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        p1, p2 = list1, list2

        p, res = None, None
        if p1.val < p2.val:
            p = p1
            p1 = p1.next
            res = list1
        else:
            p = p2
            p2 = p2.next
            res = list2

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p = p1
                p1 = p1.next
            else:
                p.next = p2
                p = p2
                p2 = p2.next
        
        if p1 is not None:
            p.next = p1
        elif p2 is not None:
            p.next = p2

        return res
            

                


