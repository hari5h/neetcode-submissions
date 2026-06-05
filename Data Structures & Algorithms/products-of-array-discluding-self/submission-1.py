class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            exlusive
            [1, 2, 4, 6]
            [1, 1, 2, 8]
            [48,24,6,1]

            48, 24, 12, 8
        """

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)

        prefix[0] = suffix[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res


