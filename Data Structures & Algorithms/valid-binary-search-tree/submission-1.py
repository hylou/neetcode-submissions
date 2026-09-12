# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidNode(node, left_bound, right_bound):
            if not node:
                return True
            if left_bound >= node.val or node.val >= right_bound:
                return False
            return isValidNode(node.left, left_bound, node.val) and isValidNode(node.right, node.val, right_bound)

        return isValidNode(root, float("-infinity"), float("infinity"))