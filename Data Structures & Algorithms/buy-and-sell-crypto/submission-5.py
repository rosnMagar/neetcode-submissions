class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # smallest and largest two pointer approach
        smallest = prices[0]
        profit = 0

        for p in prices:
            smallest = min(smallest, p)
            profit = max(profit, p - smallest)
        
        return profit
        