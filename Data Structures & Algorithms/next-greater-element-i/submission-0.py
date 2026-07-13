class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        num1 = [1 2 5]
        num2 = [1 2 3 4 5] 
        res = [2 3 -1]
        """

        nums1Map = {} # num -> ind
        stack = []
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            nums1Map[nums1[i]] = i

        for num in nums2:
            # stack pop
            while stack and num > stack[-1]:
                res[nums1Map[stack[-1]]] = num
                stack.pop()
            
            # stack append
            if num in nums1Map:
                stack.append(num)


        return res







        