# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # add a dummy node to point to the head so that we could always return dummy.next
        dummy = ListNode(0, head)
        prevGroupEnd = dummy

        while True:
        
            # find current group end
            # break condition: cannot form a group with k nodes
            currentGroupEnd = prevGroupEnd
            for i in range(k):
                currentGroupEnd = currentGroupEnd.next
                if not currentGroupEnd:
                    break
            if not currentGroupEnd:
                break

            # reverse current group
            nextGroupStart = currentGroupEnd.next
            prev, cur = nextGroupStart, prevGroupEnd.next 
            for i in range(k):
                nextt = cur.next
                cur.next = prev
                prev, cur = cur, nextt

            # Iterate to next group: update groupPrev
            tmp = prevGroupEnd.next # group prev of the next group
            prevGroupEnd.next = currentGroupEnd
            prevGroupEnd = tmp


        
        return dummy.next
        

            