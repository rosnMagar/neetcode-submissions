class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # first pass that checks if the pacific shore can be reached
        # second pass to check if the atlantic shore can be reached
        # if both can be reached then those can flow water from pacific to atlantic

        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, prev, visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or prev > heights[r][c]:
                return

            visited.add((r, c)) 
            for d1, d2 in directions:
                dfs(r + d1, c + d2, heights[r][c], visited)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        intersect = pacific.intersection(atlantic)        

        return [[r, c] for r, c in intersect]