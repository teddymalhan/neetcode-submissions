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

        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        
        # now there's a n difference between fast and slow
        prev = None
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next