class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # [i, temp]

        for ind,temp in enumerate(temperatures):
            while len(stack) and stack[-1][1] < temp:
                prevInd, prevTemp = stack.pop()
                output[prevInd] = ind - prevInd
            stack.append([ind, temp])
        
        return output


