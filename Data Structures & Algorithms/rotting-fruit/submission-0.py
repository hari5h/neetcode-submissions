class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        fresh = 0
        deque = collections.deque()
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    deque.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while deque and fresh:
            length = len(deque)
            
            for i in range(length): #level
                cr, cc = deque.popleft()

                for r, c  in directions:
                    dr = r + cr
                    dc = c + cc
                    if dr in range(ROW) and dc in range(COL) and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        fresh -= 1
                        deque.append((dr, dc))
            time += 1
        return time if fresh == 0 else -1

                
                    
                
                 


        