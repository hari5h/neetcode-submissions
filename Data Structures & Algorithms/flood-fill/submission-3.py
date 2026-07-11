class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        origin = image[sr][sc]

        if origin == color:
            return image


        def dfs(r, c):
            if r < 0 or r >= ROW:
                return
            
            if c < 0 or c >= COL:
                return

            if image[r][c] != origin:
                return

            #process cell
            image[r][c] = color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        dfs(sr, sc)

        return image
        