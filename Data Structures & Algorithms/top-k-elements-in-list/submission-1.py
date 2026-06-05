class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # num -> count

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
            
        counterArr = []
        for num, count in counter.items():
            counterArr.append([count, num])

        counterArr.sort()
        res = []
        while len(res) < k:
            res.append(counterArr.pop()[1])

        return res
