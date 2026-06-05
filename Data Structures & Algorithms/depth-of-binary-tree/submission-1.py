# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.maxDep = 0
        def depth(node, currDepth):
            # fdf
            if not node:
                return;
            self.maxDep = max(self.maxDep, currDepth)
            
            depth(node.left, currDepth+1)
            depth(node.right, currDepth+1)

        depth(root, 1)
        return self.maxDep
        