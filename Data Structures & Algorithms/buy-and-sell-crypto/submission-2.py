class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            new_profit = prices[r] - prices[l]
            
            if new_profit < 0:
                l = r
            else:
                profit = max(profit, new_profit)
            
            r += 1
        
        return profit




            

        