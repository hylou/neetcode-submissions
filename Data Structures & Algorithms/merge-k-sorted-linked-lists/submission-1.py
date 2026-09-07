# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(a: List[Optional[ListNode]], b: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not a and not b:
                return None
            elif not a:
                return b
            elif not b:
                return a
            else: # a and b, need merge
                if a.val < b.val:
                    head, prev, cur_1, cur_2 = a, a, a.next, b
                else:
                    head, prev, cur_1, cur_2 = b, b, b.next, a
                while cur_1 and cur_2:
                    if cur_1.val < cur_2.val:
                        prev.next = cur_1
                        cur_1 = cur_1.next
                    else:
                        prev.next = cur_2
                        cur_2 = cur_2.next
                    prev = prev.next
                prev.next = cur_1 if cur_1 else cur_2
                return head
        
        if not lists or len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            while len(lists) > 1:
                merged = list()
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i+1] if (i+1) < len(lists) else None
                    merged.append(mergeTwoLists(l1, l2))
                lists = merged
            return lists[0]



                


        