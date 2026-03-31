# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # pretty simple
        # just run the loop from head for n times
        # two pointers keep on iterating until the first pointer of n turns ahead has a next of 0
        # keep prev for the slower pointer and have it point to the node after the curr
        # done?
        if not head.next:
            return None

        behind, ahead = head, head

        for _ in range(n + 1):
            if not ahead:
                return None 
            ahead = ahead.next

        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next
        
        return head
