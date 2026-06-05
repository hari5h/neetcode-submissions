class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        
        for i in range(len(nums)):
            leftSum = prefix[i-1] if i > 0 else 0
            rightSum = prefix[len(nums)-1] - nums[i] - leftSum
            if rightSum == leftSum:
                return i
        
        return -1

"""
nums: 1,7,3,6,5,6
pre: 1,8,11,17,22,28
             ^
0 22
1 
"""



        