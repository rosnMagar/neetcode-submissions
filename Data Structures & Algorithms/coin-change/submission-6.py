class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def rec(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            res = 1e10
            for c in coins: 
                if amount - c >= 0:
                    res = min(res, rec(amount - c) + 1)

            dp[amount] = res 
            return res

        minCoins = rec(amount)
        return -1 if minCoins >= 1e10 else minCoins 
