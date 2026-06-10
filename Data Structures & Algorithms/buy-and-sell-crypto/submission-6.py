class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0
        
        p1 = 0
        p2 = 1
        profit = 0

        while p2 < len(prices):
            profit = max(profit, prices[p2] - prices[p1])

            if prices[p2] < prices[p1]:
                p1 = p2

            p2 += 1
        
        return profit