class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, visit, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prev > heights[r][c] or (r,c) in visit:
                return
            
            visit.add((r,c))
            for d1, d2 in directions:
                dfs(r + d1, c + d2, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            dfs(r, 0, pac, heights[r][0])

        
        u = atl.intersection(pac)
        res = [[r, c] for r, c in u]

        return res
