class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        def dfs(r,c):
            #base case
            if r < 0 or r >= ROW:
                return 1

            if c < 0 or c >= COL:
                return 1

            if grid[r][c] == 0:
                return 1

            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            


            perimeter = dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return perimeter

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return dfs(r,c)

        return 0


        