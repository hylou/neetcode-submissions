# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # classical solution
        # build a value-index first: O(n)
        idx_map = {inorder[i]: i for i in range(len(inorder))}

        # need to record cnrrent working node, start for global root
        self.pre_idx = 0

        # building tree from a slice of array: O(n)
        def buildFromIdx(left, right):
            # if the slice is not exist
            if left > right:
                return None

            root_val = preorder[self.pre_idx]

            # next one is the left tree root idx
            self.pre_idx += 1

            # build node
            root = TreeNode(root_val)

            # get root at inorder
            root_idx = idx_map[root_val]

            # build left and right tree recursively
            root.left = buildFromIdx(left, root_idx - 1)
            root.right = buildFromIdx(root_idx + 1, right)

            return root

        return buildFromIdx(0, len(preorder)-1)

