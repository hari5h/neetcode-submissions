class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        deque = collections.deque()
        fresh = 0
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    deque.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while deque and fresh:
            length = len(deque)

            #level
            for i in range(length):
                nr, nc = deque.popleft()

                for dr, dc in directions:
                     r = nr + dr
                     c = nc + dc

                     if r in range(ROW) and c in range(COL) and grid[r][c] == 1:
                        grid[r][c] = 2
                        deque.append((r,c))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
        
        