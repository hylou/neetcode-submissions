# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        head, tail = None, None
        carryover = 0

        while cur1 or cur2:
            cur1_val = cur1.val if cur1 else 0
            cur2_val = cur2.val if cur2 else 0
            sums = cur1_val + cur2_val + carryover
            carryover, dig = sums // 10, sums % 10

            cur = ListNode(val=dig)
            if not head:
                head = cur
            else:
                tail.next = cur
            tail = cur

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        if carryover > 0:
            cur = ListNode(val=carryover)
            tail.next = cur
        
        return head





        