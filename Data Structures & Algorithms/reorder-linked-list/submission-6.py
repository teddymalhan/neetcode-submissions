class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        # have to reverse linkedin list
        prev = None
        curr = second_half

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # now prev is the reversed list start
        second_half = prev


        first = head

        while second_half:
            t1 = first.next
            t2 = second_half.next


            first.next = second_half
            second_half.next = t1

            first = t1
            second_half = t2