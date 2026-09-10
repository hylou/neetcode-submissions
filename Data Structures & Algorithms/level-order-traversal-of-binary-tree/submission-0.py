# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        current_level = [root]
        current_val = []
        next_level = []
        res = []

        while current_level:
            for node in current_level:
                if node:
                    current_val.append(node.val)
                    next_level.extend([node.left, node.right])
            if current_val:
                res.append(current_val.copy())
            current_level = next_level.copy()
            current_val = []
            next_level = []

        return res
        