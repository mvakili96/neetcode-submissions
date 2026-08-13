# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        while True:
            next_ = head.next
            
            head.next =  prev
            prev = head

            if next_ is None:
                return head
            head = next_
            
        

        