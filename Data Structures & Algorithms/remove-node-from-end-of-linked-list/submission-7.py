# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(0, head)
        behind, ahead = dummy, dummy

        for _ in range(n+1):
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        # now behind at node we have to remove
        behind.next = behind.next.next

        return dummy.next
