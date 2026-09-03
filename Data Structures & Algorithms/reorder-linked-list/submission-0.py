# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list into two using fast and slow pointer
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # move one more step for slow so that the first half will be longer
        # slow now is the starting of the second half
        slow_next = slow.next
        slow.next = None # cut off the list

        # Reverse the second half
        prev, cur = None, slow_next
        while cur:
            c_next = cur.next
            cur.next = prev
            prev, cur = cur, c_next
        

        # New prev is the head of the second half
        first, second = head, prev

        # construct the list
        while second:
            first_next = first.next
            second_next = second.next

            # reorg
            first.next = second
            second.next = first_next
            
            # move
            first = first_next
            second = second_next





        