# need to define node and linked list
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        # for freq
        self.freq = 1

        # for linking
        self.head = None
        self.tail = None

class LinkedList:
    def __init__(self):
        # dummy head and tail
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head
        
        # need to record the size
        self.size = 0
    
    # add as the most recently used node (at right)
    def push_to_right(self, node):
        # get the left node
        left = self.tail.left

        # link: left <-> node <-> self.right
        left.right = node
        node.left, node.right = left, self.tail
        self.tail.left = node

        # set size
        self.size += 1

    # remove node
    def pop(self, node):
        # get left and right
        left, right = node.left, node.right
        # link left <-> right
        left.right, right.left = right, left
        # make the node being orphan
        node.left, node.right = None, None
        # set size
        self.size -= 1

    # remove least recently used node (at left)
    def pop_from_left(self):
        # only pop if there's at least a node, excluding head/tail
        if self.size == 0:
            return None
        # get the node
        node = self.head.right
        self.pop(node)
        return node

from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.least_freq = 0
        self.node_map = dict()
        self.list_map = defaultdict(LinkedList)

    def update_count(self, node):
        # remove the node
        freq = node.freq
        self.list_map[freq].pop(node)

        # if the list is empty, update least_freq
        if freq == self.least_freq and self.list_map[freq].size == 0:
            self.least_freq += 1
        
        # update the node
        node.freq += 1
        self.list_map[node.freq].push_to_right(node)


    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.update_count(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0 and self.least_freq == 0:
            return # the capacity is zero at beginning
        
        # check if we are updating node
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.update_count(node)
            return

        # if we are adding new node
        # check if the capacity is full, if it is, pop the LFU
        if self.capacity == 0:
            node = self.list_map[self.least_freq].pop_from_left()
            self.node_map.pop(node.key)
            self.capacity += 1
        
        # add new node
        node = ListNode(key, value)
        self.node_map[key] = node
        self.list_map[1].push_to_right(node)
        self.capacity -= 1
        self.least_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)