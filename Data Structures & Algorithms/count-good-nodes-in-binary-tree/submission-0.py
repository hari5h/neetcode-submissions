# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, maxVal):
            if not node:
                return 0

            # pre order traversal
            # process the node

            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal, node.val)
            left_goodNode_count = dfs(node.left, maxVal)
            res += left_goodNode_count

            right_goodNode_count = dfs(node.right, maxVal)
            res += right_goodNode_count

            return res

        return dfs(root, root.val)


        