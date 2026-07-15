class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        pac, atl = set(), set()

        def dfs(r, c, prev, visit):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or prev > heights[r][c]:
                return
            visit.add((r, c))

            for d1, d2 in directions:
                dfs(r + d1, c + d2, heights[r][c], visit)
            
        for c in range(COLS):
            dfs(0, c, 0, pac)
            dfs(ROWS - 1, c, 0, atl)

        for r in range(ROWS):
            dfs(r, 0, 0, pac)
            dfs(r, COLS - 1, 0, atl)
        
        intersection = pac.intersection(atl) 

        return [[r, c] for r, c in intersection]
        
