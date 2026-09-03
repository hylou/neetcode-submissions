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

        # create nodes and link them
        # for each (new, old) node pair, we switch the following pointers:
        # new.random = old.random, old.random = new
        # After that, we could use new.random.random to map to it's random pointer

        cur = head
        pre_new = None
        
        while cur:
            new = Node(x=cur.val)
            new.random = cur.random
            cur.random = new

            # assign
            if pre_new:
                pre_new.next = new

            cur = cur.next
            pre_new = new
        
        # assign random
        cur = head.random
        while cur:
            if cur.random:
                cur.random = cur.random.random
            cur = cur.next

        return head.random



        