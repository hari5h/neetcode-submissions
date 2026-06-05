class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix array
        [1, 2,8,48]

        #suffix Arr
        [48, 48, 24, 6]

        prefixProdArr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefixProdArr[i] *= prefix * nums[i]
            prefix *= nums[i]
        
        suffixProdArr = [1] * len(nums)
        suffix = 1
        for i in range(len(nums)-1, -1 , -1):
            suffixProdArr[i] *= nums[i] * suffix
            suffix *= nums[i]

        res = [1] * len(nums)
        for i in range(len(nums)):
            prefix = prefixProdArr[i-1] if i-1 >= 0 else 1
            postfix = suffixProdArr[i+1] if i+1 < len(nums) else 1
            res[i] = prefix * postfix
        
        return res

        print(suffixProdArr)
        