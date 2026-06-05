class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {} # val -> index
        
        for i,n in enumerate(nums):
            numsDict[n] = i

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in numsDict and i != numsDict[diff]:
                return [i, numsDict[diff]]
        