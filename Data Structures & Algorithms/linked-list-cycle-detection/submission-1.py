# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we assume at least two nodes
        if head.next is None:
            return False
        
        fast, slow = head, head

        while fast and slow:
            if fast.val == slow.val and fast != head:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        
        return False