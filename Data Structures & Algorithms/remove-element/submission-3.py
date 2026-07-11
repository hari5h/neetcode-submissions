class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        res = 0
        # l pointer is writer
        # r pointer is reader

        for r in range(len(nums)):
            if nums[r] != val:
                res += 1
                nums[l] = nums[r]
                l += 1

        return res




        