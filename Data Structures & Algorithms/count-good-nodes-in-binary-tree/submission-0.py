# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def findGood(node, thres):
            if not node:
                return 0
            elif node.val >= thres:
                return 1 + findGood(node.left, node.val) + findGood(node.right, node.val)
            else:
                return findGood(node.left, thres) + findGood(node.right, thres)

        return findGood(root, -101)
        