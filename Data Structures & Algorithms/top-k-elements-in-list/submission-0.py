class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # num -> count

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        arr = []
        for num,cnt in counter.items():
            arr.append([cnt,num])

        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res      

