class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0],[-1,0], [0,1], [0,-1]]
        def bfs(r,c):
            dist = 0
            deque = collections.deque()
            deque.append((r,c))
            visited = set((r,c))

            while deque:

                length = len(deque)
                for i in range(length): #level
                    r, c = deque.popleft()
                    if grid[r][c] == 0:
                        return dist
                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc

                        if row in range(ROW) and col in range(COL) and (row, col) not in visited and grid[row][col] != -1:
                            visited.add((row, col))
                            deque.append((row, col))
                dist+= 1

            return -1
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r,c)

        
        