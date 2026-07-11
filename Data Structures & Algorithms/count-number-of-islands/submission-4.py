class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1 , 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = "*"
            for d1, d2 in directions:
                dfs(r + d1, c + d2)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res