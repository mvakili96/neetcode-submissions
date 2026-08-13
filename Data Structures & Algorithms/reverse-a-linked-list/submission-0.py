# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head

        current = head.next
        head.next = None
        prev = head
        while True:
            next_ = current.next
            current.next = prev  
            prev = current
            if next_ is None:
                return current
            current = next_
        

        