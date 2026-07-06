# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque = collections.deque()
        deque.append(root)
        res = []

        while deque:
            qlen = len(deque)
            level = []

            for i in range(qlen):
                node = deque.popleft()
                if node:
                    level.append(node.val)
                    deque.append(node.left)
                    deque.append(node.right)

            if level:
                res.append(level)

        return res




        