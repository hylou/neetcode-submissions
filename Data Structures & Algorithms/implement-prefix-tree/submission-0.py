# define a trie node
class TrieNode:
    def __init__(self):
        self.node_map = dict()
        self.eow = False # indicate if this is the end of word

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.node_map:
                cur.node_map[char] = TrieNode()
            cur = cur.node_map[char]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.node_map:
                return False
            cur = cur.node_map[char]
        return cur.eow

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.node_map:
                return False
            cur = cur.node_map[char]
        return True
        