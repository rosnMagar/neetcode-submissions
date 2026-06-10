class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        # can also use a visited set
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r > ROWS - 1 or c > COLS - 1 or r < 0 or c < 0 or grid[r][c] == "0": 
                return
            
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(0, COLS):
            for r in range(0, ROWS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1

        return res