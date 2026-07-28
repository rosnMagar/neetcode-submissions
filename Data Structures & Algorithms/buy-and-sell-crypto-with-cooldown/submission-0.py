class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def rec(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in cache.keys():
                return cache[(i, buy)]

            # cooldown 
            cooldown = rec(i + 1, buy)

            if not buy:
                # either sell or cooldown
                v = rec(i + 2, not buy) + prices[i]
                cache[(i, buy)] = max(v, cooldown)
            else:
                v = rec(i + 1, not buy) - prices[i]
                cache[(i, buy)] = max(v, cooldown)
            return cache[(i, buy)]
            
        return rec(0, True)

