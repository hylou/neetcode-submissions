class TrieNode:
    def __init__(self):
        self.node_map = dict()
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.node_map:
                cur.node_map[char] = TrieNode()
            cur = cur.node_map[char]
        cur.eow = True
        

    def search(self, word: str) -> bool:
        
        # use dfs for wildcard
        def dfs(idx, node):
            cur = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    # dfs
                    for next_char in cur.node_map:
                        if dfs(i+1, cur.node_map[next_char]):
                            return True
                    return False

                if char not in cur.node_map:
                    return False
                cur = cur.node_map[char]
            return cur.eow

        return dfs(0, self.root)

        
