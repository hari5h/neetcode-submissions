class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        [1,1,3,2]
        for cur_indx, temp in enumerate(temperatures):
            # stack pop
            while stack and temp > stack[-1][0]:
                _, indx = stack.pop()
                res[indx] = cur_indx - indx

            

            # stack append
            stack.append([temp, cur_indx])
        
        return res