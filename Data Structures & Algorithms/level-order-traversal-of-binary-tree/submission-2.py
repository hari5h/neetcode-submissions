# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, depth):
            #base case
            if not node:
                return None

            if len(res) == depth:
                res.append([])

            #process the node
            res[depth].append(node.val)

            #traverse left
            dfs(node.left, depth +1)

            #traverse right
            dfs(node.right, depth +1)
        
        dfs(root, 0)
        return res
        