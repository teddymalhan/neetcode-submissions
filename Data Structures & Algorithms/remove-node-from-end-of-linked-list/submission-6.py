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
        ahead, behind = dummy, dummy
        # ahead is n boxes ahead
        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next
        return dummy.next
