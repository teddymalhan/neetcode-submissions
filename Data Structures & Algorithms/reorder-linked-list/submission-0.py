# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # no monkey business
        if not head.next:
            return None
        
        dummy = ListNode(-1)
        tail = dummy

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        # now we have two halfes second which points to second half and head which points to first half
        # reversing second

        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # now prev is the head to the second half
        # now swapping the two

        first = head
        second = prev

        while second:
            t1, t2 = first.next, second.next

            first.next = second
            second.next = t1

            first = t1 
            second = t2
            