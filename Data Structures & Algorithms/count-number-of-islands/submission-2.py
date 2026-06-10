class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res




        