class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSub = nums[0]

        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0

            currSum += nums[i]
            maxSub = max(maxSub, currSum)

        return maxSub



        