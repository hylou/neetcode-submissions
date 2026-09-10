# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()

        current_level = deque()
        current_level.append(root)
        res = []

        while current_level:
            res.append(current_level[0].val)
            current_num = len(current_level)
            for _ in range(current_num):
                node = current_level.popleft()
                if node.right: # right first
                    current_level.append(node.right)
                if node.left:
                    current_level.append(node.left)
        return res
        