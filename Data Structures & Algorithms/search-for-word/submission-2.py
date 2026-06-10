class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # MEMORIZE/REVIEW this method
        # Follows a similar pattern for these type of questions

        # Dimentions
        ROWS, COLS = len(board), len(board[0])

        # no revisit
        path = set()
        # sort of a DFS Approach?
       
        def dfs(r, c, i):
            if i == len(word):
                return True
            if c < 0 or r < 0 or c >= COLS or r >= ROWS or word[i] != board[r][c] or (c, r) in path:
                return False

            path.add((c,r))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((c, r))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


