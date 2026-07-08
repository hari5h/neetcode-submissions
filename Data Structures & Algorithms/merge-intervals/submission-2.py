class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            int1 = res[-1]
            int2 = intervals[i]

            #int1 end > int2 start
            if int1[1] >= int2[0]:
                res[-1][1] = max(res[-1][1], int2[1])
            else:
                res.append(int2)

        return res

        