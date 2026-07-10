class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0

        for r in range(len(arr)):
            if r-l+1 > k:
                l += 1
            if r-l+1 == k:
                window_avg = sum(arr[l:r+1])/k
                if window_avg >= threshold:
                    res += 1


        return res
        