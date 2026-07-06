class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dp(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1

            s1 = s[i]
            s2 = s[i: i + 2]

            ways = 0

            if s1 != "0":
                ways += dp(i + 1)
            
            if int(s2) < 27 and int(s2) > 9:
                ways += dp(i + 2)
            cache[i] = ways
            return ways
        
        return dp(0)