class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None] * n for _ in range(m)]

        def rec(m, n):
            if dp[m][n] is not None:
                return dp[m][n]
            if m == 0 and n == 0:
                return 1
            if m < 0 or n < 0:
                return 0
            
            dp[m][n] = rec(m - 1, n) + rec(m, n - 1)

            return dp[m][n]
        
        return rec(m - 1, n - 1)