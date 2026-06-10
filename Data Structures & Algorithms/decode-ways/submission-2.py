class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1] * len(s)
        # REDO with actual DP 
        def recursive(i):
            if i < len(s) and cache[i] != -1:
                return cache[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            res = recursive(i + 1)

            if i < len(s) - 1 and int(s[i: i + 2]) <= 26:
                res += recursive(i + 2)

            cache[i] = res 
            return res

        return recursive(0)
