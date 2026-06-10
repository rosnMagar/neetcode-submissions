class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if (r,c) in visited or r > ROWS - 1 or c > COLS - 1 or r < 0 or c < 0 or grid[r][c] == "0": 
                return False
            
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return True

        for c in range(0, COLS):
            for r in range(0, ROWS):
                if dfs(r, c):
                    res += 1

        return res