# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case
        if not root:
            return None

        left_comp = self.invertTree(root.left)
        right_comp = self.invertTree(root.right)

        root.left = right_comp
        root.right = left_comp

        return root

        