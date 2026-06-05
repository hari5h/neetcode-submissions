class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TWO SUM

        Input
            unsorted
            duplicate values
            [2, n]
        Output
            index - [i, j] i != j
            one answer


        Edgecases:
            []/null element
        
        complexity
            brute force - Time:n^2 Space: constant
            sorted --> two pointers - time: nlogn space: 0
            hashmap solution nums[i]  = { target - nums[j] } n, n 
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []