# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first idea: let's do sanity checks
        if not head:
            return []
        
        # now simple aspect
        prev = None

        while head.next is not None:
            prev = head
            head = head.next
            head.next = prev
        
        return head

        

