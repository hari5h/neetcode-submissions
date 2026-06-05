class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for row in matrix:
            l,r = 0, len(row)-1
            while l <= r:
                m = (l+r)//2

                if row[m] == target:
                    return True
                elif target > row[m]:
                    l = m+1
                else:
                    r=m-1

        return False 