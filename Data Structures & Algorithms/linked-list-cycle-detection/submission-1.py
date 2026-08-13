# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while head.next is not None:
            if head.next == -1:
                return True
            next_ = head.next
            head.next = -1
            head = next_
        
        return False
        