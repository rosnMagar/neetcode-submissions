class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m x n
        # m rows and n columns
        # 5 element in 3 x 4 matrix
        # at index 4
        # 4 // 4 = 1
        # 4 % 4 = 0

        # 3 x 4 matrix
        # 10th element
        # 10 // 4 = 2
        # 10 % 4 = 2

        # 3 x 4
        # 7th element
        # 7 // 4 = 1
        # 7 % 4 = 3

        # general formula
        # number of columns
        # ith index of an elemnt to convert it into the matrix ij format of 
        # locating an element
        # ith = cth // column_length
        # jth = cth % column_length


        # number of columns
        n = len(matrix[0])

        # number of rows
        m = len(matrix)

        hi = (m * n) - 1
        lo = 0
        pos = 0 

        while lo <= hi:
            pos = (hi + lo) // 2

            # converting the pos to matrix ij format
            i = pos // n
            j = pos % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = pos + 1
            else:
                hi = pos - 1
        
        return False
            


