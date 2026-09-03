"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # create all node copy, and create map from old node to new node
        old_to_new = dict()
        cur = head
        while cur:
            copy_cur = Node(x=cur.val, next=None, random=None)
            old_to_new[cur] = copy_cur
            cur = cur.next

        # assign pointer to new copy nodes based on the mapping
        cur = head
        while cur:
            copy_cur = old_to_new[cur]
            copy_cur.next = old_to_new[cur.next] if cur.next else None
            copy_cur.random = old_to_new[cur.random] if cur.random else None
            cur = cur.next
        
        return old_to_new[head] # return the head


        