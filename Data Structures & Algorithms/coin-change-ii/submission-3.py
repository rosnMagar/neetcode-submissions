class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # coins.sort()
        dp = [[0 for j in range(n + 1)] for i in range(amount + 1)]

        for c in range(n + 1):
            dp[0][c] = 1
        
        for a in range(amount + 1):
            for i in range(n - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a >= coins[i]:
                    dp[a][i] += dp[a - coins[i]][i]
        
        return dp[amount][0]

