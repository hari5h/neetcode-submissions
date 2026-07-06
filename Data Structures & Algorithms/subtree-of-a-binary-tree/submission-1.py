# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        leftTree = self.isSubtree(root.left, subRoot)
        if leftTree:
            return True
        
        rightTree = self.isSubtree(root.right, subRoot)
        if rightTree:
            return True

        return False



    def isSameTree(self, tree1, tree2):

        #base case:
        if not tree1 and not tree2:
            return True

        if tree1 and not tree2:
            return False
        
        if tree2 and not tree1:
            return False

        #post order traversal
        left_node = self.isSameTree(tree1.left, tree2.left)
        right_node = self.isSameTree(tree1.right, tree2.right)

        #process node
        isSame = tree1.val == tree2.val

        return isSame and right_node and left_node




        