class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        fresh = 0

        visited = set()
        q = deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r,c))
                
        while q and fresh > 0:
            length = len(q)
            proceed = False
            for i in range(length):
                row, col = q.popleft()

                for d1, d2 in directions:
                    r, c = row + d1, col + d2 
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                        grid[r][c] = 2
                        visited.add((r,c))
                        q.append((r,c))
                        fresh -= 1

            res += 1
        
        return res if fresh <= 0 else -1

                

        