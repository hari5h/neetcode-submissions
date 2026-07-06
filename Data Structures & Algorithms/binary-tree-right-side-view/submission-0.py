# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deque = collections.deque()
        deque.append(root)
        res = []

        while deque:
            qlen = len(deque)
            rightSide = None
            for i in range(qlen): #drain the level
                node = deque.popleft()

                if node:
                    rightSide = node.val
                    deque.append(node.left)
                    deque.append(node.right)

            if rightSide:
                res.append(rightSide)

        return res
                






        return res
        