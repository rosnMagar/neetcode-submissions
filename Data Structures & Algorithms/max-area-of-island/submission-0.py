class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == 0:
                return 0 

            grid[r][c] = 0

            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1
        
        for c in range(COLS):
            for r in range(ROWS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res

