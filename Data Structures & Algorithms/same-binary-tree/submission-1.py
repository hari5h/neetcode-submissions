# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dequeQ = deque([q])
        dequeP = deque([p])
        while dequeQ and dequeP:
            dq = dequeQ.popleft()
            dp = dequeP.popleft()

            if dp is None and dq is None:
                continue

            if not dp or not dq or dq.val != dp.val:
                return False
            
            dequeQ.append(dq.left)
            dequeQ.append(dq.right)
            dequeP.append(dp.left)        
            dequeP.append(dp.right)        
        return True






        




        return True