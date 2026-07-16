class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def recurse(amt):
            if amt in dp:
                return dp[amt]
            if amt == 0:
                return 0
            if amt < 0:
                return -1

            res = 9e9
            for c in coins:
                op = recurse(amt - c)
                if op == -1:
                    continue
                res = min(res, op + 1)
            if res == 9e9:
                res = -1
            dp[amt] = res
            return res

        return recurse(amount)