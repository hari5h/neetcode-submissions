class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        visit = set()

        def dfs_area(r, c):
            if r < 0 or r >= ROW:
                return 0

            if c < 0 or c >= COL:
                return 0

            if grid[r][c] == 0:
                return 0

            if (r, c) in visit:
                return 0

            visit.add((r,c))

            return (1 + dfs_area(r+1,c) +
                dfs_area(r-1,c) +
                dfs_area(r,c+1) +
                dfs_area(r,c-1))




        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs_area(r,c) 
                    max_area = max(area, max_area)

        return max_area