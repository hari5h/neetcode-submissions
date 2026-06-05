# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        nodeList = deque([root])
        
        while len(nodeList):
            node = nodeList.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                nodeList.append(node.left)
            if node.right:
                nodeList.append(node.right)

        return root
