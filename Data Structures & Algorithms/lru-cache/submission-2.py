# Use double-linked list to track both LRU and MRU nodes
# Start (psudo node) <-> node 1 (MRU) <-> node 2 ... <-> node n (LRU) <-> End (psudo node)

# Define node class
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None # double-linked

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict() # key to node

        # initial start and end node
        self.start, self.end = Node(0, 0), Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start

    def insert_to_mru(self, node):
        left, right = self.start, self.start.next
        left.next = node
        node.prev, node.next = left, right
        right.prev = node

    def remove_node(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    def get(self, key: int) -> int:
        # after get, this node should be moved to MRU
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_to_mru(self.cache[key])
            return self.cache[key].val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        # remove original node if updating
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.cap += 1
        # this node should be put to MRU
        self.cache[key] = Node(key, value)
        self.insert_to_mru(self.cache[key])
        self.cap -= 1

        # if capacity reached, remove the LRU
        while self.cap < 0: # should be -1
            lru = self.end.prev
            lru_key = lru.key
            self.remove_node(lru)
            del self.cache[lru_key]
            self.cap += 1
        
