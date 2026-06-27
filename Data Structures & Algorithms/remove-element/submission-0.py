class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''

        #1
        match replace inft
        sort asc

        #2
        tmp variable
        replace back

        '''

        temp = []

        for num in nums:
            if num != val:
                temp.append(num)

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)