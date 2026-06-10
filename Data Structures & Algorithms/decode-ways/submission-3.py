class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {}
        
        def recursive(i):
            if i in dp.keys():
                return dp[i]

            if i >= len(s):
                return 1

            if s[i] == "0":
                dp[i] = 0
                return 0
            
            res = 0 
            if i <= len(s) - 1 and int(s[i]) != 0:
                res += recursive(i + 1)
            
            if i <= len(s) - 2 and int(s[i: i + 2]) <= 26:
                res += recursive(i + 2)

            dp[i] = res 
            return res
        
        return recursive(0)
