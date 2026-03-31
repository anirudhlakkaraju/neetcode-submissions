# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Create a deep copy of the list
        dummy = ListNode(0)
        copy_tail = dummy
        curr = head
        n = 0

        while curr:
            copy_tail.next = ListNode(curr.val)
            copy_tail = copy_tail.next
            curr = curr.next
            n += 1

        # Step 2: Reverse the copied list
        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        
        # Step 3: Merge original and reversed lists alternately
        p = head
        p1 = head.next
        p2 = prev
        for i in range(n - 1):
            if i % 2 == 0:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        p.next = None

        

            


        