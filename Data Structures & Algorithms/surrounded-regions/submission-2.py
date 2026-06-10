class Solution:
    def solve(self, board: List[List[str]]) -> None:

        """
        Graph Problem:
        2nd approach
        connected to any outer 0 is safe
        """

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        safe = set()

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]] 

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or (r, c) in visited or board[r][c] == "X":
                return

            visited.add((r,c)) 
            safe.add((r,c))
            for d1, d2 in directions:
                dfs(r + d1, c + d2)
            
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # final pass
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe:
                    board[r][c] = "X"

        
        