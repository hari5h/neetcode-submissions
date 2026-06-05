class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         res = max(res, (r-l) * min(heights[l], heights[r]))

        # return res
        
        l, r = 0, len(heights)-1
        while l < r:
            res = max(res, (r-l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return res
            
        

        