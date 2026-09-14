def getIndex(char):
    return ord(char) - ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0 # how many words use this node
    
    def addWord(self, word, idx):
        cur = self
        cur.refs += 1
        for char in word:
            char_idx = getIndex(char)
            if not cur.children[char_idx]:
                cur.children[char_idx] = TrieNode()
            cur = cur.children[char_idx]
            cur.refs += 1
        cur.idx = idx # tag at the end of word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add wods to Trie
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        # dfs for searching
        def dfs(r, c, node):
            # out of bound, cell visited, or not in the trie
            if r < 0 or r >= ROWS or \
            c < 0 or c >= COLS or \
            board[r][c] == '*' or \
            not node.children[getIndex(board[r][c])]:
                return 0

            current_char = board[r][c]
            board[r][c] = '*' # visited
            next_node = node.children[getIndex(current_char)]
            found = 0

            # if found
            if next_node.idx != -1: # get eow
                res.append(words[next_node.idx])
                next_node.idx = -1 # avoid double finding
                found += 1

            # dfs
            found += dfs(r+1, c, next_node)
            found += dfs(r-1, c, next_node)
            found += dfs(r, c+1, next_node)
            found += dfs(r, c-1, next_node)

            # backtrack (reverse)
            board[r][c] = current_char
            node.refs -= found

            # if no more new words, prune that tree
            if not next_node.refs:
                node.children[getIndex(current_char)] = None
            return found

        for r in range(ROWS):
            for c in range(COLS):
                root.refs -= dfs(r, c, root)
        
        return res




        