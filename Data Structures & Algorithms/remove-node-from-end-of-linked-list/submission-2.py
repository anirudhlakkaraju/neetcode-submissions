# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast, slow = head, head
        prev = None
        i = 1

        while fast.next:
            if i >= n:
                prev = slow
                slow = slow.next
            fast = fast.next
            i += 1
        
        if prev is None:
            if slow.next is None:
                return None
            head = slow.next
            return head
        
        prev.next = slow.next

        return head