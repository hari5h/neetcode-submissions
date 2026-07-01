# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return inverted the subtree

        #base case
        if not root:
            return None

        #recurse left
        left_inv = self.invertTree(root.left)

        #recurse right
        right_inv = self.invertTree(root.right)
        
        #process the node

        root.left = right_inv
        root.right = left_inv

        return root
        