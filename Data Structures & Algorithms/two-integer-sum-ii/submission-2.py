class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            Input:
            sorted
            duplicates can exist
            -ve/0's we don't care
            Output:
            [i1, i2] 
            i1 < i2
            i1 == i2
            aleast 1 answer
            edge cases:
            []
            [i1] 
            return []
            Space and time:
            s: o(1)
            t: o(n)
            Algorithms pattern
            pointer l, r --> 0(1)
            sorted

            [1, 2, 4, 9] = 6
                L  R
        """
        l, r = 0, len(numbers) -1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r = r-1
            else:
                l = l+1
        
        return []
            



        