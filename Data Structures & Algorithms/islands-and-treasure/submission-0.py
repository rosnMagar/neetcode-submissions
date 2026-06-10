class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # MULTI SOURCE BFS

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r, c))

        def addCell(r, c):
            if c < 0 or r < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == -1:
                return 
            
            visited.add((r, c))
            q.append((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft();
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

                grid[r][c] = dist
            dist += 1


                
