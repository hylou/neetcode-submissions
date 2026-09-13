# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # for each node, need to compare:
        # 1. self.val + left + right
        # 2. self.val + max(left, right)
        # (no need to compare without self, which is already calculated in recursive)
        # use root itself as the initial path
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            # get both side's max first
            left = dfs(node.left)
            right = dfs(node.right)
            left_cap = max(left, 0)
            right_cap = max(right, 0)

            # we need to check if include both will reach to max
            # however, we should only output the sum that don't include both, since it couldn't continue to form a path
            # we don't need to add them if the max is less than 0
            res = max(res, node.val + left_cap + right_cap)
            return node.val + max(left_cap, right_cap)

        dfs(root)
        return res
            
        