# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Use BFS
        res = list()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("n")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Use BFS
        vals = data.split(",")

        if vals[0] == 'n':
            return None
        
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        cur_idx = 1 # left node

        while queue:
            node = queue.popleft()
            # get left
            if vals[cur_idx] != 'n':
                node.left = TreeNode(int(vals[cur_idx]))
                queue.append(node.left)
            cur_idx += 1

            # get right
            if vals[cur_idx] != 'n':
                node.right = TreeNode(int(vals[cur_idx]))
                queue.append(node.right)
            cur_idx += 1
            
        return root

