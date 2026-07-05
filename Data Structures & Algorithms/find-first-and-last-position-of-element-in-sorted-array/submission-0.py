class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftBias = self.binarySearch(nums, target, True)
        rightBias = self.binarySearch(nums, target, False)

        return [leftBias, rightBias]
    
    def binarySearch(self, nums, target, leftBias):
        l = 0
        r = len(nums)-1
        res = -1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                res = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
            
        return res
        