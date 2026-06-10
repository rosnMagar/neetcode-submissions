class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp ={0: 0} 
        def recursive(n):
            if n in dp.keys():
                return dp.get(n)
           
            res = 1e8
            for c in coins:
                if n - c >= 0:
                    res = min(res, recursive(n - c) + 1)
            
            dp[n] = res
            return res

        result = recursive(amount) 
        if result == 1e8:
            return -1  
        
        return result