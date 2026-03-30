# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headNewList = ListNode(-1)
        tail = headNewList

        curr1, curr2 = list1, list2

        # three cases
        while curr1 and curr2:
            # compare the values and iterate pointers based on that
            # choose how to handle conflicts based on picture
            if curr1.val < curr2.val:

                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            
            tail = tail.next
        
        # curr2 got exhausted
        if curr1:
            # set the curr_to_new_list to curr1 instead
            tail.next = curr1
        if curr2:
            tail.next = curr2

        
        return headNewList.next

            

