class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # assuming we don't go diagonally

        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        # reset it every time we start
        visited = set() 

        def dfs(r, c, w):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or word[len(w)] != board[r][c]:
                return False
            w += board[r][c]
            visited.add((r, c))

            if w == word:
                return True

            for d1, d2 in directions:
                if dfs(r + d1, c + d2, w):
                    return True
            visited.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                if word[0] == board[r][c] and dfs(r, c, ''):
                    return True
        
        return False