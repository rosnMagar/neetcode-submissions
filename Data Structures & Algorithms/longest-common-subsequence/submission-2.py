class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0] * len(text2) for i in range(len(text1))]

        def dp(r, c):
            if r == len(text1) or c == len(text2):
                return 0
            if cache[r][c] != 0:
                return cache[r][c]
            
            result = 0
            if text1[r] == text2[c]:
                result = 1 + dp(r + 1, c + 1)
            else:
                result = max(dp(r + 1, c), dp(r, c + 1))
            cache[r][c] = result 
            return result
        
        return dp(0, 0)