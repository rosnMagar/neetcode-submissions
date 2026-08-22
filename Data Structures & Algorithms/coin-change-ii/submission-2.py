class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]

        for c in range(n + 1):
            dp[c][0] = 1
        
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i+1][a]
                    dp[i][a] += dp[i][a - coins[i]]
        
        return dp[0][amount]

