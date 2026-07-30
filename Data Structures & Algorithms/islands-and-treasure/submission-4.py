class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        def traverse(r, c, val):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit:
                return
            q.append((r, c))
            visit.add((r, c))
            grid[r][c] = val + 1

        while q:
            r, c = q.popleft()
            val = grid[r][c]
            traverse(r + 1, c, val)
            traverse(r - 1, c, val)
            traverse(r, c + 1, val)
            traverse(r, c - 1, val)
        