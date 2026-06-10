class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(0, 9)]
        cols = [set() for i in range(0, 9)]

        """
        Since it is a 9x9 grid we can hard-code the window scanning method
        """

        for i in range(9):
            r = (i // 3) * 3
            c = ((i % 3) * 3)
            grid_set = set()
            for ri in range(3):
                for ci in range(3):
                    val = board[ri + r][ci + c] 
                    if val == ".":
                        continue
                    if val in grid_set or val in rows[ri + r] or val in cols[ci + c]:
                        return False
                    grid_set.add(val)
                    rows[ri + r].add(val)
                    cols[ci + c].add(val)
        return True





