class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # num -> count

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        FreqeunceArr = [[] for i in range(len(nums)+1)]

        for num, count in counter.items():
            FreqeunceArr[count].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            temp = FreqeunceArr[i]
            for j in temp:
                res.append(j)
                if len(res) == k:
                    return res

        return [] 



        # Sort method
        counterArr = []
        for num, count in counter.items():
            counterArr.append([count, num])

        counterArr.sort()
        res = []
        while len(res) < k:
            res.append(counterArr.pop()[1])

        return res

        # Time: O(nlogn) and Space: O(n)
