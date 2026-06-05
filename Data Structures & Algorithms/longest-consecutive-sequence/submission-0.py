class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res= 0
        for num in nums:
            length = 1
            if num - 1 not in numsSet:
                while num + 1 in  numsSet:
                    length +=1
                    num += 1
            res = max(length, res)

        return res

            


