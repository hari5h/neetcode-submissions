class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        nlogn
        n
        pointer --> counter {}
        []
        sort
        '''

        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        counter_arr = []
        for key,val in counter.items():
            counter_arr.append([key, val])
        
        counter_arr.sort(key= lambda x:x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(counter_arr[i][0])

        return res

