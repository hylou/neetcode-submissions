# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        prev, cur, nextt = None, head, head.next
        while length > n:
            prev, cur, nextt = cur, nextt, nextt.next
            length -= 1
        if prev:
            prev.next = nextt
        else:
            return nextt # if prev is none, means we are removing the first item
        return head
        