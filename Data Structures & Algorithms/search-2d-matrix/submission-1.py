class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_len = len(matrix)
        c_len = len(matrix[0])
        length = r_len * c_len
        lo = 0
        hi = length - 1

        while lo <= hi:
            m = (hi + lo) // 2
            r = m // c_len
            c = m % c_len

            hval = matrix[hi // c_len][hi % c_len]
            lval = matrix[lo // c_len][lo % c_len]

            if target < matrix[r][c]:
                hi = m - 1
            elif target > matrix[r][c]:
                lo = m + 1
            else:
                return True
        
        return False