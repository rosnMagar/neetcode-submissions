class Solution:
    def convert(self, val, matrix):
        rows, columns = len(matrix), len(matrix[0])
        r = val // (columns)
        c = val % (columns)
        return r, c

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) * len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            row, col = self.convert(m, matrix) 
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        
        return False
